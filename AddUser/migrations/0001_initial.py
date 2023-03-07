# Generated by Django 4.1.3 on 2023-03-07 03:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField(default=0)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('UpdatedDate', models.DateTimeField(auto_now=True)),
                ('FirstName', models.CharField(default='FirstName', max_length=255)),
                ('LastName', models.CharField(default='LastName', max_length=255, null=True)),
                ('Country', models.CharField(max_length=255, null=True)),
                ('Phone', models.CharField(max_length=20, null=True, verbose_name='Contact Phone')),
                ('Email', models.EmailField(max_length=254, verbose_name='Email')),
                ('Follower', models.IntegerField(default=0)),
                ('Following', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='FollowingData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Active', models.BooleanField(default=True)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('UpdatedDate', models.DateTimeField(auto_now=True)),
                ('FollowingID',
                 models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='AddUser.users')),
            ],
        ),
        migrations.CreateModel(
            name='FollowData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Active', models.BooleanField(default=True)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('UpdatedDate', models.DateTimeField(auto_now=True)),
                ('FollowerId',
                 models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='AddUser.users')),
            ],
        ),
    ]
