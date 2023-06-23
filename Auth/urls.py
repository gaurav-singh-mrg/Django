from django.contrib.auth.views import LogoutView
from django.urls import path
import Auth
import Home.views
from App import settings
from Auth import views
from Home import views

urlpatterns = [
    # Auth Urls Start
    path('', Auth.views.index, name='index'),
    path('signin/', Auth.views.signin, name='signin'),
    path('login/', Auth.views.Login, name='login'),
    path('home/', Home.views.Homepage, name='home'),
    # path('logout/', Auth.views.Logout, name='logout')
    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),

    # Auth Urls END

]
