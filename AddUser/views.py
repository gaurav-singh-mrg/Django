from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import users_info, FollowData
from django.contrib.auth.models import User
from django.db.models import Case, When, Value
from django.core.paginator import Paginator  # adding pagination support

# Create your views here.
@login_required(login_url='/auth/login')
def getinfo(request):
    a = FollowData.objects.filter(UserId=request.user.id, Active=True).values('FollowersId')
    list = User.objects.annotate(
        IsFollower=Case(
            When(id__in=[a], then=Value(True)),
            default=Value(False), )).exclude(id=request.user.id).values('id', 'username',
                                                                        'first_name',
                                                                        'last_name',
                                                                        'IsFollower')
    p = Paginator(list, 10)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)

    # print(f'C => {list.query.__str__()}')
    return render(request, 'AddUser/UserInfo.html', locals())


@login_required(login_url='/auth/login')
def followbtn(request, id):
    # check for valid request id
    if request.user.id == id:
        print("Same user can't fallow itself")
    isUserIDExist = User.objects.filter(id=id).count()
    isUserExist = User.objects.filter(id=request.user.id)
    if isUserIDExist == 1:
        '''going to update follower count'''
        try:
            data = FollowData.objects.get(UserId=request.user.id, FollowersId=id)
            print(f'Active Inactive followers {data.Active}')
            data.Active = not data.Active
            data.save()
            '''Update the Active to True or false. which shows wether user is following or unfollowed'''
        except FollowData.DoesNotExist:
            print(f"Saving follow data {request.user.id} , {id}")
            c = FollowData(Active=True, UserId=request.user.id, FollowersId=id)
            c.save()
            return getinfo(request)
    else:
        print("Wrong User ID Provided")
    return getinfo(request)
