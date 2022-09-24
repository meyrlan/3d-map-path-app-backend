from django.db import models
from django.utils.translation import ugettext_lazy as _


class DataInstance(models.Model):
    class ACTIVITY(models.IntegerChoices):
        WALKING = 0, _("Walking")
        RUNNING = 1, _("Running")
        CYCLING = 2, _("Cycling")
        DRIVING = 3, _("Driving")
        UNKNOWN = 4, _("Unknown")

    lat = models.DecimalField(_("Lattitude"), max_digits=30, decimal_places=20)
    lng = models.DecimalField(_("Longitude"), max_digits=30, decimal_places=20)
    alt = models.DecimalField(_("Altitude"), max_digits=9, decimal_places=3)
    identifier = models.CharField(_("Identifier"), max_length=50, blank=True, null=True)
    timestamp = models.IntegerField(_("Timestamp"))
    floor = models.PositiveSmallIntegerField(_("Floor"), null=True, blank=True)
    horizontal_accuracy = models.DecimalField(_("Horizontal Accuracy"), max_digits=2, decimal_places=2)
    vertical_accuracy = models.DecimalField(_("Vertical Accuracy"), max_digits=2, decimal_places=2)
    confidence = models.DecimalField(_("Confidence"), max_digits=6, decimal_places=5)
    activity = models.PositiveSmallIntegerField(_("Activity"), choices=ACTIVITY.choices, default=ACTIVITY.UNKNOWN)
    data_set = models.ForeignKey(
        "core.DataSet",
        verbose_name=_("DataSet"),
        on_delete=models.PROTECT,
        related_name="data_instances",
    )
