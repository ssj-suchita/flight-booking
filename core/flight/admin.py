from django.contrib import admin

from core.flight.models import FlightDetails


@admin.register(FlightDetails)
class FlightAdmin(admin.ModelAdmin):
    list_display = ('flight_number', 'source', 'destination', 'departure_date_time', 'arrival_date_time')
