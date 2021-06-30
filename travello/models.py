from telusko.settings import TIME_ZONE
from django.db import models

# Create your models here.
class Measurement(models.Model):
    number=models.IntegerField(default="")
    network=models.CharField(max_length=100,default="",editable=False)
    d_speed=models.FloatField(default="")
    u_speed=models.FloatField(default="")
    ping=models.IntegerField(default="")
    date_time=models.DateTimeField(auto_now_add=True, blank=True)