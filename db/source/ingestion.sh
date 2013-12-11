#!/bin/bash
PYTHONPATH=$PYTHONPATH:/home/user/django_projects/cooktax/
export DJANGO_SETTINGS_MODULE=cooktax.settings
python ingestion.py
#python ../../manage.py loaddata output_test.json
