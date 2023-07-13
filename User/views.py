from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from django.contrib.auth.models import User
from AddUser.models import FollowData
from Browse.models import imageUploaded
from AddUser.models import users_info


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
    profilepic1 = users_info.objects.filter(Userid=request.user.id).values('ProfilePic')
    a = profilepic1[0].get('ProfilePic')
    context = {
        'userinfo': user,
        'Follower': Follower,
        'Following': Following,
        'profilepic': a
    }
    if btnSelect == 'media':
        print("media")
        context['mediabtn'] = True
        userInfo = imageUploaded.objects.filter(userID=request.user.id, Active=True).values('id', 'imageField',
                                                                                            'caption')
        context['media'] = userInfo
        return render(request, 'User/profile.html', context)
    if btnSelect == 'settings':

        print("settings selected")
        userExtraInfo = users_info.objects.filter(Userid=request.user.id).values()
        context['settingsbtn'] = True
        context['settings'] = userExtraInfo
        if request.method == "POST":
            first_name = request.POST.get('first_name', False)
            # middle_name = request.POST.get('middle_name', False)
            last_name = request.POST.get('last_name', False)
            dateofbirth = request.POST.get('dateofbirth', False)
            country = request.POST.get('country', False)
            state = request.POST.get('state', False)
            profilepic = request.POST.get('profilepic', False)
            print(f'profilepic => {profilepic}')
            if first_name != '':
                user.first_name = first_name
                user.update(first_name=first_name)
            # if middle_name != '':
            #     pass
            #     user.update(middle_name=middle_name)
            if last_name != '':
                user.update(last_name=last_name)
            if dateofbirth != '':
                userExtraInfo.update(DateOfBirth=dateofbirth)
            if country != '':
                userExtraInfo.update(Country=country)
            if state != '':
                userExtraInfo.update(State=state)
            if profilepic:
                userExtraInfo.update(ProfilePic=profilepic)
        return render(request, 'User/profile.html', context)
    if btnSelect == 'tagged':
        print("tagged")
        return render(request, 'User/profile.html', context)
