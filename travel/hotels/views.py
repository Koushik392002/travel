from django.shortcuts import render, redirect
from .models import Hotel
from datetime import datetime
from django.utils import timezone
# Create your views here.
def search(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            return render(request, "hotelsdata.html")
        else:
            city = request.POST.get("city")
            date = request.POST.get("date")
            datum = date
            naive_date = datetime.strptime(datum, "%Y-%m-%d")
            aware_date = timezone.make_aware(naive_date)
            if aware_date < timezone.now():
                return redirect("/hotels/search")
            print(city)
            print(date)
            hotels = Hotel.objects.filter(city=city, date=date)
            print(hotels)
            return render(request, "hotelsdetails.html", {"hotels": hotels})
    else:
        return redirect("login")
