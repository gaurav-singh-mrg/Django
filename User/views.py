from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from django.contrib.auth.models import User
from AddUser.models import FollowData


# Create your views here.
@login_required(login_url='/auth/login')
def calender(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    year = year
    month = month.title()
    month_number = list(calendar.month_name).index(month)

    month_number = int(month_number)
    Cal = HTMLCalendar().formatmonth(year, month_number)
    return render(request, 'User/UserIndex.html', locals())


@login_required(login_url='/auth/login')
def profile(request):
    print(request.user)
    user = User.objects.filter(id=request.user.id).values()
    Follower = FollowData.objects.filter(FollowId=request.user.id).count()
    Following = FollowData.objects.filter(FollowerId=request.user.id).count()
    # username = user.username()
    print(f'Follower :{Follower} , Following :{Following}')
    print(user)
    context = {
        'userinfo': user,
        'Follower': Follower,
        'Following': Following
    }
    return render(request, 'User/profile.html', context)
