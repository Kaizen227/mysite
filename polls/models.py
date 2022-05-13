from django.db import models
from django.urls import reverse

# Create your models here.

class Sign(models.Model):
    email = models.EmailField(max_length=25)
    password = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.email

    def __str__(self) -> str:
        return self.password
