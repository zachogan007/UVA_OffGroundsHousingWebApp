from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
   # path('user/', views.show_user(), name='show_user'),
   # path('review/', views.show_review(), name='show_review'),
]