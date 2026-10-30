from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    bio=models.TextField(blank=True)
    college=models.CharField(max_length=200,blank=True)
    github_link=models.URLField(blank=True)
    profile_image = models.ImageField(
    upload_to='profile_pics/',
    blank=True,
    null=True
    )

    cover_image = models.ImageField(
    upload_to='cover_photos/',
    blank=True,
    null=True
    )
    resume = models.FileField(
        upload_to='resumes/',
        blank=True,
        null=True
)

    skills = models.TextField(
        blank=True
    )
    experience_level = models.CharField(
    max_length=20,
    choices=[
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced')
    ],
    default='Beginner'

)
    linkedin_link = models.URLField(
    blank=True
)
    def __str__(self):
        return self.user.username
    