#!/bin/bash
# Start Gunicorn processes
echo Starting Gunicorn.
rm -rf multiproc-tmp

#Sharing this directory between workers
mkdir multiproc-tmp

export prometheus_multiproc_dir=multiproc-tmp
# guni
exec gunicorn -c gunicorn_conf.py FrontEndProject.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3