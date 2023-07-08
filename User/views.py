from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from django.contrib.auth.models import User
from AddUser.models import FollowData
from Browse.models import imageUploaded


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
def profile(request, btnSelect='media'):
    user = User.objects.filter(id=request.user.id).values('id', 'username', 'first_name', 'last_name')
    Follower = FollowData.objects.filter(UserId=request.user.id).count()
    Following = FollowData.objects.filter(FollowersId=request.user.id).count()
    context = {
        'userinfo': user,
        'Follower': Follower,
        'Following': Following
    }
    if btnSelect == 'media':
        print("media")
        user_photos = imageUploaded.objects.filter(userID=request.user.id, Active=True).values('id', 'imageField',
                                                                                               'caption')
        context['media'] = user_photos
        return render(request, 'User/profile.html', context)
    if btnSelect == 'settings':
        print("settings selected")
        return render(request, 'User/profile.html', context)
    if btnSelect == 'tagged':
        print("tagged")
        return render(request, 'User/profile.html', context)
