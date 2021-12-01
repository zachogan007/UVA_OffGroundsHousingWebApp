import django_filters
from .models import *


# Source: https://www.youtube.com/watch?v=G-Rct7Na0UQ
class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Listing
        fields = '__all__'
        exclude = ['name', 'longitude', 'latitude', 'pub_date', 'image', 'laundry', 'parking', 'fitness']


class ReviewFilter(django_filters.FilterSet):
    class Meta:
        model = Review
        fields = '__all__'
        exclude = ['pub_date', 'review_text']
