import django_filters
from .models import *

class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Listing
        fields = '__all__'
        exclude = ['name', 'longitude', 'latitude', 'pub_date']
