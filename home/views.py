from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Flights, Hotels
from django.http import HttpResponse


# Create your views here.


def home(request):
    return render(request, "home/index.html")


@login_required
def hotel(request):
    return render(request, 'home/hotels.html')

@login_required
def HotelView(request):
    if request.method == "POST":
        city = request.POSt.get("city")
        date = request.POST.get("date")
        rooms = request.POST.get("date")
        hotels = Hotels.objects.filter(city__contains=city).filter(rooms__gte=rooms)
        d = {"date": date}
        h = {"Hotels": hotels}
        r = {"rooms": rooms}
        response = {**h, **d, **r}
        # return render(request, "hotels.html", response)
        return HttpResponse(response)
    else:
        return redirect("/")


@login_required
def FlightView(request):
    if request.method == "POST":
        source = request.POST.get("source").upper()
        destination = request.POST.get("destination").upper()
        date = request.POST.get("date")
        seats = request.POST.get("seats")
        flights = Flights.objects.filter(source=source).filter(destination=destination).filter(seats__gte=seats)
        d = {"date": date}
        f = {"Flights": flights}
        s = {"seats": seats}
        response = {**f, **d, **s}
        # return render(request, "flights.html", response)
        return HttpResponse(response)
    else:
        return redirect('/')

# @login_required
# def Flightbook(request, flight_num=None, date=None):
#     cs = 0
#     c = None
#     price = 0
#     form = SeatForm(request.POST)
#     if request.method == "POST":
#         if form.is_valid():
#             flight = Flights.objects.filter(flight_num=flight_num)
#             seats = form.cleaned_data["seats"]
#             # d1=datetime.datetime.strptime(date, "%Y-%m-%d").date()
#             for i in flight:
#                 c = BookFlight.objects.filter(flight=i.flight_num).filter(date=date)
#                 price = seats * i.eprice
#                 seatrem = i.seats
#             for j in c:
#                 cs = cs + j.seat
#             seatrem = seatrem - cs
#             if (seatrem - seats) > 0:
#                 avail = "available"
#             else:
#                 avail = "unavailable"
#             a = {"availability": avail}
#             p = {"price": price}
#             sb = {"seatsreq": seats}
#             s = {"seatrem": seatrem}
#             b = {"flight": flight}
#             f = {"form": form}
#             d = {"date": date}
#             response = {**b, **d, **f, **s, **a, **sb, **p}
#             print(s)
#             return render(request, "bookflight.html", response)
#         else:
#             return render(request, "bookflight.html", {"form": form})
#     else:
#         return render(request, "bookflight.html", {"form": form})


# @login_required
# def FlightSubmit(request, flight_num=None, date=None, seat=None):
#     user = request.user
#     b = BookFlight(username_id=user, flight=flight_num, date=date, seat=seat)
#     b.save()
#     return redirect("dashboard")


# @login_required
# def Hotelbook(request, hotel=None, date=None):
#     cs = 0
#     c = None
#     price = 0
#     form = RoomForm(request.POST)
#     if request.method == "POST":
#         if form.is_valid():
#             room = form.cleaned_data["rooms"]
#             hotel = Hotels.objects.filter(hotel_name=hotel)
#             # d1=datetime.datetime.strptime(date, "%Y-%m-%d").date()
#             for i in hotel:
#                 c1 = BookHotel.objects.filter(hotel_name=i.hotel_name).filter(date=date)
#                 price = room * i.hotel_price
#                 roomrem = i.rooms
#             for j in c1:
#                 cs = cs + j.room
#             roomrem = roomrem - cs
#             if (roomrem - room) > 0:
#                 avail = "available"
#             else:
#                 avail = "unavailable"
#             a = {"availability": avail}
#             p = {"price": price}
#             rb = {"roomreq": room}
#             r = {"roomrem": roomrem}
#             b = {"hotel": hotel}
#             f = {"form": form}
#             d = {"date": date}
#             response = {**b, **d, **a, **p, **rb, **f, **r}
#             return render(request, "bookhotel.html", response)
#         else:
#             return render(request, "bookhotel.html", {"form": form})
#     else:
#         return render(request, "bookflight.html", {"form": form})


# @login_required
# def HotelSubmit(request, hotel=None, date=None, room=None):
#     user = request.user
#     b = BookHotel(username_id=user, hotel_name=hotel, date=date, room=room)
#     b.save()
#     return redirect("dashboard")
