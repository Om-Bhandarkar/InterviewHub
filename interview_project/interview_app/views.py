
from django.shortcuts import render, redirect
from .models import InterviewExperience
from .forms import ExperienceForm,ExperienceFilterForm
from django.contrib import messages


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


def submit_experience(request):
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = ExperienceForm()
    return render(request, 'interview_app/submit.html', {'form': form})

def home_page(request):
    return render(request,'interview_app/home_page.html')


def thank_you(request):
    return render(request,'interview_app/thank_you.html')

def login_page(request):
    return render(request,'interview_app/login_page.html')

def register_page(request):
    return render(request,'interview_app/register_page.html')




