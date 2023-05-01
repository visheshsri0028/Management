from django import forms
from .models import signup


class signup(forms.Form):
    full_name = forms.CharField(max_length=50)
    username = forms.CharField(max_length=50)
    number = forms.IntegerField()
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)
