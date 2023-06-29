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
    a = FollowData.objects.filter(UserId=request.user.id).values('FollowersId')
    list = User.objects.exclude(id=request.user.id).values('id', 'username',
                                                           'first_name',
                                                           'last_name')
    c = User.objects.annotate(IsFollower=Case(
        When(id__in=[a], then=Value(True),
        default=Value(False))
    ),)

    b = User.objects.exclude(id__in=[a]).values('id', 'username',
                                                'first_name',
                                                'last_name')

    print(f'C => {list.query.__str__()}')
    return render(request, 'AddUser/UserInfo.html', locals())


@login_required(login_url='/auth/login')
def followbtn(request, id):
    # check for valid request id
    if request.user.id == id:
        print("Same user can't fallow itself")

    # try:
    isUserIDExist = User.objects.filter(id=id).count()
    # print(f'isUserIDExist => {isUserIDExist.query.__str__()}')

    isUserExist = User.objects.filter(id=request.user.id)
    print(f'isUserExist => {isUserExist.query.__str__()}')
    # except User.DoesNotExist():
    #     print("User id not exist")
    print(f'isUserIDExist => {isUserIDExist}')
    if isUserIDExist == 1:
        '''going to update follower count'''
        isDuplicate = FollowData.objects.filter(id=request.user.id, FollowersId=id).count()
        # isDuplicate = 0

        if isDuplicate > 0:
            print("Duplicate data , do not insert")
        else:
            print(f"Saving follow data {request.user.id} , {id}")
            c = FollowData(Active=True, UserId=request.user.id, FollowersId=id)
            c.save()
            # a = User.objects.get(id=id)
            # a.Followers.add(c)
    else:
        print("User id not exist")
    return getinfo(request)
