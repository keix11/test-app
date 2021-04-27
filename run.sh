#!/bin/sh

cd /app

uwsgi --socket 0.0.0.0:3031 --chdir /app \
        --wsgi-file /app/app.py --callable app \
        --uid www-data --master --processes 4 --threads 2 &

nginx -g "daemon off;"
