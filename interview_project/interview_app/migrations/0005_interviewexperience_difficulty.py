# Generated by Django 4.0.5 on 2025-05-11 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview_app', '0004_alter_interviewexperience_company_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='interviewexperience',
            name='difficulty',
            field=models.CharField(choices=[('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')], default='Medium', max_length=10),
        ),
    ]
