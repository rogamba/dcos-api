#-*- coding: utf-8 -*-
from subprocess import call
from config import *

'''
Construct the database and tables
'''

user = SQL_USER
passwd = SQL_PASS
filename = BASE_DIR + "/setup/db.sql"

def init():
    call('mysql --user=root --password= < '+filename, shell=True)
