from django.contrib import admin

from .models import Order, Place


admin.site.register(Order)
admin.site.register(Place)