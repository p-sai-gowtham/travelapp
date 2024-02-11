from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Flights, Hotels, BookFlight, BookHotel

# Create your views here.


@login_required
def home(request):
    return render(request, "home/index.html")


def hotel(request):
    if request.method == "POST":
        city = request.POST.get("city").strip()
        fdate = request.POST.get("fdate")
        tdate = request.POST.get("tdate")
        rooms = int(request.POST.get("rooms").strip())
        hotels = Hotels.objects.all().filter(city=city)
        available_hotels = []
        for i in hotels:
            bhotel = (
                BookHotel.objects.all()
                .filter(hotel_name=i.hotel_name)
                .filter(date__range=[fdate, tdate])
            )
            booked_rooms = 0
            for j in bhotel:
                booked_rooms += j.room
            available_rooms = i.rooms - booked_rooms
            if available_rooms >= rooms:
                available_hotels.append(i)
        if len(available_hotels) == 0:
            messages.error(request, "No hotels available")
            return redirect("/home")
        else:
            response = {
                "Hotels": available_hotels,
                "fdate": fdate,
                "tdate": tdate,
                "rooms": rooms,
                "Page": "Hotels",
            }
            return render(request, "home/hotels.html", response)


def Flight(request):
    if request.method == "POST":
        source = request.POST.get("source").strip()
        destination = request.POST.get("destination").strip()
        date = request.POST.get("date")
        seats = int(request.POST.get("seats").strip())
        print(source, destination, date, seats)
        print(source, destination, date, seats)
        print(source, destination, date, seats)
        print(source, destination, date, seats)
        print(source, destination, date, seats)
        print(source, destination, date, seats)
        print(source, destination, date, seats)
        print(source, destination, date, seats)
        print(source, destination, date, seats)
        print(source, destination, date, seats)
        print(source, destination, date, seats)
        print(source, destination, date, seats)
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
    flights = Flights.objects.all().filter(username_id=user)
    response = {"Flights": flights, "Page": "Booked Flights"}
    return render(request, "home/flights.html", response)


@login_required
def Bookedhotels(request):
    user = request.user
    hotels = Hotels.objects.all().filter(username_id=user)
    response = {"Hotels": hotels, "Page": "Booked Hotels"}
    return render(request, "home/hotels.html", response)


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
            return redirect("/bookedflights")
        else:
            messages.error(request, "Booking failed")
            return redirect("/")


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
