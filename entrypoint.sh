#!/bin/sh

python manage.py migrate --no-input
python manage.py collectstatic --no-input

# Creating Super-User
# DJANGO_SUPERUSER_PASSWORD=$SUPER_USER_PASSWORD python manage.py createsuperuser --username $SUPER_USER_NAME --email $SUPER_USER_EMAIL --noinput

gunicorn dipense.wsgi:application --bind 0.0.0.0:8000

