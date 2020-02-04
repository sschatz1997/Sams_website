import csv
import random
import base64
import sqlite3
import datetime
import numpy as np
import mysql.connector
from random import randint

def c1():
	file = "/home/sam/pull/test.txt"
	with open(file, 'r') as f:
		coded = f.readline()
	f.close()

	temp1 = base64.b64decode(coded)
	temp2 = temp1.decode('utf-8')
	print(temp2)
	db = mysql.connector.connect(
		host="localhost",
		passwd = temp2,
		user="localUser1", 
		database="main", 
		auth_plugin='mysql_native_password'
	)
	return db  


#transfer from sqlite3
def openSqlite():
	conn = sqlite3.connect("/var/www/html/BB.db")
	return conn

def closesqlite():
	conn = openSqlite()
	conn.close()

# will open the db and go from each entry and enter them in mySQL
# +---------+--------------+------+-----+---------+----------------+
#| Field   | Type         | Null | Key | Default | Extra          |
#+---------+--------------+------+-----+---------+----------------+
#| id      | int          | NO   | PRI | NULL    | auto_increment |
#| name    | varchar(500) | NO   |     | NULL    |                |
#| website | varchar(500) | NO   |     | NULL    |                |
#| scope   | varchar(500) | NO   |     | NULL    |                |
#+---------+--------------+------+-----+---------+----------------+

def getFirstID():
	db = c1()
	c = db.cursor()
	c.execute("SELECT COUNT(*) FROM defs;")
	t0 = c.fetchall()
	t1 = str(t0.pop())
	t2 = t1.strip("([','])")
	count = int(t2)
	return count 

def transfer():
	#@@@@@



# testing
def test():
	db = c1()
	cursor = db.cursor()
	cursor.execute("""CREATE TABLE IF NOT EXISTS t1(
		id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
		name VARCHAR(100) NOT NULL
	);""")
	db.commit()
	db.close()

def showTables():
	db = c1()
	cursor = db.cursor()
	cursor.execute("show tables;");
	c = cursor.fetchall()
	return c
