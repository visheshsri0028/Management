from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template.context_processors import csrf
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import *
from django.contrib.auth.hashers import *
from .forms import signup


def home(request):
    return render(request, 'home.html')


def signup(request):
    return render(request, "signup.html")


def success(request):
    return render(request, "success.html")


def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = user(
                name=form.cleaned_date['full_name'],
                username=form.cleaned_data['username'],
                number=form.cleaned_data['number'],
                password=form.cleaned_data['password'],
            )
            new_user.save()
            return redirect('success')
        else:
            form = UserForm()
        return render(request, 'signup.html', {'form': form})


def user_details(request, pk):
    user = User.objects.get(pk=pk)
    return render(request, 'success.html', {'user': user})


def signup1(request):
    if resuest.method == "POST":
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            hashed_password = make_password(password)
            user = User(
                username=request.POST['username'], password=hashed_password)
            user.save()
            return render(request, 'signup_success.html')
        else:
            error_message = "Passwords don't match"
            return render(request, 'signup.html', {'error_message': error_message})
    else:
        return render(request, 'signup.html')
