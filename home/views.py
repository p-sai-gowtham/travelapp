from pyexpat import features
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Flights, Hotels, BookFlight, BookHotel
import json

# Create your views here.


@login_required
def home(request):
    hotels= Hotels.objects.all()
    features = []
    hdet={
        "features": features
    }
    for i in hotels:
        hdet["features"].append({
            "type": "Feature",
            "properties": {
                "name": i.hotel_name,
                "address": i.hotel_address,
                "rating": i.hotel_rating,
            },
            "geometry": {
                "type": "Point",
                "coordinates": [i.lon, i.lat]
            }
        })
    json.dumps(hdet)
    return render(request, "home/index.html", {"hdet": hdet})


@login_required
def allHotels(request):
    hotels = Hotels.objects.all()
    features = []
    hdet={
        "features": features
    }
    for i in hotels:
        hdet["features"].append({
            "type": "Feature",
            "properties": {
                "name": i.hotel_name,
                "address": i.hotel_address,
                "rating": i.hotel_rating,
            },
            "geometry": {
                "type": "Point",
                "coordinates": [i.lon, i.lat]
            }
        })
    json.dumps(hdet)
    response = {"Hotels": hotels, "Page": "All Hotels", "hdet": hdet}

    return render(request, "home/hotels.html", response)

@login_required
def allFlights(request):
    flights = Flights.objects.all()
    response = {"Flights": flights, "Page": "Flights"}
    return render(request, "home/flights.html", response)

def hotel(request):
    if request.method == "POST":
        city = request.POST.get("city").upper().strip()
        fdate = request.POST.get("fdate")
        tdate = request.POST.get("tdate")
        rooms = int(request.POST.get("rooms").strip())
        hotels = Hotels.objects.all().filter(city=city)
        available_hotels = []
        for i in hotels:
            bhotel = (
                BookHotel.objects.all()
                .filter(hotel_name=i.hotel_name)
                .filter(fdate=fdate)
                .filter(tdate=tdate)
            )
            booked_rooms = 0
            for j in bhotel:
                booked_rooms += j.room
            available_rooms = i.rooms - booked_rooms
            if available_rooms >= rooms:
                available_hotels.append(i)
        features = []
        hdet={
            "features": features
        }
        for i in available_hotels:
            hdet["features"].append({
                "type": "Feature",
                "properties": {
                    "name": i.hotel_name,
                    "address": i.hotel_address,
                    "rating": i.hotel_rating,
                },
                "geometry": {
                    "type": "Point",
                    "coordinates": [i.lon, i.lat]
                }
            })
        json.dumps(hdet)

        
        if len(available_hotels) == 0:
            messages.error(request, "No hotels available")
            return redirect("/")
        else:
            response = {
                "Hotels": available_hotels,
                "fdate": fdate,
                "tdate": tdate,
                "rooms": rooms,
                "Page": "Hotels",
                "hdet": hdet
            }
            return render(request, "home/hotels.html", response)


def Flight(request):
    if request.method == "POST":
        source = request.POST.get("source").upper().strip()
        destination = request.POST.get("destination").upper().strip()
        date = request.POST.get("date")
        seats = int(request.POST.get("seats").strip())
        flights = (
            Flights.objects.all().filter(source=source).filter(destination=destination)
        )
        available_flights = []
        for i in flights:
            bflight = (
                BookFlight.objects.all()
                .filter(flight_num=i.flight_num)
                .filter(date=date)
            )
            booked_seats = 0
            for j in bflight:
                booked_seats += j.seat
            available_seats = i.seats - booked_seats
            if available_seats >= seats:
                available_flights.append(i)
        if len(available_flights) == 0:
            messages.error(request, "No flights available")
            return redirect("/")
        else:
            response = {
                "Flights": available_flights,
                "date": date,
                "seats": seats,
                "Page": "Flights",
            }
            return render(request, "home/flights.html", response)


@login_required
def Bookedflights(request):
    user = request.user
    flights = BookFlight.objects.all().filter(username_id=user)
    response = {"Flights": flights, "Page": "Booked Flights"}
    return render(request, "home/flights.html", response)


@login_required
def Bookedhotels(request):
    user = request.user
    print(user)
    hotels = BookHotel.objects.all().filter(username_id=user)
    features = []
    hdet={
        "features": features
    }
    for i in hotels:
        hdet["features"].append({
            "type": "Feature",
            "properties": {
                "name": i.hotel_name,
                "address": i.hotel_address,
                "rating": i.hotel_rating,
            },
            "geometry": {
                "type": "Point",
                "coordinates": [i.lon, i.lat]
            }
        })
    json.dumps(hdet)
    response = {"Hotels": hotels, "Page": "Booked Hotels", "hdet": hdet}
    return render(request, "home/hotels.html", response)


def Flightbook(request):
    if request.method == "POST":
        flight = request.POST.get("flight")
        date = request.POST.get("date")
        seats = int(request.POST.get("seats"))
        user = request.user
        flights = Flights.objects.all().filter(flight_num=flight)
        bflight = BookFlight.objects.all().filter(flight_num=flight).filter(date=date)
        booked_seats = 0
        for i in bflight:
            booked_seats += i.seat
        available_seats = flights[0].seats - booked_seats
        if available_seats >= seats:
            b = BookFlight(
                username_id=user,
                flight_num=flight,
                date=date,
                seat=seats,
                source=flights[0].source,
                destination=flights[0].destination,
                flight_name=flights[0].flight_name,
                eprice=flights[0].eprice,
                dept_time=flights[0].dept_time,
                dest_time=flights[0].dest_time,
                journey_time=flights[0].journey_time,
                company=flights[0].company,
                lat=flights[0].lat,
                lon=flights[0].lon,
            )
            b.save()
            messages.success(request, "Booked")
            return redirect("/bookedflights")
        else:
            messages.error(request, "Booking failed")
            return redirect("/")


def Hotelbook(request):
    if request.method == "POST":
        hotel = request.POST.get("hotel")
        fdate = request.POST.get("fdate")
        tdate = request.POST.get("tdate")
        rooms = int(request.POST.get("rooms"))
        user = request.user
        hotels = Hotels.objects.all().filter(hotel_name=hotel)
        bhotel = (
            BookHotel.objects.all()
            .filter(hotel_name=hotel)
            .filter(fdate=fdate)
            .filter(tdate=tdate)
        )
        booked_rooms = 0
        for i in bhotel:
            booked_rooms += i.room
        available_rooms = hotels[0].rooms - booked_rooms
        if available_rooms >= rooms:
            b = BookHotel(
                username_id=user,
                hotel_name=hotel,
                fdate=fdate,
                tdate=tdate,
                room=rooms,
                city=hotels[0].city,
                hotel_image=hotels[0].hotel_image,
                hotel_address=hotels[0].hotel_address,
                hotel_price=hotels[0].hotel_price,
                hotel_rating=hotels[0].hotel_rating,
                hotel_des=hotels[0].hotel_des,
                lat=hotels[0].lat,
                lon=hotels[0].lon,
            )
            b.save()
            messages.success(request, "Booked")
            return redirect("/bookedhotels")
        else:
            messages.error(request, "Booking failed")
            return redirect("/")
