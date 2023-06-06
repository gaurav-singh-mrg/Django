from django.contrib import admin
from .models import FollowData, users_info

# Register your models here.

admin.site.register(users_info)
# admin.site.register(FollowingData)
admin.site.register(FollowData)
