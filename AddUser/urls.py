from django.urls import path
from . import views

app_name = 'adduser'
urlpatterns = [
    path('', views.GetInfo.as_view(), name='allinfo'),
    # path('info', views.getinfo, name='info'),
    path('info', views.GetInfo.as_view(), name='info'),
    path('pk/<int:pk>', views.UserDetailView.as_view(), name='UserDetailView'),
    # path('calender', views.getinfo, name='calender'),
    path('follow/<int:id>', views.followbtn, name='FollowRequest'),
]
