from django.contrib import admin
from .models import (
    Flights,
    Hotels,
)

# Register your models here.
admin.site.register(Flights)
admin.site.register(Hotels)
