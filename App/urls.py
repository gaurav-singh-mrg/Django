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
from django.views.generic import TemplateView
import Auth.views
from django.urls import include

import User
from Auth import urls
from User import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Auth.views.index),
    # Auth Urls Start
    path('auth/', include(Auth.urls)),
    # path('test', TemplateView.as_view(template_name="AuthTemplate.html",
    #      extra_context={'title': 'Welcome to gaurav'}))
    # path('test', Auth.views.auth.as_view()),
    # Auth Urls END
    path('accounts/', include("django.contrib.auth.urls")),
    path('users/', include(User.urls), name='User')
]
