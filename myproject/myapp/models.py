from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Wind(models.Model):
    wind_level = models.CharField(max_length=64)
    wind_direction = models.CharField(max_length=64)
    add_time = models.DateTimeField()
    def __unicode__(self):
        return self.add_time

class Water(models.Model):
    water_high = models.CharField(max_length=64)
    add_time = models.DateTimeField()
    def __unicode__(self):
        return self.add_time

class Weather(models.Model):
    weather_detail = models.CharField(max_length=5120)
    add_time = models.DateTimeField()
    def __unicode__(self):
        return self.add_time

class WindScrapy(models.Model):
    wind_level = models.CharField(max_length=5120)
    add_time = models.DateTimeField()
    def __unicode__(self):
        return self.add_time

class Tide(models.Model):
    tide_height = models.CharField(max_length=64)
    add_time = models.DateTimeField()
    place = models.CharField(max_length=64)
    def __unicode__(self):
        return self.add_time
