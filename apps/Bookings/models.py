from django.db import models



#Creating Database tables "models" Bookings & Vehicles

class Bookings(models.Model):
    booking_number = models.CharField(primary_key=True, max_length=50)
    loading_port = models.CharField(max_length=50)
    discharge_port = models.CharField(max_length=50)
    departure_date = models.CharField(max_length=10)
    arrival_date = models.CharField(max_length=10)

    def __str__(self):
        texto = "{0}{1}"
        return texto.format(self.loading_port, self.discharge_port)
    class Meta:
        ordering = ('departure_date',)

class Vehicles(models.Model):
    vin_num = models.CharField(primary_key=True,max_length=50)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    weight = models.CharField(max_length=50)
    booking = models.CharField(max_length=50)

    class Meta:
        ordering = ('booking',)


