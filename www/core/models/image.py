from django.db import models

from django.utils.translation import ugettext_lazy as _


class Image(models.Model):
    image = models.ImageField(_("Image"))
    name = models.CharField(_("Name"), max_length=30)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    event = models.ForeignKey(
        "core.Event",
        verbose_name=_("Event"),
        related_name="images",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "image"
        verbose_name = _("Image")
        verbose_name_plural = _("Images")
