from django.urls import path
from . import views

urlpatterns = [
    path("<str:package>/<int:package_id>/<int:num_seats>/", views.book, name="book"),
    path("<str:package>/<int:package_id>/<int:num_seats>/<str:date>/", views.bookhotel, name="bookhotel"),
    path("bookings/", views.bookings, name="bookings"),
]