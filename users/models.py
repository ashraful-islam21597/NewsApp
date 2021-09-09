from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    age=models.PositiveIntegerField(blank=True,null=True)
    Fullname=models.CharField(max_length=120)