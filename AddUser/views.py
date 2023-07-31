from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from .models import users_info, FollowData
from django.contrib.auth.models import User
from django.db.models import Case, When, Value, F
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage  # adding pagination support
from django.views.generic.list import ListView
from django.urls import reverse


class UserDetailView(DetailView):
    model = User
    template_name = 'AddUser/UserDetailView.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'userinfo'

    # def get_queryset(self, *args, **kwargs):
    #     print(*args, **kwargs)
    #     return 404
    #     # return User.objects.filter(id=self.args['pk'])


# todo: fix method decorator login required
# @method_decorator(login_required, name="dispatch")
class GetInfo(ListView):
    # model = 'FollowData'
    template_name = 'AddUser/UserInfo.html'
    context_object_name = 'list'
    paginate_by = 12

    def get_queryset(self):
        a = FollowData.objects.filter(UserId=self.request.user.id, Active=True).values('FollowersId')
        query_set = User.objects.annotate(
            IsFollower=Case(
                When(id__in=[a], then=Value(True)),
                default=Value(False), )).exclude(id=self.request.user.id).order_by('first_name').values('id',
                                                                                                        'username',
                                                                                                        'first_name',
                                                                                                        'last_name',
                                                                                                        'IsFollower')
        return query_set

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        page = context['page_obj']
        context['paginator_range'] = page.paginator.get_elided_page_range(page.number)
        return context


@login_required(login_url='/auth/login')
def followbtn(request, id):
    # check for valid request id
    if request.user.id == id:
        print("Same user can't follow itself")
    isUserIDExist = User.objects.filter(id=id).count()
    isUserExist = User.objects.filter(id=request.user.id).values('id')
    print(f'isUserExist => {isUserExist.query.__str__()}')
    if isUserIDExist == 1:
        '''going to update follower count'''
        try:
            data = FollowData.objects.get(UserId=request.user.id, FollowersId=id)
            print(f'Active Inactive followers {data.Active}')
            data.Active = not data.Active
            data.save()
            '''Update the Active to True or false. which shows weather user is following or unfollowed'''
        except FollowData.DoesNotExist:
            print(f"Saving follow data {request.user.id} , {id}")
            c = FollowData(Active=True, UserId=request.user.id, FollowersId=id)
            c.save()
        '''Going to update entry in user_info table'''
        # user, isCreated = users_info.objects.get_or_create(Userid=isUserExist[0:1])
        # # a = user.update(FollowerCount=F('FollowerCount') + 1)
        # print(f'a => {a.query.__str__()}')
    else:
        print("Wrong User ID Provided")
    return redirect('adduser:info')
