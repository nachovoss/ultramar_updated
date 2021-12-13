from django.test import TestCase
from  .models import Bookings, Vehicles

# Create your tests here.
class BookingTestCase(TestCase):
    def setUp(self):
        Bookings.object.create(booking_number="1233456666", loading_port="miami", discharge_port="NY",
                               departure_date="2021-12-20", arrival_date="2022-01-22")
        Bookings.object.create(booking_number="122222", loading_port="Liverpool", discharge_port="Sydney",
                               departure_date="2021-12-23", arrival_date="2022-03-22")

