from django.urls import path
from . import views

urlpatterns = [
    path('', views.getinfo, name='Info'),
    path('info', views.getinfo, name='Info')
]
