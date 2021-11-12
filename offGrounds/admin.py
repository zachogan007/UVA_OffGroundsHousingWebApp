from django.contrib import admin
from .models import Listing #, Pin
# Register your models here.
from .models import Event

from .models import *


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



#class CalendarAdmin(admin.ModelAdmin):
    #fieldsets = [
     #   (None, {'fields': ['name']}),
    #]

admin.site.register(Event)


