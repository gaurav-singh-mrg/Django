# Generated by Django 4.1.3 on 2023-07-07 02:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='imageUploaded',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imageField', models.ImageField(upload_to='')),
                ('caption', models.TextField(default='No Caption')),
                ('likesCount', models.IntegerField(default=0)),
                ('Active', models.BooleanField(default=True)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('UpdatedDate', models.DateTimeField(auto_now=True)),
                ('userID',
                 models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
