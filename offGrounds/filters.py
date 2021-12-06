import django_filters
from .models import *
from django_filters import CharFilter, NumberFilter, NumericRangeFilter


# Source: https://www.youtube.com/watch?v=G-Rct7Na0UQ
class OrderFilter(django_filters.FilterSet):
    address = CharFilter(field_name='address', lookup_expr='icontains')
    rent = NumberFilter(field_name='rent', lookup_expr='lte')
    size = NumberFilter(field_name='size', lookup_expr='gte')
    class Meta:
        model = Listing
        fields = '__all__'
        exclude = ['name', 'longitude', 'latitude', 'pub_date', 'image', 'laundry', 'parking', 'fitness']


class ReviewFilter(django_filters.FilterSet):
    content = CharFilter(field_name='content', lookup_expr='icontains')
    class Meta:
        model = Review
        fields = '__all__'
        exclude = ['pub_date', 'review_text']
