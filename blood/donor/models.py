from django.db import models

# Create your models here.

from blood.donor.constants import *


class DonorInformation(models.Model):
    """"""
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    Email = models.CharField(max_length=255, blank=False)
    Phone = models.CharField(max_length=30, blank=False)
    Age = models.CharField(max_length=10)
    city = models.CharField(max_length=100, blank=False)
    group = models.IntegerField(choices=BLOOD_GROUP, default=0)
    reason = models.IntegerField(choices=REASON_FOR_DONATION, default=0)
