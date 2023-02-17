import sys

from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import response
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User


# Create your views here.

def Login(request):
    return render(request, 'Login.html')


def SigninAction(request):
    print(request.method)
    if request.method == "POST":
        # print(request.__dict__, file=sys.stderr)
        username = request.POST.get('username', False)
        email = request.POST.get('email', False)
        password = request.POST.get('password', False)
        print(username, email, password)
        myuser = User.objects.create_user(username, email, password)
        return redirect(request, 'Login')

    return render(request, "Login.html")


def signin(request):
    print(f'Printing request method {request.method}')
    if request.method == "POST":
        username = request.POST.get('username', False)
        email = request.POST.get('email', False)
        password = request.POST.get('password', False)
        print(username, email, password)
        myuser = User.objects.create_user(username, email, password)
        return render(request, "Login.html")
    Title = "W̵̵̵elcome,Please signin"
    Header = 'Sign In'
    ButtonName = 'Signin'
    return render(request, 'AuthTemplate.html', locals())


class index(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Title'] = "Welcome,Homepage"
        # context['Header'] = 'Login Here'
        # context['ButtonName'] = 'Login'
        return context

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
#             # messages.succes(request, 'Account created successfully')
#             return redirect(request, 'Login')
