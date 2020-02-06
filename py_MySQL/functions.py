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
from time import sleep as s

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
	cursor.execute("show tables;")
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
	log = list(open(file1,'r').read().split('\n'))
	newip = []

	for entry in log:
		ips = re.findall(r'[0-9]+(?:\.[0-9]+){3}',entry)
		for ip in ips:
			newip.append(ip)

	t = list(set(newip))
	x = 0
	size = len(t)
	return t

def logCreator():
	db = c1()
	cursor = db.cursor()
	cursor.execute("""CREATE TABLE IF NOT EXISTS fromLogs(
		id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
		logFile VARCHAR(100) NOT NULL,
		ipAddr VARCHAR(30) NOT NULL,
		timeSubmitted TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
		dateSubmitted DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL
	);""")
	db.commit()
	db.close()
#+---------------+--------------+------+-----+-------------------+-------------------+
#| Field         | Type         | Null | Key | Default           | Extra             |
#+---------------+--------------+------+-----+-------------------+-------------------+
#| id            | int          | NO   | PRI | NULL              | auto_increment    |
#| logFile       | varchar(100) | NO   |     | NULL              |                   |
#| ipAddr        | varchar(30)  | NO   |     | NULL              |                   |
#| timeSubmitted | timestamp    | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
#| dateSubmitted | datetime     | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
#+---------------+--------------+------+-----+-------------------+-------------------+


def secPlusMySQL():
	db = c1()
	cursor = db.cursor()
	cursor.execute("""CREATE TABLE IF NOT EXISTS secPlusDefs(
		id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
		chapter INTEGER NOT NULL,
		term VARCHAR(100) NOT NULL,
		def VARCHAR(500) NOT NULL
	);""")
	db.commit()
	db.close()

def toLogFile(list1,file1):
	db = c1()
	cursor = db.cursor()
	
	#size = len(list1)
	x = 0
	#while(x != size):
	#	temp = list1[x]
	#	tup = (file1,temp,)
	tup = (file1,list1,)
	cursor.execute("INSERT INTO fromLogs(logFile, ipAddr) VALUES (%s,%s);", tup)
	db.commit()
	db.close()

def nmapScan(ip,file1):
	nm = nmap.PortScaner()
	rand = nm.scan(ip, "1-444")
	print("THIS WILL TAKE A WHILE")
	if(file1 == "/var/log/auth.log"):
		p1 = "/home/sam/CSVnmap/auth/"
	elif(file1 == "/var/log/syslog"):
		p2 = "/home/sam/CSVnmap/sys/"
	elif(file1 == "/var/log/ufw.log"):
		p3 = "/home/sam/CSVnmap/ufw/"
	elif(file1 == "/var/log/apache2/access.log"):
		p4 = "/home/sam/CSVnmap/apache/"
	elif(file1 == "/var/log/apache2/error.log"):
		p5 = "/home/sam/CSVnmap/apacheE/"
	elif(file1 == "/var/log/proftpd/proftpd.log"):
		p6 = "/home/sam/CSVnmap/ftp/"
	ending = ".csv"
	file1 = p1 + str(ip) + ending

