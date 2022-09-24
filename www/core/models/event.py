from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from django.utils import timezone


class Event(models.Model):
    title = models.CharField(_("Name"), max_length=30)
    attendees = models.ManyToManyField(
        "core.Profile",
        verbose_name=_("Attendees"),
        related_name="events",
        db_table="profiles_events"
    )
    capacity = models.IntegerField(_("Capacity"), validators=[MinValueValidator(settings.MINIMUM_EVENT_CAPACITY)])
    date_time = models.DateTimeField(_("Date time"))
    age_limit = models.IntegerField(_("Age limit"), validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True)
    description = models.TextField(_("Description"))
    photo = models.ImageField(blank=True)
    owner = models.ForeignKey(
        "core.Profile",
        verbose_name=_("Owner"),
        related_name="created_events",
        on_delete=models.CASCADE
    )
    interests = models.ManyToManyField(
        "core.Interest",
        verbose_name=_("Interests"),
        related_name="events",
        db_table="interests_events",
    )

    def clean(self):
        if self.date_time and self.date_time <= timezone.now():
            raise ValidationError({"date_time": "Assigned date could not be earlier than current date."})

    def __str__(self):
        return self.title

    class Meta:
        db_table = "event"
        verbose_name = _("Event")
        verbose_name_plural = _("Events")
