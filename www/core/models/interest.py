from django.db import models

from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinLengthValidator


class Interest(models.Model):
    title = models.CharField(_("Title"), max_length=50, validators=[MinLengthValidator(4)])

    def __str__(self):
        return str(self.title)

    class Meta:
        db_table = "interests"
        verbose_name = _("Interest")
        verbose_name_plural = _("Interests")
