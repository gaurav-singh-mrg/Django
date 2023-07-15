from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class users_info(models.Model):
    # CreatedDate = models.DateTimeField(auto_now_add=True, editable=False)

    Userid = models.ForeignKey(User, on_delete=models.CASCADE)
    UpdatedDate = models.DateTimeField(auto_now=True)  # changes value on update every
    Country = models.CharField(max_length=255, null=True)
    State = models.CharField(max_length=255, null=True)
    Phone = models.CharField('ContactPhone', null=True, max_length=20)
    DateOfBirth = models.DateTimeField('DOB', null=True)
    ProfilePic = models.ImageField(upload_to="ProfilePic", default=None, null=True)
    FollowerCount = models.IntegerField(default=0)
    FollowingCount = models.IntegerField(default=0)
    Active = models.BooleanField(default=True)
    PrivateAccount = models.BooleanField(default=False)

    # default ordering
    class META:
        ordering = '-Userid'
    # def __str__(self):
    #     return self.userid


class FollowData(models.Model):
    UserId = models.IntegerField(default=0, db_index=True)  # added db index
    FollowersId = models.IntegerField(default=0)
    Active = models.BooleanField(default=True, null=False)
    CreatedDate = models.DateTimeField(auto_now_add=True, editable=False)
    UpdatedDate = models.DateTimeField(auto_now=True)  # changes value on update every

    # class Meta:
    #     verbose_name_plural = 'FollowDatas'
    # def __str__(self):
    #     return self.id
    # class Meta:
    #     db_table = "profile"
