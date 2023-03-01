from django.db import models

# Create your models here.

class Bank(models.Model):
    user = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phonenum = models.TextField(max_length=11)
    balance = models.TextField()