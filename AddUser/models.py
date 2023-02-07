from django.db import models


# Create your models here.

class users(models.Model):
    userid = models.IntegerField(default=0, null=False)
    CreatedDate = models.DateTimeField(auto_now_add=True, editable=False)
    UpdatedDate = models.DateTimeField(auto_now=True)  # changes value on update every
    FirstName = models.CharField(max_length=255, default='FirstName', null=False)
    LastName = models.CharField(max_length=255, default='LastName', null=True)
    Country = models.CharField(max_length=255, null=True)
    Follower = models.IntegerField(default=0)
    Following = models.IntegerField(default=0)


class FollowData(models.Model):
    FollowerId = models.IntegerField(default=0, null=False)
    FollowingID = models.IntegerField(default=0, null=False)
    CreatedDate = models.DateTimeField(auto_now_add=True, editable=False)
    UpdatedDate = models.DateTimeField(auto_now=True)  # changes value on update every
