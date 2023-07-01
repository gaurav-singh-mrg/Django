import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "App.settings")
import django

django.setup()
from faker import factory, Faker
from django.contrib.auth.models import User
from model_bakery.recipe import Recipe

myfake = Faker()
for k in range(10000):
    user = Recipe(User,
                  username=myfake.user_name(),
                  email=myfake.email(),
                  password='Test123!',
                  first_name=myfake.first_name(),
                  last_name=myfake.last_name())
    user.make()
