from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    BRANCH_CHOICES = [
        ('100', 'Branch 100'),
        ('101', 'Branch 101'),
        ('102', 'Branch 102'),
    ]
    branch = models.CharField(max_length=3, choices=BRANCH_CHOICES)
