# -*- coding: utf-8 -*-
'''
Configuration variables
'''
import os
import sys

# Argumentos del programa en caso de que haya
args = sys.argv

DEBUG = True
SECRET_KEY = 'weslkjasdfjoeijrsdfg234A'

# App directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
PATH = os.path.dirname(os.path.realpath(__file__)) + "/"
PORT = os.environ['PORT'] if 'PORT' in os.environ else 8000

# obtenemos host y topics de las variables de ambient
SQL_PORT = os.environ['SQL_PORT'] if 'SQL_PORT' in os.environ else '3306'
SQL_HOST = os.environ['SQL_HOST'] if 'SQL_HOST' in os.environ else 'localhost'
SQL_DB = "dcos"
SQL_USER = os.environ['SQL_USER'] if 'SQL_USER' in os.environ else 'root'
SQL_PASS = os.environ['SQL_PASS'] if 'SQL_PASS' in os.environ else 'ByPrice123!'
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://"+SQL_USER+":"+SQL_PASS+"@"+SQL_HOST+"/"+SQL_DB+"?host="+SQL_HOST+"?port="+SQL_HOST
SQLALCHEMY_TRACK_MODIFICATIONS=False
DATABASE_CONNECT_OPTIONS = {}

THREADS_PER_PAGE = 8
WTF_CSRF_ENABLED = True
WTF_CSRF_SECRET_KEY = "somethingimpossibletoguess"
