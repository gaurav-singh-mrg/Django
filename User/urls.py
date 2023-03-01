from django.urls import path

import User.views

print("inside superuser")
urlpatterns = {
    path('calender', User.views.calender, name='calender'),
    path('calender/<int:year>/<str:month>', User.views.calender, name='calender'),

}
