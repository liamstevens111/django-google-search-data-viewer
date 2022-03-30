from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.shortcuts import render, redirect

# from django.contrib.auth.forms import AuthenticationForm

from .forms import UserSignUpForm, UserAuthenticationForm
from .services import user_create

def signup(request):
  if request.method == 'POST':
      form = UserSignUpForm(request.POST)
      if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')
        
        # form.save()
        user_create(email=email, password=password)

        user = authenticate(email=email, password=password)
        auth_login(request, user)
        return redirect('home')
  else:
      form = UserSignUpForm()
  return render(request, 'users/signup.html', {'form': form})


def login(request):
  if request.method == 'POST':
    form = UserAuthenticationForm(request, data=request.POST)
    if form.is_valid():
      user = form.get_user()
      auth_login(request, user)
      return redirect('home')
  else:
      form = UserAuthenticationForm(request)
  return render(request, 'users/login.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('home')
