from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, TemplateView


# Create your views here.
@login_required(login_url='/auth/login')
def homepage(request):
    return render(request, "Home/home.html")


# we cand also use login decorator in url config file  like
# login_required(TemplateView.as_view(template_name="secret.html"))
@method_decorator(login_required, name="dispatch")
class Homepage(TemplateView):
    template_name = 'Home/home.html'
