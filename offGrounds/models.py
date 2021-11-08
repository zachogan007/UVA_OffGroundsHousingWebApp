from django.db import models


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


class Housing(models.Model):
    property_name = models.TextField(max_length=2000)
    address = models.TextField(default="", max_length=2000)
    bed = models.BigIntegerField(default=0)
    bath = models.DecimalField(default=0, decimal_places=1, max_digits=2)
    area = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    description = models.TextField(default="", max_length=2000)

    def get_property_name(self):
        return self.property_name

    def get_address(self):
        return self.address

    def get_bed(self):
        return "Beds: " + self.bed

    def get_bath(self):
        return "Baths: " + self.bath

    def get_area(self):
        return self.area + " sq ft"

    def get_description(self):
        return self.description

    def __str__(self):
        return self.get_property_name()
