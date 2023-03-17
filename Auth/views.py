from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as ln, logout


# Create your views here.

def Login(request):
    if request.method == "POST":
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        user = authenticate(username=username, password=password)
        if user is not None:
            ln(request, user)
            return render(request, "Auth/index.html")
        return redirect('')
    signup = False
    Title = "Welcome,Please Login"
    Header = 'Log In'
    ButtonName = 'Login'
    showEmailField = False
    return render(request, 'Auth/AuthTemplate.html', locals())


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

# class index(TemplateView):
#     template_name = "index.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['Title'] = "Welcome,Homepage"
#         context['Header'] = 'Login Here'
#         context['ButtonName'] = 'Login'
#         return context

# class auth(TemplateView):
#     template_name = "AuthTemplate.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['Title'] = "Welcome,Please Login"
#         context['Header'] = 'Login Here'
#         context['ButtonName'] = 'Login'
#         return context
#
#     def post(self, request):
#         if self.request.method == "POST":
#             # print(request.__dict__, file=sys.stderr)
#             username = self.request.POST.get('username', False)
#             email = self.request.POST.get('email', False)
#             password = self.request.POST.get('password', False)
#             print(username, email, password)
#             myuser = User.objects.create_user(username, email, password)
#             # myuser.first_user =
#             # messages.success(request, 'Account created successfully')
#             return redirect(request, 'Login')
