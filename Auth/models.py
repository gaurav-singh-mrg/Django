from django.db import models
from django.utils.timezone import now


# Create your models here.
class GetUser(models.Model):
    class Meta:
        verbose_name_plural = 'getuser'
        # override default name of table (GetUser)     and set the table name as getuser
        ordering = ('-CreatedDate',)
        # return table results in order by created date desc

    def __str__(self):
        return self.name

    # return the table name

    # no need to set primary key an ID field will be created autom
    Email = models.EmailField(max_length=50, unique=True, db_index=True)
    Password = models.CharField(max_length=50)
    CreatedDate = models.DateTimeField(auto_now_add=True, editable=False)  # only populated once
    UpdatedDate = models.DateTimeField(auto_now=True)  # changes value on update every time
    ExtraPermission = models.BooleanField(default=False, editable=False)
