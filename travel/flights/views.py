from django.shortcuts import render, redirect
from .models import Flight
from datetime import datetime
from django.utils import timezone

# Create your views here.
def search(request):
    if request.user.is_authenticated:
        return render(request, 'flightsdata.html')
    else:
        return redirect('login')
    
def flightsdata(request):
    if request.user.is_authenticated:
        departure_city = request.POST.get('departure')
        arrival_city = request.POST.get('arrival')
        date = request.POST.get('date')
        datum = date
        datum = datetime.strptime(datum, "%Y-%m-%d")
        aware_date = timezone.make_aware(datum)
        if aware_date < timezone.now():
            return redirect("/flights/search")
        print(departure_city, arrival_city)
        flights = Flight.objects.filter(departure_city__iexact=departure_city, arrival_city__iexact=arrival_city, date=date)
        return render(request, 'flightsdetails.html', {'flights': flights})
    else:
        return redirect('login')