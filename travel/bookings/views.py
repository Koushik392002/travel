from django.shortcuts import redirect, render
from .models import Booking
from django.db import models
from flights.models import Flight
from hotels.models import Hotel
from packages.models import Package
from django.contrib import messages

def book(request, package, package_id, num_seats):
    if request.user.is_authenticated:
        if package == "flight":
            flight = Flight.objects.get(id=package_id)
            if flight.seats > num_seats:
                Booking.objects.create(
                    user=request.user,
                    package_type="flight",
                    package_id=package_id,
                    flight_name=f"{flight.airline} {flight.flight_number}",
                    departure=flight.departure_city,
                    arrival=flight.arrival_city,
                    date = flight.date,
                    seats_booked = num_seats
                )
                Flight.objects.filter(id=package_id).update(seats=flight.seats - num_seats)
                return redirect ("bookings")
        else:
            package_obj = Package.objects.get(id=package_id)
            Booking.objects.create(
                user=request.user,
                package_type="package",
                package_id=package_id,
                package_name=package_obj.title,
                place=package_obj.location,
                date = package_obj.date,
                seats_booked = num_seats
            )
            return redirect ("bookings")
    else:
        return redirect("login")
        
def bookhotel(request, package, package_id, num_seats, date):
    if request.user.is_authenticated:
        hotel = Hotel.objects.get(id=package_id)
        if hotel.rooms_available > num_seats:
            Booking.objects.create(
                user=request.user,
                package_type="hotel",
                package_id=package_id,
                hotel_name=hotel.name,
                hotel_place=hotel.city,
                date = date,
                seats_booked = num_seats
            )
            Hotel.objects.filter(id=package_id).update(rooms_available=hotel.rooms_available - num_seats)
            
            return redirect ("bookings")
        else:
            messages.info(request, "No rooms available for this hotel.")
            return redirect ("/hotels/search")
    else:
        return redirect("login")
def bookings(request):
    if request.user.is_authenticated:
        user_bookings = Booking.objects.filter(user=request.user)
        return render(request, "book.html", {"bookings": user_bookings})
    else:
        return redirect("login")