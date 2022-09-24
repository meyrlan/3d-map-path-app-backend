from django.db import models
from user.models import User


class Location(models.Model):
    longitude = models.FloatField()
    latitude = models.FloatField()
    altitude = models.FloatField()
    identifier = models.CharField(max_length=255, null=True)
    timestamp = models.IntegerField()
    floor = models.IntegerField(null=True)
    horizontal_accuracy = models.FloatField()
    vertical_accuracy = models.FloatField()
    confidence_in_location_accuracy = models.FloatField()
    activity = models.CharField(max_length=50, null=True)
    user = models.ForeignKey(
        User,
        related_name="timeline",
        on_delete=models.CASCADE
    )
