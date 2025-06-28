from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

ROLE_CHOICES = [
    ('admin','Admin' ),
    ('student','Student' ),
]

class CustomUserManager(BaseUserManager):

    def create_user(self,email,role,password=None):
        if email is None:
            raise ValueError("User Must have email address")
        user = self.model(email=self.normalize_email(email),role=role)
        user.set_password(password)
        user.save(using= self._db)
        return user
    
    def create_superuser(self,email,role='admin', password=None):
        user = self.model(email=self.normalize_email(email),role=role,password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using= self._db)
        return user

class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique=True)
    role = models.CharField(choices=ROLE_CHOICES,max_length=10)
    is_active = models.BooleanField(default=True)
    is_staff  = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['role']

    def __str__(self):
        return self.email


class InterviewExperience(models.Model):
    DIFFICULTY_CHOICES = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField()
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    experience = models.TextField()
    interview_question = models.TextField(blank=False)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='Medium')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.company}"