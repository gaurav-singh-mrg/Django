from django.shortcuts import render
from django.http import response
from django.views.generic.base import TemplateView


# Create your views here.

def LoginAction(request):
    return render(request, 'Login.html')


def SigninAction(request):
    return render(request, 'index.html')


class simpleauth(TemplateView):
    template_name = "MainTemplate.html"

    def get_context_data(self, **kwargs):
        context = super.get_context_date(**kwargs)
        return context

class auth(TemplateView):
    template_name = "AuthTemplate.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Title'] = "Welcome,Please Login"
        context['Header'] = 'Login Here'
        context['ButtonName'] = 'Login'
        return context
