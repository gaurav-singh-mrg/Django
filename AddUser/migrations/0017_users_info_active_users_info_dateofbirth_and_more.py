# Generated by Django 4.1.3 on 2023-07-11 02:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('AddUser', '0016_alter_followdata_followersid_alter_followdata_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='users_info',
            name='Active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='users_info',
            name='DateOfBirth',
            field=models.DateTimeField(null=True, verbose_name='DOB'),
        ),
        migrations.AddField(
            model_name='users_info',
            name='ProfilePic',
            field=models.ImageField(default=None, null=True, upload_to='media/ProfilePic'),
        ),
        migrations.AddField(
            model_name='users_info',
            name='State',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='users_info',
            name='Phone',
            field=models.CharField(max_length=20, null=True, verbose_name='ContactPhone'),
        ),
    ]
