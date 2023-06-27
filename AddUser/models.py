from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class users_info(models.Model):
    # CreatedDate = models.DateTimeField(auto_now_add=True, editable=False)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    UpdatedDate = models.DateTimeField(auto_now=True)  # changes value on update every
    # FirstName = models.CharField(max_length=255, default='FirstName', null=False)
    # LastName = models.CharField(max_length=255, default='LastName', null=True)
    Country = models.CharField(max_length=255, null=True)
    Phone = models.CharField('Contact Phone', null=True, max_length=20)
    # Email = models.EmailField('Email')
    FollowerCount = models.IntegerField(default=0)
    FollowingCount = models.IntegerField(default=0)

    # def __str__(self):
    #     return self.userid


''' We can find total number of followers by counting 
select count followerid from followdata where userid = 1
and we can find total number of following by count 
seelct count userid from followdata where followerid = 1 '''


class FollowData(models.Model):
    FollowId = models.IntegerField(default=1, blank=True)
    FollowerId = models.IntegerField(blank=True, default=1)
    FollowsID = models.ManyToManyField(User, related_name='Follows')
    FollowersId = models.ManyToManyField(User, related_name='Followers')
    # Active = models.BooleanField(default=True, null=False)
    CreatedDate = models.DateTimeField(auto_now_add=True, editable=False)
    UpdatedDate = models.DateTimeField(auto_now=True)  # changes value on update every

    # def __str__(self):
    #     return self.id

# class FollowingData(models.Model):
#     UserId = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
#     FollowingID = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
#     Active = models.BooleanField(default=True, null=False)
#     CreatedDate = models.DateTimeField(auto_now_add=True, editable=False)
#     UpdatedDate = models.DateTimeField(auto_now=True)  # changes value on update every
#
#     # def __str__(self):
#     #     return self.FollowingID
