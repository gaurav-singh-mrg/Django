# Generated by Django 4.1.3 on 2023-06-27 02:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AddUser', '0007_remove_followdata_followid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='followdata',
            name='FollowersId',
            field=models.ManyToManyField(related_name='Followers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='followdata',
            name='FollowsID',
            field=models.ManyToManyField(related_name='Follows', to=settings.AUTH_USER_MODEL),
        ),
    ]