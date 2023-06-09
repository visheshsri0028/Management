from django.db import models
from django.contrib.auth.hashers import *
# Create your models here.


class signup(models.Model):
    full_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    number = models.IntegerField()
    password = models.CharField(max_length=20)
    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('Unknown', 'Prefer Not To Say'),
    )
    gender = models.CharField(max_length=10, choices=GENDERS)

    def __str__(self):
        return f'{self.full_name}{self.username}{self.number}{self.password}'
