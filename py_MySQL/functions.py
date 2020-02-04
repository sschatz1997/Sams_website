import os
import re
import csv
import random
import base64
import sqlite3
import datetime
import numpy as np
import mysql.connector
from random import randint

def files():
	fs = ["/var/log/auth.log", "/var/log/syslog","/var/log/ufw.log","/var/log/apache2/access.log","/var/log/apache2/error.log", "/var/log/proftpd/proftpd.log" ]
	return fs

def c1():
	file = "/home/sam/pull/test.txt"
	with open(file, 'r') as f:
		coded = f.readline()
	f.close()

	temp1 = base64.b64decode(coded)
	temp2 = temp1.decode('utf-8')
	db = mysql.connector.connect(
		host="localhost",
		passwd = temp2,
		user="localUser1", 
		database="main", 
		auth_plugin='mysql_native_password'
	)
	return db  

def showTables():
	db = c1()
	cursor = db.cursor()
	cursor.execute("show tables;");
	c = cursor.fetchall()
	return c

def getLinesFromFile(file):
	with open(file) as f:
		for i, l in enumerate(f):
			pass
	return i + 1

def getChangedLogFiles():
	dirs = ["/var/log/", "/var/log/apache2/", "/var/log/mysqld/", "/var/log/proftpd/" ]
	exclude = ["alternatives.log", "/var/log/apt/", "/var/log/cassandra"]

def getIPs(file1):
	log = list(open(file,'r').read().split('\n'))
	newip = []

	for entry in log:
		ips = re.findall(r'[0-9]+(?:\.[0-9]+){3}',entry)
		for ip in ips:
			newip.append(ip)

	t = list(set(newip))
	x = 0
	size = len(t)
	return t