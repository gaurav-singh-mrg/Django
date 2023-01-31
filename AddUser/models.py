from django.db import models
from django.utils.timezone import now

import Auth.models
from Auth import models


# Create your models here.

class users(models.Model):
    userid = models.ForeignKey(Auth.models.GetUser, related_name='UserID', on_delete=models.CASCADE)
    CreatedDate = models.DateTimeField(auto_now_add=True, editable=False)
    UpdatedDate = models.DateTimeField(auto_now=True)  # changes value on update every
    FirstName = models.CharField(max_length=255, default='FirstName', Null=False)
    LastName = models.CharField(max_length=255, default='LastName', Null=True)
    Country = models.CharField(max_length=255, Null=True)
    Follower = models.models.IntegerField(default=0)
    Following = models.models.IntegerField(default=0)


class FollowData(models.Model):
    FollowerId = models.ForeignKey(Auth.models.GetUser, related_name='FollowerId', on_delete=models.CASCADE)
    FollowingID = models.ForeingKey(Auth.models.GetUser, related_name='FollowingId', on_delete=models.CASCADE)
    CreatedDate = models.DateTimeField(auto_now_add=True, editable=False)
    UpdatedDate = models.DateTimeField(auto_now=True)  # changes value on update every
