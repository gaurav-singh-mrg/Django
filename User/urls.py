from django.urls import path

import User.views

app_name = 'user'
urlpatterns = [
    path('calender', User.views.calender, name='calender'),
    path('calender/<int:year>/<str:month>', User.views.calender, name='calender'),
    path('profile/changeinfo', User.views.changeInfo, name='changeinfo'),
    path('profile/', User.views.profile, name='profile'),
    path('profile/<str:btnSelect>', User.views.profile, name='profile'),

]
