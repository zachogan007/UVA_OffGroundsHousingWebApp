from django.contrib import admin
from django.urls import include, path

from django.views.generic import TemplateView
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', TemplateView.as_view(template_name="login/index.html")),
    path('accounts/', include('allauth.urls')),
    path('maps/', views.default_map, name="default"),
    path('logout/', views.logout_view, name="logout_index"),
]
