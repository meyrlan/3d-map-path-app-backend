from django.db import models
from django.utils.translation import ugettext_lazy as _


class DataSet(models.Model):
    identifier = models.CharField(_("Identifier"), max_length=50, blank=True, null=True)
