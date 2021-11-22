from django.contrib import admin

# Register your models here.

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
#admin.site.register(Review)
admin.site.register(User)

admin.site.register(Event)
# admin.site.register(Pin)


