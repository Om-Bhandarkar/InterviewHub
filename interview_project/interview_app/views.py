
from django.shortcuts import render, redirect
from .models import InterviewExperience
from .forms import ExperienceForm
from django.contrib import messages
def experience(request):
    experiences = InterviewExperience.objects.all().order_by('-created_at')
    return render(request, 'experience.html', {'experiences': experiences})

def submit_experience(request):
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
            # messages.success(request,"Form Submitted Successfully ...")
    else:
        form = ExperienceForm()
        # messages.error(request,"fill the form properly")
    return render(request, 'submit.html', {'form': form})

def home_page(request):
    return render(request,'home_page.html')


def thank_you(request):
    return render(request,'thank_you.html')

