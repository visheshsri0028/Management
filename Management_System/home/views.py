from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import SignupForm


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("success")
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})
