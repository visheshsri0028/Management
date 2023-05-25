from django.db import models
from django.contrib.auth.hashers import *


class Signup(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    number = models.IntegerField()
    password = models.CharField(max_length=20)
    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('Unknown', 'Prefer Not To Say'),
    )
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDERS)

    def __str__(self):
        return f'{self.name}{self.username}{self.number}{self.password}'
