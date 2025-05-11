from django import forms
from .models import InterviewExperience

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = InterviewExperience
        fields = ['name', 'email', 'company', 'position', 'experience', 'interview_question', 'difficulty']

class ExperienceFilterForm(forms.Form):
    company = forms.CharField(required=False, label='Company', widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Search Company'}))
    position = forms.CharField(required=False, label='Position', widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Search Position'}))
    difficulty = forms.ChoiceField(
        required=False,
        choices=[('', 'Any'), ('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')],
        label='Difficulty',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
