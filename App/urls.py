"""App URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import AddUser
import Auth.views
import Home
from django.urls import include

from Home import urls
import User
from Auth import urls
from User import urls
from AddUser import urls
from Browse import urls as browseUrl

urlpatterns = [
    path(r'admin/', admin.site.urls, name='admin'),
    path('', Auth.views.index, name='index'),
    path('auth/', include(Auth.urls), name='auth'),
    path('users/', include(User.urls), name='User'),
    path('adduser/', include(AddUser.urls), name='AddUser'),
    path('home/', include(Home.urls), name='profile'),
    path('browse/', include(browseUrl), name='Browse')
]
