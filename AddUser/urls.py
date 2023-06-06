from django.urls import path
from . import views

urlpatterns = [
    path('', views.getinfo, name='Info'),
    path('info', views.getinfo, name='Info'),
    path('calender', views.getinfo, name='calender'),
    path('follow/<int:id>', views.followbtn, name='FollowRequest'),
]
