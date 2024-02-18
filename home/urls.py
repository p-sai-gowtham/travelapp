from . import views
from django.urls import path, include
from django.conf import settings

from django.conf.urls.static import static

app_name = "app"

urlpatterns = [
    path("", views.home),
    path("hotels/", views.hotel, name="hotel"),
    path("flights/", views.Flight, name="flights"),
    path("bookflight/", views.Flightbook, name="bookflight"),
    path("bookhotel/", views.Hotelbook, name="bookhotel"),
    path("bookedflights/", views.Bookedflights, name="bookedflights"),
    path("bookedhotels/", views.Bookedhotels, name="bookedhotels"),
    path('hotel/', views.allHotels, name='allHotels'),
    path('flight/', views.allFlights, name='allFlights'),
]
