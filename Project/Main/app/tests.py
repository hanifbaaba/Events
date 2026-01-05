from django.test import TestCase

# Create your tests here.
# root directory = Main
# build command = pip install -r requirements.txt && python manage.py collectstatic --noinput
# start command = python manage.py migrate && gunicorn vengo_backend.wsgi:application