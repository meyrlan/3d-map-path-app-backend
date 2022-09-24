from celery import shared_task
from django.core.management import call_command

from .one_off import *  # noqa
from .periodic import *  # noqa


@shared_task
def call_command_periodically(name: str, **kwargs):
    call_command(name, **kwargs)
