from django.shortcuts import render
from .models import users_info
from django.contrib.auth.models import User


# Create your views here.

def getinfo(request):
    list = User.objects.all()
    return render(request, 'AddUser/UserInfo.html', locals())
