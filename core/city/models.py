from django.db import models


class City(models.Model):
    city_name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return "{}".format(self.city_name)
