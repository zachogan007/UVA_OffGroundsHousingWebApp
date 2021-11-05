from django.contrib import admin
from .models import Pin
# Register your models here.

class PinAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
    ]

admin.site.register(Pin)
