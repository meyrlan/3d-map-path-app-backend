from uuid import uuid4

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from datetime import date
from dateutil.relativedelta import relativedelta
from typing import Optional


def random_username():
    return str(uuid4())


class Profile(models.Model):
    class SEX(models.TextChoices):
        MALE = "m", _("Male")
        FEMALE = "f", _("Female")

    first_name = models.CharField(_("First Name"), max_length=30)
    last_name = models.CharField(_("Last Name"), max_length=30)
    sex = models.CharField(_("Sex"), max_length=1, choices=SEX.choices)
    birth_date = models.DateField(_("Birth Date"), null=True, blank=True)

    bio = models.TextField(_("Bio"))
    interests = models.ManyToManyField(
        "core.Interest",
        verbose_name=_("Interests"),
        related_name="profiles",
        db_table="interests_profiles",
    )
    user = models.OneToOneField(
        "core.User",
        verbose_name=_("Users"),
        related_name="user",
        on_delete=models.CASCADE,
    )

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @property
    def age(self) -> Optional[int]:
        return relativedelta(date.today(), self.birth_date).years

    def __str__(self):
        return self.user.email

    class Meta:
        db_table = "profile"
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")
        sensitive_fields = ("birth_date")
