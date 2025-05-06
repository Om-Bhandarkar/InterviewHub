
from django.shortcuts import render, redirect
from .models import InterviewExperience
from .forms import ExperienceForm

def home(request):
    experiences = InterviewExperience.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'experiences': experiences})

def submit_experience(request):
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ExperienceForm()
    return render(request, 'submit.html', {'form': form})