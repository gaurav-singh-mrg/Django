from django.urls import path
from django.views.generic import TemplateView
import Auth
from Auth import views

urlpatterns = [
    # Auth Urls Start
    path('', Auth.views.simpleauth.as_view()),
    path('login/', Auth.views.auth.as_view()),
    path('signin/', TemplateView.as_view(template_name="AuthTemplate.html",
                                         extra_context={'Title': 'Welcome, Please SignIn',
                                                        'ButtonName': 'SignIn',
                                                        'Header': 'SignIn Here',
                                                        'method': 'post',
                                                        'ButtonAction': 'SigninAction'})),
    # path('simpleSignIn/', TemplateView.as_view(template_name="AuthSampleTemplate.html",
    #                                            extra_context={'Title': 'Welcome, Please SignIn',
    #                                                           'ButtonName': 'SignIn',
    #                                                           'Header': 'SignIn Here',
    #                                                           'method': 'post',
    #                                                           'ButtonAction': 'SigninAction'})),
    path('login/loginAction', Auth.views.LoginAction),
    path('signin/SigninAction', Auth.views.SigninAction),
    # path('simpleSignIn/SigninAction', Auth.views.SigninAction),
    path('test', Auth.views.auth.as_view(), name='AuthTemplate.html')

    # Auth Urls END
]
