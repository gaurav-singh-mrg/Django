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
    # with connection.cursor() as c:
    #     c.execute('SELECT a.id ,a.username,a.first_name,a.last_name, b.* FROM public."auth_user" as a left join '
    #               'public."AddUser_followdata" b  on a.id = b.id')
    #     row = namedtuplefetchall(c)
    #     # print(f'row => {row}')
    #     for a in row:
    #         print(a)
    #     list = row
    list = User.objects.exclude(id=request.user.id).values('id', 'username',
                                                           'first_name',
                                                           'last_name')
    # print(list.query.__str__())
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
        if isDuplicate > 0:
            print("Duplicate data , do not insert")
        else:
            print(f"Saving follow data {request.user.id} , {id}")
            FollowData(FollowId=request.user.id, FollowerId=id).save()
            a = User.objects.filter(id=id)
            b = FollowData.FollowersId.set(a)
            print(b)
            # FollowData.FollowsID.set(User.id)

    return getinfo(request)
