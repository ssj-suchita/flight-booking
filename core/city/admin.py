from django.contrib import admin

from core.city.models import City


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('city_name',)
