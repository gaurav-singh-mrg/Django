from django.db import models


# Create your models here.

class users(models.Model):
    userid = models.IntegerField(default=0, null=False)
    CreatedDate = models.DateTimeField(auto_now_add=True, editable=False)
    UpdatedDate = models.DateTimeField(auto_now=True)  # changes value on update every
    FirstName = models.CharField(max_length=255, default='FirstName', null=False)
    LastName = models.CharField(max_length=255, default='LastName', null=True)
    Country = models.CharField(max_length=255, null=True)
    Phone = models.CharField('Contact Phone', null=True, max_length=20)
    Email = models.EmailField('Email')
    Follower = models.IntegerField(default=0)
    Following = models.IntegerField(default=0)

    def __str__(self):
        return self.FirstName


class FollowData(models.Model):
    # FollowerId = models.IntegerField(default=0, null=False)
    FollowerId = models.ForeignKey(users, blank=True, on_delete=models.CASCADE)
    Active = models.BooleanField(default=True, null=False)
    CreatedDate = models.DateTimeField(auto_now_add=True, editable=False)
    UpdatedDate = models.DateTimeField(auto_now=True)  # changes value on update every

    def __str__(self):
        return self.FollowerId


class FollowingData(models.Model):
    FollowingID = models.ForeignKey(users, blank=True, on_delete=models.CASCADE)
    Active = models.BooleanField(default=True, null=False)
    CreatedDate = models.DateTimeField(auto_now_add=True, editable=False)
    UpdatedDate = models.DateTimeField(auto_now=True)  # changes value on update every

    def __str__(self):
        return self.FollowingID
