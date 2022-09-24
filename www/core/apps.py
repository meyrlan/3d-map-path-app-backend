from django.utils.translation import gettext_lazy as _

from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = "core"
    label = "core"
    verbose_name = _("Core")

    def ready(self):
        import core.signals
