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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(r'admin', admin.site.urls, name='admin'),
    path('', Auth.views.index, name='index'),
    path('auth/', include(Auth.urls, namespace='auth'), name='auth'),
    path('users/', include(User.urls, namespace='user'), name='User'),
    path('adduser/', include(AddUser.urls, namespace='adduser'), name='AddUser'),
    path(r'home/', include(Home.urls, namespace='home'), name='home'),
    path('browse/', include(browseUrl, namespace='browse'), name='Browse')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
