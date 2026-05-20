from django.urls import path
from . import views

urlpatterns = [
    path("search", views.search, name="search"),
    path("flightsdata", views.flightsdata, name="flightsdata"),
]