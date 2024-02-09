from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Flights(models.Model):
    id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=200)
    source = models.CharField(max_length=200)
    date = models.DateField()
    destination = models.CharField(max_length=200)
    flight_name = models.CharField(max_length=200)
    flight_num = models.CharField(max_length=10)
    eprice = models.IntegerField(null=True)
    dept_time = models.TimeField(auto_now=False, auto_now_add=False)
    dest_time = models.TimeField(auto_now=False, auto_now_add=False)
    journey_time = models.IntegerField(null=True)
    company = models.CharField(max_length=15, default=" ")
    seats = models.IntegerField()

    def __str__(self):
        return self.flight_num


class Hotels(models.Model):
    id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=200)
    hotel_image = models.ImageField(null=True, upload_to="img/")
    hotel_name = models.CharField(max_length=200)
    hotel_address = models.CharField(max_length=500)
    hotel_price = models.IntegerField(null=True)
    hotel_rating = models.IntegerField(null=True)
    hotel_des = models.CharField(max_length=500)
    rooms = models.IntegerField(default=0)

    def __str__(self):
        return self.hotel_name


# class BookFlight(models.Model):
#     username_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     flight = models.CharField(max_length=10)
#     date = models.CharField(max_length=20)
#     seat = models.IntegerField(default=1)

#     def __str__(self):
#         return self.date


# class BookHotel(models.Model):
#     username_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     hotel_name = models.CharField(max_length=10)
#     date = models.CharField(max_length=20)
#     room = models.IntegerField(default=1)

#     def __str__(self):
#         return self.date
