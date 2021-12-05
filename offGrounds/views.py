from django.shortcuts import render, get_object_or_404, redirect

from .filters import ReviewFilter
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout
from django.urls import reverse
from django.views import generic
from .models import Listing
from django.utils import timezone
from .filters import OrderFilter

from datetime import datetime, timedelta, date
from django.utils.safestring import mark_safe

from .models import *
from .calendar import Calendar
import calendar
from .forms import UpdateUserForm

from django.contrib import messages
from django.contrib.auth.decorators import login_required


def review_search(request):
     places = Listing.objects.all()
    #Source: https://www.youtube.com/watch?v=Y5vvGQyHtpM
     if request.method == 'POST':
         place = request.POST.get('place', )
         stars = request.POST.get('stars', 3)
         content = request.POST.get('content', "")
         user = request.POST.get('user', "")
         temp = Listing.objects.get(name=place)
         review = Review.objects.create(stars=stars, content=content, place=temp, user=user)
         review.save()
     # Source: https://www.youtube.com/watch?v=G-Rct7Na0UQ
     reviews = Review.objects.all()
     rFilter = ReviewFilter(request.GET, queryset=reviews)
     reviews = rFilter.qs
     context = {
          'reviews': reviews, 'rFilter': rFilter, 'places': places
     }
     return render(request, 'review/review_list.html', context)

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

#Source: https://www.youtube.com/watch?v=G-Rct7Na0UQ
def search_view(request):
    listings = Listing.objects.all()

    myFilter = OrderFilter(request.GET, queryset=listings)
    listings = myFilter.qs

    context = {'listings': listings, 'myFilter': myFilter}
    return render(request, 'homesearch/search.html',
                  {'all_listings': listings, 'myFilter': myFilter})



class ListingView(generic.DetailView):
    model = Listing
    template_name = 'homesearch/listing.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Listing.objects.filter(pub_date__lte=timezone.now())


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



@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
           # messages.success(request, 'Your profile is updated successfully')
            return redirect('/view_profile')
    else:
        user_form = UpdateUserForm(instance=request.user)

    return render(request, 'account/profile.html', {'user_form': user_form})

def view_profile(request):
    return render(request, 'account/view_profile.html')
