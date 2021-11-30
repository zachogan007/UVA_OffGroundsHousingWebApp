from django.shortcuts import render, get_object_or_404, redirect

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout
from django.urls import reverse, reverse_lazy
from django.views import generic
from .models import Listing
from django.utils import timezone
from .filters import OrderFilter

from datetime import datetime, timedelta, date
from django.utils.safestring import mark_safe
from .forms import AccountForm

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

def account_view(request):
    user = UserInfo.objects.filter(user_key=request.user)
    context = {'user_info': user}
    return render(request, 'account/profile.html', context)
    # if request.method == "POST":
    #     form = AccountForm(request.POST)
    #     if form.is_valid():
    #         new_user_info = form.save(commit=False)
    #         new_user_info.user_key = request.user
    #         new_user_info.year = request.POST['year']
    #         new_user_info.phone_number = request.POST['phone_number']
    #         new_user_info.instagram = request.POST['instagram']
    #         new_user_info.save()
    #         return HttpResponseRedirect('account/manage_account.html')
    #     else:
    #         form = AccountForm
    #     # new_user = User()
    #     # new_user.username = request.POST.get("user_username", None)
    #     # new_user.first_name = request.POST.get("user_first_name", None)
    #     # new_user.last_name = request.POST.get("user_last_name", None)
    #     # User.save(new_user)
    # return render(request, 'account/manage_account.html', {'form':form, 'UserModel': UserModel.objects.filter(user_key=request.user)})

class EditProfileView(generic.UpdateView):
    model = UserInfo
    template_name = 'account/manage_account.html'
    fields = ['year', 'phone_number', 'instagram']
    success_url = reverse_lazy('profile')
    # def edit_profile(self, request):
        # if request.method == "POST":
        #     form = AccountForm(request.POST, instance=request.user)
        #     if form.is_valid():
        #         form.save()
        #         # new_user_info.user_key = request.user
        #         # new_user_info.year = request.POST['year']
        #         # new_user_info.phone_number = request.POST['phone_number']
        #         # new_user_info.instagram = request.POST['instagram']
        #         # new_user_info.save()
        #         return HttpResponseRedirect('/manage_account')
        #     else:
        #         form = AccountForm(instance=request.user)
        #     return render(request, 'account/manage_account.html', {'form': form})
        # return render(request, 'account/manage_account.html')
            # new_user = User()
            # new_user.username = request.POST.get("user_username", None)
            # new_user.first_name = request.POST.get("user_first_name", None)
            # new_user.last_name = request.POST.get("user_last_name", None)
            # User.save(new_user)

        # user = UserInfo.objects.filter(user_key=request.user)
        # if request.method == "POST":
        #     if not user:
        #         u = UserInfo()
        #         u.user_key = request.user
        #         u.year = request.POST.get("year", None)
        #         u.phone_number = request.POST.get("phone_number", None)
        #         u.instagram = request.POST.get("instagram", None)
        #         u.save()
        #         return HttpResponseRedirect('/profile')
        #     else:
        #         print("ERERE")
        #         year = request.POST.get("year", None)
        #         phone_number = request.POST.get("phone_number", None)
        #         instagram = request.POST.get("instagram", None)
        #         user.update(year=year, phone_number=phone_number, instagram=instagram)
        #         user.save()
        #         return HttpResponseRedirect('/profile')
        # return render(request, 'account/manage_account.html')
