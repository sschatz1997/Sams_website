import os
import re
import csv
import psutil
import random
import base64
import sqlite3
import datetime
import numpy as np
import mysql.connector
from random import randint
from time import sleep as s
import subprocess as sp
# adding this comment so it will commit
#from IPcount import getAllIPs, getMultiples, toCSV


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

def compare(list1):
	loops = len(list1)
	x = 0
	t = 0
	new = []
	master = getAllIPs()
	for i in list1:
		if i not in master:
			new.append(i)
		else:
			print("no new.")

	return new
				

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
		return l 

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
	l1 = compare(list1)
	size = len(l1)
	#temp = str(list1[1])
	x = 0
	#print("Type1: ", type(temp))
	#print("Type: ", type(file1))
	if(size != 0):
		while(x != size):
			val = str(l1[x])
			#print("val = ", val)
			insert1(val,file1)
			#cursor.execute("INSERT INTO fromLogs(logFile, ipAddr) VALUES (%s,%s);", (file1, temp))
			s(0.5)
			x += 1
	else:
		print("no new values: not inserting anything.")

def getAllIPs():
    db = c1()
    cursor = db.cursor()
    cursor.execute("SELECT ipAddr FROM fromLogs;")
    temp1 = cursor.fetchall()
    x = 0
    finial = []
    while(x != len(temp1)):
        temp2 = str(temp1[x])
        temp2 = temp2.strip("[(',')]")
        finial.append(temp2)
        x += 1
   
    db.close()
    return finial

def getLogFile(ip):
	tempA = []
	x = 0
	db = c1()
	cursor = db.cursor()
	tup = (ip,)
	statement = "SELECT logFile FROM fromLogs WHERE ipAddr = %s;"
	cursor.execute(statement, tup)
	files = cursor.fetchall()

	while(x != len(files)):
		temp1 = str(files[x])
		temp2 = temp1.strip("[(',')]")
		tempA.append(temp2)
		x += 1
	return tempA


#	if(len(files) != 1):
#		while(x != len(files)):
#			print("more then one file. thier are %s files for " % len(files))
#			print(ip)
#			temp1 = str(files[x])
#			temp2 = temp1.strip("[(',')]")
#			tempA.append(temp2)
#			x += 1
#		return tempA, x
#	else:
#		temp1 = str(files[0])
#		temp2 = temp1.strip("[(',')]")
#		return temp1, 0


# ipCounter
#+---------------+-------------+------+-----+-------------------+-------------------+
#| Field         | Type        | Null | Key | Default           | Extra             |
#+---------------+-------------+------+-----+-------------------+-------------------+
#| id            | int         | NO   | PRI | NULL              | auto_increment    |
#| ipAddr        | varchar(30) | NO   |     | NULL              |                   |
#| occr          | int         | NO   |     | NULL              |                   |
#| timeSubmitted | timestamp   | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
#| timeUpdated   | timestamp   | YES  |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
#| logFile       | varchar(100)| NO   |     | NULL              |                   |
#+---------------+-------------+------+-----+-------------------+-------------------+

# pass the value after the first run and file type.
def ipCounter():
#	db = c1()
#	cursor = db.cursor()
	# FIRST RUN
	ips = getAllIPs()
	occr = 1
	size = len(ips)
	x = 0
	
	while(x != size):
		t = 0
		fileCheck = getLogFile(ips[x])
		size2 = len(fileCheck)
		if(size2 < 1):
			occr = size
		while(t != size2):
			file1 = fileCheck.pop()
			insert2(ips[x],occr,file1)
			t += 1
		x += 1
	

def insert1(val, file1):
	db = c1()
	cursor = db.cursor()
	tup = (file1,val)
	statement = "INSERT INTO fromLogs(logFile, ipAddr) VALUES (%s,%s);"
	cursor.execute(statement, tup)
	db.commit()
	db.close()

def insert2(ip, occur,file1):
	db = c1()
	cursor = db.cursor()
	tup = (ip,occur,file1)
	statement = "INSERT INTO ipCounter(ipAddr, occr, logFile) VALUES (%s,%s,%s);"
	cursor.execute(statement, tup)
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

# networking:

#https://github.com/kyan001/ping3
#https://stackoverflow.com/questions/2953462/pinging-servers-in-python?noredirect=1&lq=1

def ipcheck():
	upAddresses = []
	logs = []
	pss = []
	up = 0
	down = 0
	ip = getAllIPs()
	size = len(ip)
	x = 0
	while(x != size):
		temp1 = str(ip.pop())
		status,result = sp.getstatusoutput("ping -c1 -w2 " + str(temp1))
		if status == 0:
			upAddresses.append(temp1)
			log = getLogFile(temp1)
			log = log.pop()
			logs.append(log)
			ps = getPS(log)
			pss.append(ps)
			print("System " + temp1 + " is UP !")
			up += 1
		else:
			print("System " + temp1 + " is DOWN !")
			down += 1

		x += 1
	print("There are %s up." % str(up))
	print("There are %s down."% str(down))
	insertIP(logs, upAddresses, pss)
	#return logs, upAddresses

def getPS(log):
	ML = files()
	if(log == ML[0]):
		return 1
	elif(log == ML[1]):
		return 3
	elif(log == ML[2]):
		return 3
	elif(log == ML[3]):
		return 2
	elif(log == ML[4]):
		return 1
	elif(log == ML[5]):
		return 3

def insertIP(logs, upAddr, pss):
	db = c1()
	cursor = db.cursor()
	x = 0
	size1 = len(upAddr)
	size2 = len(logs)

	while(x != size1 or x != size2):
		ip = upAddr[x]
		log = logs[x]
		ps = pss[x]
		statement = "INSERT INTO upIps(ipAddr, logFile, PS) VALUES(%s,%s,%s);"
		tup = (ip,log,ps,)
		cursor.execute(statement,tup)
		db.commit()
		#print("TUP: ", tup)
		x += 1
	db.close()


def addUpAddress():
    db = c1()
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS upIps(
                id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
                ipAddr VARCHAR(30) NOT NULL,
                logFile VARCHAR(100) NOT NULL,
		timeSubmitted TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
		dateSubmitted DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL            
            );""")
    cursor.commit()
    db.close()
    
