import re
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Flights, Hotels, BookFlight, BookHotel
from django.http import HttpResponse

# Create your views here.
def home(request):
    print(request.user)
    return render(request, "home/index.html")


@login_required
def Hotel(request):
    if request.method == "POST":
        city = request.POST.get("city").strip()
        fdate = request.POST.get("fdate")
        tdate = request.POST.get("tdate")
        rooms = int(request.POST.get("rooms").strip())
        hotels = Hotels.objects.all().filter(city=city).filter(rooms__gte=rooms)
        d = {"fdate": fdate, "tdate": tdate}
        h = {"Hotels": hotels}
        r = {"rooms": rooms}
        response = {**h, **d, **r, "Page": "Hotels"}
        print(hotels)
        return render(request, "home/hotels.html", response)
    else:
        return redirect("/")


@login_required
def Flight(request):
    if request.method == "POST":
        source = request.POST.get("source").upper().strip()
        destination = request.POST.get("destination").upper().strip()
        date = request.POST.get("date")
        seats = int(request.POST.get("seats").strip())
        flights = (
            Flights.objects.all().filter(source=source)
            .filter(destination=destination)
            .filter(seats__gte=seats)
        )
        d = {"date": date}
        f = {"Flights": flights}
        s = {"seats": seats}
        response = {**f, **d, **s, "Page": "Flights"}
        return render(request, "home/flights.html", response)
    else:
        return redirect("/")

@login_required
def Flightbook(request):
    if request.method == "POST":
        flight = request.GET.get("flight")
        date = request.GET.get("date")
        seats = int(request.GET.get("seats"))
        user = request.user
        flights = Flights.objects.all().filter(flight_num=flight)
        bflight = BookFlight.objects.all().filter(flight_num=flight).filter(date=date)
        booked_seats = 0
        for i in bflight:
            booked_seats += i.seat
        available_seats = flights[0].seats - booked_seats
        if available_seats >= seats:
            b = BookFlight(username_id=user, flight_num=flight, date=date, seat=seats)
            b.save()
            messages.success(request, "Booked")
            return redirect("/home")
        else:
            messages.error(request, "Booking failed")
            return redirect("/home")
    else:
        user = request.user
        bflight = BookFlight.objects.all().filter(username_id=user)
        flights = []
        for i in bflight:
            f = Flights.objects.all().filter(flight_num=i.flight_num)
            flights.append(f[0])
        response = {"Flights": flights, "Page": "Booked Flights"}
        return render(request, "home/flightbook.html", response)

@login_required
def Hotelbook(request):
    if request.method == "POST":
        hotel = request.GET.get("hotel")
        date = request.GET.get("date")
        rooms = int(request.GET.get("rooms"))
        user = request.user
        hotels = Hotels.objects.all().filter(hotel_name=hotel)
        bhotel = BookHotel.objects.all().filter(hotel_name=hotel).filter(date=date)
        booked_rooms = 0
        for i in bhotel:
            booked_rooms += i.room
        available_rooms = hotels[0].rooms - booked_rooms
        if available_rooms >= rooms:
            b = BookHotel(username_id=user, hotel_name=hotel, date=date, room=rooms)
            b.save()
            messages.success(request, "Booked")
            return redirect("/home")
        else:
            messages.error(request, "Booking failed")
            return redirect("/home")
    else:
        user = request.user
        bhotel = BookHotel.objects.all().filter(username_id=user)
        hotels = []
        for i in bhotel:
            h = Hotels.objects.all().filter(hotel_name=i.hotel_name)
            hotels.append(h[0])
        response = {"Hotels": hotels, "Page": "Booked Hotels"}
        return render(request, "home/hotelbook.html", response)