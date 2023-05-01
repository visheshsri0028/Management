from django import forms
from .models import signup


class UserForm(forms.ModelForm):
    class Meta:
        model = signup
        fields = ['full_name', 'username', 'number', 'password']
