import django.db.models
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class imageUploaded(models.Model):
    userID = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    imageField = models.ImageField()
    caption = models.TextField(default='No Caption')
    likesCount = models.IntegerField(default=0)
    Active = models.BooleanField(default=True, null=False)
    CreatedDate = models.DateTimeField(auto_now_add=True, editable=False)
    UpdatedDate = models.DateTimeField(auto_now=True)

# todo : Need to implement a table for like count by users
# todo: Need to implement a table for comment on user pic
