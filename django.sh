#!/bin/bash\
python manage.py makemigrations movies
python manage.py makemigrations api
python manage.py migrate
python manage.py runserver 0.0.0.0:8000