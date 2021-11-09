from django.shortcuts import render, get_object_or_404, redirect

from django.http import HttpResponse
from django.contrib.auth import logout
from django.views import generic
from .models import Listing, Review  # , Pin
from django.utils import timezone
from .filters import OrderFilter
from .forms import ReviewForm

from .models import Listing  # , Pin
from django.utils import timezone
from .filters import OrderFilter

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


def write_review(request):
    listing = Listing.objects.filter(pub_date__lte=timezone.now())
    #listing.save()
    form = ReviewForm()

    if request.method == 'POST' and request.user.is_authenticated:
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        rating = request.POST.get('rating', 3)
        review_text = request.POST.get('review_text', '')
        #review = Review.objects.create(listing=listing, user=request.user, rating=rating, review_text=review_text)
        return redirect('listing_details')
    return render(request, 'homesearch/listing.html', {"form": form})

def user_view(request):
    return render(request, 'userprofile/profile_index.html')

