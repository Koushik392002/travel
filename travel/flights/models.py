from django.db import models

# Create your models here.

class Flight(models.Model):
    airline = models.CharField(max_length=50)
    flight_number = models.CharField(max_length=20, default = '')
    departure_city = models.CharField(max_length=50)
    arrival_city = models.CharField(max_length=50)
    departure_time = models.DateTimeField(null=True, blank=True)
    arrival_time = models.DateTimeField(null=True, blank=True)
    seats = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(null=True, blank=True)

