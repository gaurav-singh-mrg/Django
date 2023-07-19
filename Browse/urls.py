from django.urls import path
from . import views

app_name = 'browse'
urlpatterns = [
    path('', views.browse, name='Feed'),
    path('uploadImage', views.browse, name='uploadImage'),
    path('follow/<int:id>', views.browse, name='FollowRequest'),
]
