from django.conf import settings
from django.db import models
from django.utils import timezone

class Person(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    