from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import users_info, FollowData
from django.contrib.auth.models import User


# Create your views here.
@login_required(login_url='/auth/login')
def getinfo(request):
    list = User.objects.exclude(id=request.user.id).select_related()
    print(list.query)
    print(f"list: {list}")
    for a in list:
        print(f"user {a.first_name}")
    # isFollow = FollowData.objects.filter(FollowId=request.user.id).all()
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
            FollowData(FollowId=request.user.id, FollowerId=id).save()
            followcount = users_info.objects.filter(userid=request.user.id)
    return getinfo(request)
