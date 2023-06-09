from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as ln, logout
from AddUser.models import users_info


# Create your views here.

def Login(request):
    if request.method == "POST":
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        user = authenticate(username=username, password=password)
        if user is not None:
            ln(request, user)
            return render(request, "Home/home.html")
        return redirect('')
    signup = False
    Title = "Welcome,Please Login"
    Header = 'Log In'
    ButtonName = 'Login'
    showEmailField = False
    return render(request, 'Auth/AuthTemplate.html', locals())
    # return render(request, 'Home/home.html', locals())


def Logout(request):
    logout(request)
    return Login(request)


def signin(request):
    if request.method == "POST":
        username = request.POST.get('username', False)
        email = request.POST.get('email', False)
        Fname = request.POST.get('Fname', False)
        Lname = request.POST.get('Lname', False)
        ConfirmPassword = request.POST.get('ConfirmPassword', False)
        password = request.POST.get('password', False)
        # print(username, email, password)

        if not username.isalnum():
            messages.info(request, "Username should be alphanumeric only ", fail_silently=True)
        elif not Fname.isalpha():
            messages.info(request, "Firstname should not contain numeric digits", fail_silently=True)
        elif not Lname.isalpha():
            messages.info(request, "Lastname should not contain numeric digits", fail_silently=True)
        elif password != ConfirmPassword:
            messages.info(request, "Password doesn't match")
        else:
            myuser = User.objects.create_user(username, email, password)
            userid = User.objects.get(username=username)
            users_info(userid=userid).save()
            print(f"users_info {userid.id}")
            return render(request, "Auth/Login.html")

    Title = "Welcome,Please signin"
    Header = 'Sign In'
    ButtonName = 'Signin'
    signup = True
    return render(request, 'Auth/AuthTemplate.html', locals())


def index(request):
    messages.info(request, 'Welcome Please login', fail_silently=True)
    Title = "Welcome, Homepage"
    return render(request, 'Auth/index.html', locals())

