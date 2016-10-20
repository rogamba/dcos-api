#-*- coding: utf-8 -*-
from subprocess import Popen, PIPE
from config.py import *

user = SQL_USER
passwd = SQL_PASS
filename = BASE_DIR + "/setup/db.sql"

process = Popen(['mysql', '-u', user, '-p', passwd],
                stdout=PIPE, stdin=PIPE)
output = process.communicate('source ' + filename)[0]
