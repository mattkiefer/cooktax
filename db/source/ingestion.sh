#!/bin/bash
python ingestion.py;
python ../../manage.py loaddata output_test.json
