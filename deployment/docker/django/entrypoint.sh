#!/bin/sh

poetry run python manage.py collectstatic --no-input
poetry run python manage.py migrate
poetry run python manage.py compilemessages
poetry run "$@"
