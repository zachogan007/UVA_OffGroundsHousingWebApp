from django.contrib import admin
from .models import Listing #, Pin
# Register your models here.
<<<<<<< HEAD
from .models import *
=======

# class PinAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None, {'fields': ['name']}),
#     ]

class ListingAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
    ]

# admin.site.register(Pin)
admin.site.register(Listing)
>>>>>>> 7fb4991a5f9b0d8190fb94de60a45515e89f5f1f
