from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
@login_required(login_url='/auth/login')
def browse(request):
    a = FollowData.objects.filter(UserId=request.user.id, Active=True).values('FollowersId')
    list = User.objects.annotate(
        IsFollower=Case(
            When(id__in=[a], then=Value(True)),
            default=Value(False), )).exclude(id=request.user.id).order_by('first_name').values('id', 'username',
                                                                                               'first_name',
                                                                                               'last_name',
                                                                                               'IsFollower')
    p = Paginator(list, 12)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    totalPages = page_obj.paginator.num_pages  # shows the total number of pages
    print(f'totalPages => {totalPages}')
    pageIter = [a + 1 for a in range(totalPages)]
    print(f'pageIter => {pageIter}')
    elidedPageRange = p.get_elided_page_range(number=page_number, on_each_side=2)
    # print(f'C => {list.query.__str__()}')
    return render(request, 'AddUser/UserInfo.html', locals())
