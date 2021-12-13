from django.shortcuts import render, redirect
from .models import Bookings, Vehicles



# Create your views here.


def home(request):
    bookings = Bookings.objects.all()
    vehicles = Vehicles.objects.all()

    return render(request, "booking_mgmt.html", {"bookings": bookings, "vehicles": vehicles})

def register_booking(request):
    booking_number = request.POST['txtBook_num']
    loading_port = request.POST['txtloading_port']
    discharge_port = request.POST['txtDischarge_port']
    departure_date = request.POST['txtDeparture_date']
    arrival_date = request.POST['txtArrival_date']

    booking = Bookings.objects.create(
        booking_number=booking_number, loading_port=loading_port, discharge_port=discharge_port,
        departure_date=departure_date, arrival_date=arrival_date)
    return redirect("/")


def edit_booking(request, booking_number):
    booking = Bookings.objects.get(booking_number=booking_number)
    vehicle = Vehicles.objects.filter(booking=booking_number)

    return render(request, 'edit_booking.html', {"vehicle": vehicle, "booking": booking})


def booking_edition(request):
    booking_number = request.POST['txtBook_num']
    loading_port = request.POST['txtloading_port']
    discharge_port = request.POST['txtDischarge_port']
    departure_date = request.POST['txtDeparture_date']
    arrival_date = request.POST['txtArrival_date']

    booking = Bookings.objects.get(booking_number=booking_number)
    booking.loading_port = loading_port
    booking.discharge_port = discharge_port
    booking.departure_date = departure_date
    booking.arrival_date = arrival_date
    booking.save()

    return redirect("/")


def erase_booking(request, booking_number):
    booking = Bookings.objects.get(booking_number=booking_number)
    booking.delete()

    return redirect("/")


def register_vehicle(request):
    vin_num = request.POST['txtVin_num']
    make = request.POST['txtMake']
    model = request.POST['txtModel']
    weight = request.POST['txtWeight']
    booking_num = request.POST['txtBooking_num']

    vehicle = Vehicles.objects.create(
        vin_num=vin_num, make=make, model=model, weight=weight, booking=booking_num)
    return redirect("/")


def edit_vehicle(request, vin_num):
    vehicle = Vehicles.objects.get(vin_num=vin_num)
    bookings = Bookings.objects.all()

    return render(request, "edit_vehicle.html", {"vehicle": vehicle, "bookings": bookings})


def vehicle_edition(request):
    vin_num = request.POST['txtVin_num']
    make = request.POST['txtMake']
    model = request.POST['txtModel']
    weight = request.POST['txtWeight']
    booking_num = request.POST['txtBooking_num']

    vehicle = Vehicles.objects.get(vin_num=vin_num)
    vehicle.make = make
    vehicle.model = model
    vehicle.weight = weight
    vehicle.booking = booking_num

    vehicle.save()

    return redirect("/")


def erase_vehicle(request, vin_num):
    vehicle = Vehicles.objects.get(vin_num=vin_num)
    vehicle.delete()

    return redirect("/")


