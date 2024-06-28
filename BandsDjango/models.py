from django.contrib.auth.models import User
from django.db import models
from django.forms import TimeField

import Bands


class Band (models.Model):
    name = models.CharField(max_length=50)
    Country = models.CharField(max_length=50)
    year = models.IntegerField()
    numberOfPerformances = models.IntegerField()

    def __str__(self):
        return self.name
    # vidi so e ova


# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    time = TimeField()
    bands = models.ManyToManyField(Bands)
    poster = models.ImageField(upload_to='images/')
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    isOpen = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} on {self.date}"

