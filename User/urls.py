from django.urls import path

import User.views

urlpatterns = [
    path('calender', User.views.calender, name='calender'),
    path('calender/<int:year>/<str:month>', User.views.calender, name='calender'),
    path('profile/', User.views.profile, name='profile'),
    path('profile/<str:btnSelect>', User.views.profile, name='profile'),
    path('profile/<str:btnSelect>/changeinfo', User.views.changeInfo, name='changeinfo')
]
