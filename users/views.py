from django.shortcuts import render, redirect
from .forms import RegistrationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
# Create your views here.

def user_register(request):
    register_form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request, request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("users:login")
    context = {'register_form':register_form}
    return render(request, 'users/register.html', context)

def user_login(request):
    login_form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are logged in as {username}")
                return redirect("main:home")

    context = {'login_form':login_form}
    return render(request, 'users/login.html', context)
