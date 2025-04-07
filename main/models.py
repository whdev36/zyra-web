from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Default: username, first_name, last_name, email, password, etc.

    phone_number = models.CharField(max_length=30, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile-images/', blank=True, null=True)

    is_verified = models.BooleanField(default=False)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], blank=True)

    is_online = models.BooleanField(default=False)
    last_seen = models.DateTimeField(blank=True, null=True)
    # language = models.CharField(max_length=10, default='en')
    # timezone = models.CharField(max_length=50, default='UTC')