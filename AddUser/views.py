from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import users_info, FollowData
from django.contrib.auth.models import User
from django.db import connection
from collections import namedtuple
from django.db.models import Case, When, Value, Q, Count


# Create your views here.
@login_required(login_url='/auth/login')
def getinfo(request):
    # list = User.objects.exclude(id=request.user.id).values('id', 'username',
    #                                                        'first_name',
    #                                                        'last_name').select_related()
    list = User.objects.exclude(Followers=request.user.id).select_related().all()
    # a = FollowData.objects.exclude(User__id=request.user.id).select_related().all()
    c = users_info.objects.exclude(userid=2).select_related()
    print(list.query.__str__())
    print(c.query.__str__())
    return render(request, 'AddUser/UserInfo.html', locals())


@login_required(login_url='/auth/login')
def followbtn(request, id):
    # check for valid request id
    if request.user.id == id:
        print("Same user can't fallow itself")
    isUserIDExist = User.objects.filter(id=id).count()
    if isUserIDExist == 1:
        '''going to update follower count'''
        isDuplicate = FollowData.objects.filter(FollowId=request.user.id, FollowerId=id).count()
        # isDuplicate = 0
        if isDuplicate > 0:
            print("Duplicate data , do not insert")
        else:
            print(f"Saving follow data {request.user.id} , {id}")
            c = FollowData(FollowId=request.user.id, FollowerId=id)
            c.save()
            a = User.objects.get(id=id)
            print(a)
            a.Followers.add(c)
    return getinfo(request)
