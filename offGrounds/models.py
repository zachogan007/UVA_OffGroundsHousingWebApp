from django.db import models


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

# class Maps(models.Model):
# address = map_fields.AddressField(max_length = 200)
# geo_location = map_fields.GeoLocationField(max_length=100)
