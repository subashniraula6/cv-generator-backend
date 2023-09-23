#!/bin/bash
source /var/www/cv-generator-backend/kneg/bin/activate
gunicorn -w 4 -b 0.0.0.0:5000 app:app

