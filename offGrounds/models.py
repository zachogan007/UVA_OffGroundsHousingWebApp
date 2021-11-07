from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Review(models.Model):
    review_text = models.TextField(max_length=20000)
    pub_date = models.DateField('date published')

    def __str__(self):
        return self.review_text


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
    pub_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name

