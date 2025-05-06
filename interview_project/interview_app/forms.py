from django import forms
from .models import InterviewExperience

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = InterviewExperience
        fields = ['name', 'email', 'company', 'position', 'experience','interview_question']