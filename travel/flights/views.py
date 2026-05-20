from django.shortcuts import render, redirect
from .models import Flight

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
        print(departure_city, arrival_city)
        flights = Flight.objects.filter(departure_city__iexact=departure_city, arrival_city__iexact=arrival_city, date=date)
        return render(request, 'flightsdetails.html', {'flights': flights})
    else:
        return redirect('login')