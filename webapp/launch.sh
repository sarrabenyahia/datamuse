#!/bin/bash

bash ./model/data_getter.sh ./model/data.csv

python manage.py migrate
python manage.py runserver
