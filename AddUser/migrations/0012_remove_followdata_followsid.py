# Generated by Django 4.1.3 on 2023-06-29 03:37

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('AddUser', '0011_remove_followdata_followid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='followdata',
            name='FollowsId',
        ),
    ]
