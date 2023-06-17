from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
@login_required(login_url='/auth/login')
def Homepage(request):
    return render(request, "Home/home.html")
