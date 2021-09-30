from django.db import models

# Create your models here.
class Floor(models.Model):
    floor = models.IntegerField
    wait_time = models.IntegerField
    passenger = models.IntegerField
    # elevator_location = models.IntegerField
    
    def __str__(self):
        return self.floor