from django.db import models
from datetime import date
from django.utils import timezone
from django.conf import settings

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
    year = models.TextField(default="")
    phone_number = models.CharField(max_length=12, default="000-000-0000")
    instagram = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.name

    def set_password(self, pwd):
        self.password = pwd
        self.is_logged_in = True

    def logout(self):
        self.password = ""
        self.is_logged_in = False

class UserModel(models.Model):
    user_key = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.TextField(max_length=2000)
    password = models.TextField(max_length=2000, default="")
    is_logged_in = False
    year = models.TextField(default="N/A")
    phone_number = models.CharField(max_length=12, default="000-000-0000")
    instagram = models.CharField(max_length=200, default="N/A")

class UserInfo(models.Model):
    user_key = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    year = models.TextField(default="N/A")
    phone_number = models.CharField(max_length=12, default="000-000-0000")
    instagram = models.CharField(max_length=200, default="N/A")


class Listing(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    num_beds = models.IntegerField(default=0)
    num_baths = models.FloatField(default=0.0)
    rent = models.FloatField(default=0.0)
    size = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    latitude = models.FloatField(default=0.0)
    pub_date = models.DateTimeField(default=date.today)
    image = models.ImageField(upload_to='images')
    laundry = models.CharField(max_length=200, default="", blank=True)
    parking = models.CharField(max_length=200, default="", blank=True)
    fitness = models.CharField(max_length=200, default="", blank=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.name