from django.db import models

# Create your models here.
class Booking(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    package_type = models.CharField(max_length=20)  # "flight", "hotel", "package"
    package_id = models.IntegerField()
    flight_name = models.CharField(max_length=100,null=True, blank=True)
    departure = models.CharField(max_length=100,null=True, blank=True)
    arrival = models.CharField(max_length=100,null=True, blank=True)
    hotel_name = models.CharField(max_length=100,null=True, blank=True)  # For hotel bookings
    hotel_place = models.CharField(max_length=100,null=True, blank=True)  # For hotel bookings
    package_name = models.CharField(max_length=100,null=True, blank=True) 
    place = models.CharField(max_length=100,null=True, blank=True)
    date = models.DateField(null = True,blank = True)
    seats_booked = models.IntegerField(default=1)
     #
