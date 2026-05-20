from django.shortcuts import redirect, render
from .models import Package
# Create your views here.
def search(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        packages = Package.objects.all()
        return render(request, "packages.html", {"packages": packages})