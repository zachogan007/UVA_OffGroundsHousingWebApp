import datetime

"""
import mock
import google.auth.credentials
import google_auth_httplib2
import httplib2
# from googleapiclient import _auth
"""
from django.test import TestCase
# from django.test import Client

from .models import User
from .models import Review

from django.http import HttpRequest
from django.http import HttpResponse
from offGrounds.views import logout_view
from django.contrib.auth import logout, authenticate

from django.urls import resolve


# run this command: py manage.py test


# Create your tests here.

class UserTestCase(TestCase):

    def setUp(self):
        User.objects.create(name="bob")

    def test_to_string(self):
        # test the to string method for User
        # expected return value: the user's name (for now, can change later)
        bob = User.objects.get(name="bob")
        self.assertEqual(bob.__str__(), "bob")


# source: https://github.com/googleapis/google-api-python-client/blob/main/tests/test__auth.py
class GoogleAuthTestCase(TestCase):
    """
    def setUp(self):
        _auth.HAS_GOOGLE_AUTH = True
        _auth.HAS_OAUTH2CLIENT = False
    def test_default_credentials(self):
        with mock.patch("google.auth.default", autospec=True) as default:
            default.return_value = (mock.sentinel.credentials, mock.sentinel.project)
            credentials = _auth.default_credentials()
            self.assertEqual(credentials, mock.sentinel.credentials)
    def test_credentials_from_file(self):
        with mock.patch(
                "google.auth.load_credentials_from_file", autospec=True
        ) as default:
            default.return_value = (mock.sentinel.credentials, mock.sentinel.project)
            credentials = _auth.credentials_from_file("credentials.json")
            self.assertEqual(credentials, mock.sentinel.credentials)
            default.assert_called_once_with(
                "credentials.json", scopes=None, quota_project_id=None
            )
    """

    # User models the user account, needs to call set_password to actually sign in since default password is blank
    def test_login_sim(self):
        # c = Client()
        user = User.objects.create(name="bob@gmail.com")
        user.set_password("new_password")  # logged in should be true here
        user.save()
        login = user.is_logged_in
        self.assertTrue(login)

    def test_logout_sim(self):
        user = User.objects.create(name="bob@gmail.com")
        user.set_password("new_password")  # logged in should be true here
        user.save()
        user.logout()
        user.save()
        logged_out = user.is_logged_in
        self.assertFalse(logged_out)


class ReviewsTestCase(TestCase):
    def setUp(self):
        place1 = Listing.objects.create(name="1800 JPA", address="1800 Jefferson Park Ave.", num_beds=2, num_bath2=1.0)
        place2 = Listing.objects.create(name="1900 JPA", address="1900 Jefferson Park Ave.", num_beds=3, num_bath2=2.0)
        place3 = Listing.objects.create(name="Woodrow", address="102 Stadium Ave", num_beds=4, num_bath2=4.0)
        Review.objects.create(content="nice", stars=3.0, place=place1)
        Review.objects.create(content="no dryer in unit", stars=2.0, place=place2)
        Review.objects.create(content="great location", stars=5.0, place=place3)
        Review.objects.create(content="it's ok", stars=2.0, place=place2)

    def review1_test_to_string(self):
        review1 = Review.objects.get(place=place1)
        self.assertEqual(review1.__str__(), "nice")
        self.assertFalse(review1.__str__(), "wrong one")

    def review1_test_stars(self):
        review1 = Review.objects.get(place=place1)
        self.assertEquals(review1.get_stars(), 2.0)

    def review1_test_place(self):
        review2 = Review.objects.get(place=place2)
        self.assertEquals(review2.get_stars(), 2.0)





