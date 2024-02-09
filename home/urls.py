from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

app_name = "app"

urlpatterns = [
    path("", views.home),
    path("hotel_s/", views.HotelView),
    path("flights_s/", views.FlightView),
    path('hotel',views.hotel),
]
