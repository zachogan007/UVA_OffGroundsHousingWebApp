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
from .models import Listing

from django.http import HttpRequest
from django.http import HttpResponse
from offGrounds.views import logout_view
from django.contrib.auth import logout, authenticate

from django.urls import resolve
import datetime
import pytz


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
        creationDate = datetime.datetime(2021, 11, 20, 20, 8, 7, 127325, tzinfo=pytz.UTC)
        place1 = Listing.objects.create(name="1800 JPA", address="1800 Jefferson Park Ave.", num_beds=2, num_baths=1.0,
                                        pub_date=creationDate)
        place2 = Listing.objects.create(name="1900 JPA", address="1900 Jefferson Park Ave.", num_beds=3, num_baths=2.0,
                                        pub_date=creationDate)
        place3 = Listing.objects.create(name="Woodrow", address="102 Stadium Ave", num_beds=4, num_baths=4.0,
                                        pub_date=creationDate)
        Review.objects.create(content="nice", stars=3, place=place1)
        Review.objects.create(content="no dryer in unit", stars=2, place=place2)
        Review.objects.create(content="great location", stars=5, place=place3)
        #Review.objects.create(content="it's ok", stars=2, place=place2)

    def test_review1_to_string(self):
        place1 = Listing.objects.get(name="1800 JPA")
        review1 = Review.objects.get(place=place1)
        self.assertEqual(review1.__str__(), "nice")
        self.assertNotEquals(review1.__str__(), "wrong one")

    def test_review1_get_stars(self):
        place1 = Listing.objects.get(name="1800 JPA")
        review1 = Review.objects.get(place=place1)
        self.assertEquals(review1.get_stars(), 3)

    def test_review1_get_place(self):
        place1 = Listing.objects.get(name="1800 JPA")
        review1 = Review.objects.get(place=place1)
        self.assertEquals(review1.get_place(), "1800 JPA")

    def test_review2_to_string(self):
        place2 = Listing.objects.get(name="1900 JPA")
        review2 = Review.objects.get(place=place2)
        self.assertEqual(review2.__str__(), "no dryer in unit")
        self.assertNotEquals(review2.__str__(), "wrong one")

    def test_review2_get_stars(self):
        place2 = Listing.objects.get(name="1900 JPA")
        review2 = Review.objects.get(place=place2)
        self.assertEquals(review2.get_stars(), 2)

    def test_review2_get_place(self):
        place2 = Listing.objects.get(name="1900 JPA")
        review2 = Review.objects.get(place=place2)
        self.assertEquals(review2.get_place(), "1900 JPA")

    def test_review3_to_string(self):
        place3 = Listing.objects.get(name="Woodrow")
        review3 = Review.objects.get(place=place3)
        self.assertEqual(review3.__str__(), "great location")
        self.assertNotEquals(review3.__str__(), "wrong one")

    def test_review3_get_stars(self):
        place3 = Listing.objects.get(name="Woodrow")
        review3 = Review.objects.get(place=place3)
        self.assertEquals(review3.get_stars(), 5)

    def test_review3_get_place(self):
        place3 = Listing.objects.get(name="Woodrow")
        review3 = Review.objects.get(place=place3)
        self.assertEquals(review3.get_place(), "Woodrow")

    """
    def test_login_sim(self):
    self.c = Client()
    self.user = User.objects.create(name="bob@gmail.com",password="12345")
    self.user.set_password("newPassword")
    self.user.save()
    self.user = authenticate(name="bob@gmail.com", password="newPassword")
    login = self.c.login(name="bob@gmail.com", password="newPassword")
    self.assertTrue(login)     

def logout2_test_url(self):
    pass

    def test_logout_url(self):
    request = HttpRequest()
    response = logout(request)
    html = response.content.decode('utf8')
    self.assertTrue(html.startswith('html'))
    #self.assertTemplateUsed(response, 'logout_index.html')
 """


# testing ideas/approaches for urls: query against the website --> for example: do something like ..,url/list
"""
class ListingFilterTestCase(TestCase):
    def setUp(self):
        Listing.objects.create(name="1800 jpa", address="1800 Jefferson Park Ave. Charlottesville, VA 22903", num_baths=3.0, num_beds=3)

    def filter_test_1(self):
        get = {Listing.objects.get(name="1800 jpa").pk}
        listings = Listing.objects.all()
        list_ordered = OrderFilter(get, queryset=listings)
        self.assertTrue(len(list(list_ordered.qs)), 1)
"""
