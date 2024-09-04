#!/bin/bash

python manage.py makemigrations
python manage.py migrate

if [ "$APP_MODE" = "prod" ]; then
    gunicorn mainProject.wsgi:application --bind 0.0.0.0:8000 --workers 3 --access-logfile - --error-logfile -
else
    python manage.py runserver 0.0.0.0:8000
fi