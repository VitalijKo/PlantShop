#!/bin/sh

python3.9 manage.py makemigrations store
python3.9 manage.py migrate
python3.9 manage.py createsuperuser --noinput

gunicorn --bind 0.0.0.0:8000 main.wsgi