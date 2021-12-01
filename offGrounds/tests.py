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
    