from django.urls import path
from django.views.generic import TemplateView
import Auth
from Auth import views

urlpatterns = [
    # Auth Urls Start
    # path('', Auth.views.simpleauth.as_view()),
    # path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('', Auth.views.index, name='index'),
    path('signin/', Auth.views.signin, name='signin'),
    path('login/', Auth.views.Login, name='login'),
    # path('login/', Auth.views.auth.as_view()),
    # path('signin/', TemplateView.as_view(template_name="AuthTemplate.html",
    #                                      extra_context={'Title': 'Welcome, Please SignIn',
    #                                                     'ButtonName': 'SignIn',
    #                                                     'Header': 'SignIn Here',
    #                                                     'method': 'post',
    #                                                     'ButtonAction': 'SigninAction'
    #                                                     })),
    # path('login/loginAction', Auth.views.LoginAction),
    # path('signin/SigninAction', Auth.views.SigninAction),
    # path('test', Auth.views.auth.as_view(), name='AuthTemplate.html')

    # Auth Urls END

]
