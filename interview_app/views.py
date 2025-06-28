import random
from django.contrib import messages
from .forms import RegistrationForm
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import InterviewExperience,CustomUser
from .forms import ExperienceForm,ExperienceFilterForm
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

def get_token_for_user(user):
    refresh = RefreshToken.for_user(user)
    return{
        'refresh':str(refresh),
        'access': str(refresh.access_token)
    }

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            otp = str(random.randint(100000, 999999)) 
            request.session['user_data'] = form.cleaned_data
            request.session['otp'] = otp

            send_mail(
                subject='OTP Verification',
                message=f'Your OTP is {otp}',
                from_email='ombhandarkar1206@gmail.com',
                recipient_list= [form.cleaned_data['email']],
                fail_silently=False,
            )
            return redirect('verify-otp')
    else:
        form = RegistrationForm() 
    return render(request, 'interview_app/register_page.html', {'form': form})

def verify_otp(request):
    if request.method == 'POST':
        user_otp = request.POST.get('otp')
        session_otp = request.session.get('otp')

        if user_otp == session_otp:
            data = request.session.get('user_data')
            user = CustomUser(
                email=data['email'],
                role=data['role']
            )
            user.set_password(data['password'])  
            user.save()
            messages.success(request, 'Account is created. Please log in!')
            return redirect('login')
        else:
            messages.error(request, 'Invalid OTP')
            return render(request, 'interview_app/verify_otp.html')  

    return render(request, 'interview_app/verify_otp.html')  

def login_view(request):
  if request.method=='POST':
    user = authenticate(request,username=request.POST['email'],password=request.POST['password'])
    print(user)
    if user:
      login(request,user)
      request.session['access_token']=get_token_for_user(user)['access']
      return redirect('home')
    else:
      messages.error(request,'Invalid creadentials')
  return render(request,'interview_app/login_page.html')

def forgot_password(request):
   if request.method == 'POST':
      try:
         user = CustomUser.objects.get(email=request.POST['email'])
         otp = str(random.randint(100000,999999))
         request.session['forgot_email'] = user.email
         request.session['forgot_otp'] = otp
         send_mail('Password Reset OTP', f'Your OTP is: {otp}', 'ombhandarkar1206@gmail.com', [user.email])
         return redirect('verify_forgot_otp')
      except CustomUser.DoesNotExist:
         messages.error(request, 'Email not found')
   return render(request, 'interview_app/forgot_password.html')

def verify_forgot_otp(request):
   if request.method == 'POST':
      if request.POST['otp'] == request.session.get('forgot_otp'):
         if request.POST['new_password1'] == request.POST['new_password2']:
            user = CustomUser.objects.get(email = request.session['forgot_email'])
            user.set_password(request.POST['new_password1'])
            user.save()
            messages.success(request,'Password reset successful')
            return redirect('login')
         else:
            messages.error(request,'Password do not match')
      else:
         messages.error(request,"Invalid OTP")
         return render(request,'interview_app/verify_forgot_otp.html')
@login_required
def logout_view(request):
   logout(request)
   return redirect('home')
@login_required
def experience(request):
    form = ExperienceFilterForm(request.GET or None)
    experiences = InterviewExperience.objects.all().order_by('-created_at')
    if form.is_valid():
        company = form.cleaned_data.get('company')
        position = form.cleaned_data.get('position')
        difficulty = form.cleaned_data.get('difficulty')
        if company:
            experiences = experiences.filter(company__icontains=company)
        if position:
            experiences = experiences.filter(position__icontains=position)
        if difficulty:
            experiences = experiences.filter(difficulty=difficulty)

    context = {
        'form': form,
        'experiences': experiences
    }
    return render(request, 'interview_app/experience.html', context)


@login_required
def submit_experience(request):
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = ExperienceForm()
    return render(request, 'interview_app/submit.html', {'form': form})

def main_page(request):
    return render(request,'interview_app/home_page.html')

def home_page(request):
    data = {
       '📝 Experience Submission':'Share your interview journey through a clean and intuitive <strong>ExperienceForm</strong>',
       '🔍 Experience Filtering':'Search by company, role, or tags using the flexible <strong>ExperienceFilterForm</strong>.',
       '🔐 Route Protection': "Critical routes are secured with Django's <code>@login_required</code> decorator.",
       '📧 OTP Verification':'Verify identity securely using <strong>session-based OTP</strong> flows for login and registration.',
       '🎨 User Interface':'Polished UI powered by Bootstrap 5 ensures a responsive and modern experience.',
       '🤝 Community-Driven':'Foster learning and encouragement through shared stories and peer engagement.'
    }
    return render(request,'interview_app/home_page.html',{'data':data})


def thank_you(request):
    return render(request,'interview_app/thank_you.html')






