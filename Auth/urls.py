from django.urls import path
import Auth
import Home.views
from Auth import views
from Home import views

urlpatterns = [
    # Auth Urls Start
    path('', Auth.views.index, name='index'),
    path('signin/', Auth.views.signin, name='signin'),
    path('login/', Auth.views.Login, name='login'),
    path('home/', Home.views.Homepage, name='home'),
    path('logout/', Auth.views.Logout, name='logout')

    # Auth Urls END

]
