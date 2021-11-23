from django.db import models
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

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.name

class Review(models.Model):
    review_text = models.TextField(max_length=20000)
    pub_date = models.DateField('date published')
    rating = models.IntegerField(default=0, validators = [MaxValueValidator(5), MinValueValidator(0)])
    place = models.TextField(default="",max_length=20000)

    def __str__(self):
        return self.review_text