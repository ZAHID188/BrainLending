from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='api_user_set',  # Change this name as needed
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='api_user_set',  # Change this name as needed
        blank=True
    )

    def __str__(self):
        return self.username
