from django.db import models
from core.city.models import City


class FlightDetails(models.Model):

    flight_number = models.CharField(max_length=20)
    source = models.ForeignKey(City, related_name='source', on_delete=models.CASCADE)
    destination = models.ForeignKey(City, on_delete=models.CASCADE, related_name='destination')
    departure_date_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    arrival_date_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    price = models.PositiveBigIntegerField()
    # layOver = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Flight Detail'
        verbose_name_plural = 'Flight Details'

