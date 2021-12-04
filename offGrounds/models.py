from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
from django.utils import timezone


# Create your models here.
class User(models.Model):
    name = models.TextField(max_length=2000)
    password = models.TextField(max_length=2000, default="")
    is_logged_in = False

    def __str__(self):
        return self.name

    def set_password(self, pwd):
        self.password = pwd
        self.is_logged_in = True

    def logout(self):
        self.password = ""
        self.is_logged_in = False


# class Pin(models.Model):
#     name = models.CharField(max_length=200)
#     longitude = models.FloatField(default=0.0)
#     latitude = models.FloatField(default=0.0)
#
#     def __str__(self):
#         return self.name

class Listing(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    num_beds = models.IntegerField(default=0)
    num_baths = models.FloatField(default=0.0)
    rent = models.FloatField(default=0.0)
    size = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    latitude = models.FloatField(default=0.0)
    pub_date = models.DateTimeField(default=0.0)
    image = models.ImageField(upload_to='images')
    laundry = models.CharField(max_length=200, default="", blank=True)
    parking = models.CharField(max_length=200, default="", blank=True)
    fitness = models.CharField(max_length=200, default="", blank=True)

    # slug = models.SlugField()

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.name


# https://www.programcreek.com/python/example/99929/django.db.models.CASCADE
class Review(models.Model):
    place = models.ForeignKey(Listing, related_name='reviews', on_delete=models.CASCADE, null=True)
    content = models.TextField(blank=True, null=True)
    stars = models.IntegerField()

    def __str__(self):
        return self.content

    def get_stars(self):
        return self.stars

    def get_place(self):
        return self.place.name


# https://dev.to/earthcomfy/django-user-profile-3hik
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    year = models.TextField(default="N/A")
    phone_number = models.CharField(max_length=12, default="000-000-0000")
    instagram = models.CharField(max_length=200, default="N/A")

    def __str__(self):
        return self.user.username
