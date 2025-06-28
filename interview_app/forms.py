from django import forms
from .models import InterviewExperience, CustomUser

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = InterviewExperience
        fields = ['name', 'email', 'company', 'position', 'experience', 'interview_question', 'difficulty']


class ExperienceFilterForm(forms.Form):
    company = forms.CharField(
        required=False,
        label='Company',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search Company'})
    )
    position = forms.CharField(
        required=False,
        label='Position',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search Position'})
    )
    difficulty = forms.ChoiceField(
        required=False,
        choices=[('', 'Any'), ('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')],
        label='Difficulty',
        widget=forms.Select(attrs={'class': 'form-control'})
    )


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}),
        label='Password'
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}),
        label='Confirm Password'
    )

    class Meta:
        model = CustomUser
        fields = ['email', 'role', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match")
