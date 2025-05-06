from django.db import models

# Create your models here.
class InterviewExperience(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    experience = models.TextField()
    interview_question = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.company}"