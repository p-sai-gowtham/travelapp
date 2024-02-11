from django.contrib import admin
from .models import (
    Flights,
    Hotels,
    BookFlight,
    BookHotel,
)

# Register your models here.
admin.site.register(Flights)
admin.site.register(Hotels)
admin.site.register(BookFlight)
admin.site.register(BookHotel)
