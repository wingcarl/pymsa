from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Wind(models.Model):
    wind_level = models.CharField(max_length=64)
    wind_direction = models.CharField(max_length=64)
    add_time = models.DateTimeField()
    def __unicode__(self):
        return self.add_time
