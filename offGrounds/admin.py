from django.contrib import admin
from .models import Listing
# Register your models here.
from .models import Event

from .models import *


class ListingAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
    ]

admin.site.register(Listing)



#class CalendarAdmin(admin.ModelAdmin):
    #fieldsets = [
     #   (None, {'fields': ['name']}),
    #]

admin.site.register(Event)
admin.site.register(UserInfo)

