from django.contrib import admin

from main.models import Service, Specialist, Booking

# Register your models here.
admin.site.register(Service)
admin.site.register(Specialist)
admin.site.register(Booking)