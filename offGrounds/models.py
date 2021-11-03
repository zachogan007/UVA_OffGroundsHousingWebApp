from django.db import models


class Listing(models.Model):
    listing_name = models.CharField(max_length=200)
    posting_date = models.DateTimeField('date published')
    utilities = models.CharField(max_length=200)
    beds = models.CharField(max_length = 200)
    baths = models.CharField(max_length = 200)
    parking = models.CharField(max_length = 200)


# Create your models here.
class Review(models.Model):
    review_text = models.TextField(max_length=20000)
    pub_date = models.DateField('date published')

    def __str__(self):
        return self.review_text

class User(models.Model):
    name = models.TextField(max_length=2000)
    year = models.CharField(max_length=2000)

    def __str__(self):
        return self.name


