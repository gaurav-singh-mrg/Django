# Generated by Django 4.1.3 on 2023-06-29 03:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('AddUser', '0010_followdata_followsid_users_info_followersid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='followdata',
            name='FollowId',
        ),
        migrations.RemoveField(
            model_name='followdata',
            name='FollowerId',
        ),
        migrations.RemoveField(
            model_name='users_info',
            name='FollowersId',
        ),
        migrations.AddField(
            model_name='followdata',
            name='Active',
            field=models.BooleanField(default=True),
        ),
    ]
