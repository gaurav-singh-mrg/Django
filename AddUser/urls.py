from django.urls import path
from . import views

app_name = 'adduser'
urlpatterns = [
    path('', views.getinfo, name='allinfo'),
    path('info', views.getinfo, name='info'),
    path('calender', views.getinfo, name='calender'),
    path('follow/<int:id>', views.followbtn, name='FollowRequest'),
]
