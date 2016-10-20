#!/bin/bash

export SQL_USER="root"
export SQL_PASS=""



source env/bin/activate
gunicorn --workers 3 --bind 0.0.0.0:8000 wsgi:app
