# Generated by Django 4.1.3 on 2023-07-14 03:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('AddUser', '0020_alter_users_info_profilepic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users_info',
            name='ProfilePic',
            field=models.ImageField(default=None, null=True, upload_to=''),
        ),
    ]
