#-*- coding: utf-8 -*-
from app import app

'''
WSGI for the application
run it with the command

gunicorn --bind 0.0.0.0:8000 wsgi:app

En local (OSX)
source run.sh
sudo service nginx

En production
sudo service byprice-search start
sudo nginx

'''

if __name__ == '__name__':
    app.run(host='0.0.0.0',port=app.config['PORT'])
