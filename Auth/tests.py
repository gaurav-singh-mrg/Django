from django.test import TestCase
from model_bakery import baker
from django.contrib.auth.models import User


# Create your tests here.

class CustomerTestModel(TestCase):
    """
    Class to test the model Customer
    """

    def setUp(self):
        self.customer = baker.make(User)
