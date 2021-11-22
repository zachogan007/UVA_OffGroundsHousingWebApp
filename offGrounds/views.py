from django.shortcuts import render, get_object_or_404, redirect

from django.http import HttpResponse, Http404
from django.contrib.auth import logout
from django.views import generic

from django.utils import timezone
from .filters import OrderFilter
from .models import *
from .calendar import Calendar
import calendar
from .models import Listing  # , Pin
from django.utils import timezone
from .filters import OrderFilter


def index(request):
    return HttpResponse("Hello, world. You're at the UVA off grounds housing index.")

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
        return Listing.objects.filter(pub_date__lte=timezone.now)


def ReviewView(request):
    review = Review.objects.all()
    context = {
        'review': review,
    }
    return render(request, 'review/review_list.html', context)

#class ReviewView(generic.DetailView):
 #  model = Review
  #template_name = 'review/review_list.html'

   # def get_queryset(self):

    #    return Review.objects.filter(pub_date__lte=timezone.now)

    #latest_review_list = Review.objects.all()
    #context={
     #   'latest_review_list': latest_review_list,
    #}
    #return render(request, 'review/review_list.html', context)
    #model = Review
    #template_name = 'review/review_list.html'


    #def get_queryset(self):
     #   return Review.objects.filter(pub_date_lte=timezone.now())

    #def write_review(request):
        #review = Review.objects.create(review_text="", rating=1)
        #if request.method == "POST":
            #rating = request.POST.get('rating', 3)
            #review_text = request.POST.get('review_content', '')
           # form = ReviewForm(request.POST)
          #  form.save()
         #   review = Review.objects.create(review_text=review_text, rating=rating)
        #    return redirect('reviews/')
       # return render(request, 'review/review_list.html', {'review': review})

def user_view(request):
    return render(request, 'userprofile/profile_index.html')