# Generated by Django 4.1.3 on 2023-04-08 07:29

import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ('AddUser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='followdata',
            name='CreatedDate',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='followdata',
            name='UpdatedDate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='followdata',
            name='FollowId',
            field=models.IntegerField(blank=True, default=1, verbose_name=django.contrib.auth.models.User),
        ),
        migrations.AlterField(
            model_name='followdata',
            name='FollowerId',
            field=models.IntegerField(blank=True, default=1, verbose_name=django.contrib.auth.models.User),
        ),
    ]
