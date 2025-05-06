
from django.shortcuts import render, redirect
from .models import InterviewExperience
from .forms import ExperienceForm

def experience(request):
    experiences = InterviewExperience.objects.all().order_by('-created_at')
    return render(request, 'experience.html', {'experiences': experiences})

def submit_experience(request):
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('experience')
    else:
        form = ExperienceForm()
    return render(request, 'submit.html', {'form': form})

def home_page(request):
    return render(request,'home_page.html')

