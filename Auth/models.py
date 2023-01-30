from django.db import models
from django.utils.timezone import now


# Create your models here.
class GetUser(models.Model):
    # no need to set primary key an ID field will be created auto
    Email = models.EmailField(max_length=50, unique=True, db_index=True)
    Password = models.CharField(max_length=50)
    CreatedDate = models.DateTimeField(default=now, editable=False)
    ExtraPermission = models.BooleanField(default=False, editable=False)
