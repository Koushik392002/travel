from django.shortcuts import render, redirect
from .models import Hotel
# Create your views here.
def search(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            return render(request, "hotelsdata.html")
        else:
            city = request.POST.get("city")
            print(city)
            hotels = Hotel.objects.filter(city=city)
            print(hotels)
            return render(request, "hotelsdetails.html", {"hotels": hotels})
    else:
        return redirect("login")
