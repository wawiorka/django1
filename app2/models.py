from django.db import models
from django.utils import timezone
import datetime

class Place(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name
