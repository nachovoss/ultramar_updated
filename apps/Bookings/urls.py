from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('register_booking/', views.register_booking),
    path('register_vehicle/', views.register_vehicle),
    path('erase_booking/<booking_number>', views.erase_booking),
    path('erase_vehicle/<vin_num>', views.erase_vehicle),
    path('edit_booking/<booking_number>', views.edit_booking),
    path('edit_vehicle/<vin_num>', views.edit_vehicle),
    path('booking_edition/', views.booking_edition),
    path('vehicle_edition/', views.vehicle_edition),
    path('edit_booking/erase_vehicle/<vin_num>', views.erase_vehicle),
    path('edit_booking/edit_vehicle/<vin_num>', views.edit_vehicle)

    ]
