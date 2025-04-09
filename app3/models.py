from django.conf import settings
from django.db import models
from django.utils import timezone
import datetime


class Event(models.Model):
    title = models.CharField(max_length=100)
    date = models.CharField(max_length=10)
    created_at = models.DateTimeField(default=datetime.datetime.now, null=False)


    def created(self):
        self.created_at = timezone.now()
        self.save()


    def __str__(self):
        return self.title

