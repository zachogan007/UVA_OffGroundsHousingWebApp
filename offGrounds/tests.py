import datetime

from django.test import TestCase
from .models import User
from .models import Review

from django.http import HttpRequest

from django.urls import resolve


# run this command: py manage.py test


# Create your tests here.
class DummyTests(TestCase):

    def test_first_dummy(self):
        """
        This is a dummy test case
        """
        self.assertIs(True, True)


class UserTestCase(TestCase):

    def setUp(self):
        User.objects.create(name="bob", year="first")

    def test_to_string(self):
        # test the to string method for User
        # expected return value: the user's name (for now, can change later)
        bob = User.objects.get(name="bob")
        self.assertEqual(bob.__str__(), "bob")

class ReviewTestCase(TestCase):

    def setUp(self):
        Review.objects.create(review_text="nice", pub_date=datetime.date.today())

    def test_to_string(self):
        # test the to string method for User
        # expected return value: the user's name (for now, can change later)
        review1 = Review.objects.get(review_text="nice")
        self.assertEqual(review1.__str__(), "nice")

class LoginTestCase(TestCase):
    def test_login(self):
        pass

# URGENT TO DO - figure out how to test google login!!!

# testing ideas/approaches for urls: query against the website --> for example: do something like ..,url/list
