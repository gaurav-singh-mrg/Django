from django.conf.global_settings import LOGIN_REDIRECT_URL
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as ln, logout

import Auth
from AddUser.models import users_info
from . import forms


# Create your views here.

def Login(request):
    if request.method == "POST":
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        user = authenticate(username=username, password=password)
        if user is not None:
            ln(request, user)
            return redirect('home')
    signup = False
    Title = "Welcome,Please Login"
    Header = 'Log In'
    ButtonName = 'Login'
    showEmailField = False
    form = forms.LoginForm()
    return render(request, 'Auth/Login.html', locals())
    # return render(request, 'Home/home.html', locals())


def Logout(request):
    logout(request)
    redirect(LOGIN_REDIRECT_URL)


def signin(request):
    if request.method == "POST":
        username = request.POST.get('UserId', False)
        email = request.POST.get('EmailId', False)
        Fname = request.POST.get('FirstName', False)
        Lname = request.POST.get('LastName', False)
        ConfirmPassword = request.POST.get('ConfirmPassword', False)
        password = request.POST.get('Password', False)

        SigninForm = forms.SignUpForm(request.POST)
        oldUser = not {User.objects.filter(username=username).exists()}
        print(f'Olduser => {oldUser}')
        print(f'SigninForm => {SigninForm.is_valid()}')
        if SigninForm.is_valid() and not oldUser:
            myuser = User.objects.create_user(username, email, password)
            userid = User.objects.get(username=username)
            users_info(userid=userid).save()
            print(f"users_info {userid.id}")
            return render(request, 'Auth/Login.html', locals())
        else:
            print("Invalid Form")
    Title = "Welcome,Please signin"
    Header = 'Sign In'
    ButtonName = 'Signin'
    signup = True
    form = forms.SignUpForm()
    return render(request, 'Auth/Signin.html', locals())


def index(request):
    if request.user.is_authenticated:
        return redirect("/home")
    else:
        messages.info(request, 'Welcome Please login', fail_silently=True)
        Title = "Welcome, Homepage"
        return render(request, 'Auth/index.html', locals())
