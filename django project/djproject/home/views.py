from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.urls import reverse
from .forms import Bookingform, LoginForm, SignupForm

# Create your views here.

def index(request):
    if request.method == "POST":
        form = Bookingform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you! Your enquiry has been submitted. We'll get back to you within 24 hours.")
            return redirect(f"{reverse('home')}#enquiry")
    else:
        form = Bookingform()
    return render(request, 'index.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('welcome')
    else:
        form = LoginForm(request)
    return render(request, 'login.html', {'form': form})


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('welcome')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def welcome_view(request):
    return render(request, 'welcome.html')


def logout_view(request):
    auth_logout(request)
    return redirect('home')

