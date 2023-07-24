from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import CreateView, TemplateView


# Create your views here.
@login_required(login_url='/auth/login')
def homepage(request):
    return render(request, "Home/home.html")


class Homepage(TemplateView):
    template_name = 'Home/home.html'
