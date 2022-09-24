from django.db import models
from django.utils.translation import ugettext_lazy as _


class DataInstance(models.Model):
    class ACTIVITY(models.TextChoices):
        WALKING = "Walking"
        RUNNING = "Running"
        CYCLING = "Cycling"
        DRIVING = "Driving"
        UNKNOWN = "Unknown"

    lat = models.DecimalField(_("Lattitude"), max_digits=20, decimal_places=15)
    lng = models.DecimalField(_("Longitude"), max_digits=20, decimal_places=15)
    alt = models.DecimalField(_("Altitude"), max_digits=20, decimal_places=15)
    identifier = models.CharField(_("Identifier"), max_length=50, blank=True, null=True)
    timestamp = models.IntegerField(_("Timestamp"))
    floor = models.PositiveSmallIntegerField(_("Floor"), null=True, blank=True)
    horizontal_accuracy = models.DecimalField(_("Horizontal Accuracy"), max_digits=20, decimal_places=15)
    vertical_accuracy = models.DecimalField(_("Vertical Accuracy"), max_digits=20, decimal_places=15)
    confidence = models.DecimalField(_("Confidence"), max_digits=20, decimal_places=15)
    activity = models.CharField(_("Activity"), default="UNKNOWN", max_length=10)
    data_set = models.ForeignKey(
        "core.DataSet",
        verbose_name=_("DataSet"),
        on_delete=models.PROTECT,
        related_name="data_instances",
    )
