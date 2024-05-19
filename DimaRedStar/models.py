# models.py

from django.db import models

# Create your models here.
from django.db import models

class Contact(models.Model):
    full_name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False)
    phone_number = models.CharField(max_length=20, blank=True)
    message = models.TextField(blank=False, max_length=500, default='')


