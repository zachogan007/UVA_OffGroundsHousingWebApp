from django.contrib import admin
from django.urls import include, path

from django.views.generic import TemplateView
from . import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', TemplateView.as_view(template_name="login/index.html")),
    path('accounts/', include('allauth.urls')),
    path('maps/', views.default_map, name="default"),
    path('direction/', views.direction_map, name="direction_map"),
    path('logout/', views.logout_view, name="logout_index"),
    path('login/', TemplateView.as_view(template_name="login/index.html")),
    path('homesearch/', views.search_view, name="search"),
    path('homesearch/listing/<int:pk>', views.ListingView.as_view(), name="listing"),
    path('calendar/', views.CalendarView.as_view(), name='calendar'),
    path('reviews/', views.review_search, name='review'),
    path('profile/', views.profile, name='users-profile'),
    path('view_profile/', views.view_profile, name='view-profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


