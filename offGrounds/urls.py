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
    path('logout/', views.logout_view, name="logout_index"),
    path('login/', TemplateView.as_view(template_name="login/index.html")),
    path('homesearch/', views.search_view, name="search"),
    path('homesearch/listing/<int:pk>', views.ListingView.as_view(), name="listing"),
    #path('homesearch/listing/<int:listing_id', views.write_review, name="listing_review"),
    path('userprofile/', views.user_view, name="userprofile"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
