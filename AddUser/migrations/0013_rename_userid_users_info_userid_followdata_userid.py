# Generated by Django 4.2.1 on 2023-06-29 06:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AddUser', '0012_remove_followdata_followsid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users_info',
            old_name='userid',
            new_name='Userid',
        ),
        migrations.AddField(
            model_name='followdata',
            name='UserId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE,
                                    to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
