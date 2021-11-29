from django.shortcuts import render, get_object_or_404, redirect

from django.http import HttpResponse, Http404
from django.contrib.auth import logout
from django.views import generic
from .models import Listing, Review  # , Pin
from django.utils import timezone
from .filters import OrderFilter
from .forms import ReviewForm

from .models import Listing  # , Pin
from django.utils import timezone
from .filters import OrderFilter
from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout
from django.urls import reverse
from django.views import generic
from .models import Listing  # , Pin
from django.utils import timezone
from .filters import OrderFilter

from datetime import datetime, timedelta, date
from django.utils.safestring import mark_safe

from .models import *
from .calendar import Calendar
import calendar


def index(request):
    return HttpResponse("Hello, world. You're at the UVA off grounds housing index.")


def show_user(request, name):
    return HttpResponse("You are looking at this user: " % name)


def show_review(request, review_text):
    return HttpResponse("You are looking at this review: " % review_text)


def default_map(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.my_mapbox_access_token'
    listings = Listing.objects.all()
    return render(request, 'maps/default.html',
                  {'mapbox_access_token': mapbox_access_token, 'all_listings': listings})


def logout_view(request):
    logout(request)
    return render(request, 'logout/logout_index.html')


def search_view(request):
    listings = Listing.objects.all()
    # beds = Listing.objects.get(id=num_beds)
    # baths = Listing.objects.get(id=num_baths)

    myFilter = OrderFilter(request.GET, queryset=listings)
    listings = myFilter.qs

    # beds = Listing.objects.get(id=num_beds)
    # baths = Listing.objects.get(id=num_baths)

    myFilter = OrderFilter(request.GET, queryset=listings)
    listings = myFilter.qs

    # beds = Listing.objects.get(id=num_beds)
    # baths = Listing.objects.get(id=num_baths)

    myFilter = OrderFilter(request.GET, queryset=listings)
    listings = myFilter.qs

    context = {'listings': listings, 'myFilter': myFilter}
    return render(request, 'homesearch/search.html',
                  {'all_listings': listings, 'myFilter': myFilter})


# def listing_view(request):
# make context
#     return render(request, 'homesearch/listing.html', context)


class ListingView(generic.DetailView):
    model = Listing
    template_name = 'homesearch/listing.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Listing.objects.filter(pub_date__lte=timezone.now())



def write_review(request, listing_id):
    # listing = Listing.objects.filter(pub_date__lte=timezone.now())
    # listing.save()
    review = Review.objects.create(review_text="", rating=1, listing=None)
    url = "homesearch/listing/" + listing_id +"/review"

    try:
        listing = Listing.objects.get(pk=listing_id)
    except Listing.DoesNotExist:
        raise Http404("listing does not exist")
    if request.method == 'POST':
        rating = request.POST.get('rating', 3)
        review_text = request.POST.get('review_content', '')
        form = ReviewForm(request.POST)
        form.save()
        review = Review.objects.create(review_text=review_text, rating=rating, listing=listing)
        print(listing_id)
        print(url)
        return redirect("homesearch/listing/1/review")
    else:
        form = ReviewForm()

    return render(request, 'homesearch/review.html', {'review': review})



class ReviewListView(generic.ListView):
    model = Review
    template_name = 'review/review_list.html'
    context_object_name = 'reviews'

    def get_queryset(self):
        return Review.objects.all()


def review_list(request):
    reviews = Review.objects.all()
    context = {
        'reviews': reviews
    }
    return render(request, 'review/review_list.html', context)


def user_view(request):
    return render(request, 'userprofile/profile_index.html')


class CalendarView(generic.ListView):
    model = Event
    template_name = 'calendar/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return datetime.date(year, month, day=1)
    return datetime.date.today()


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month
