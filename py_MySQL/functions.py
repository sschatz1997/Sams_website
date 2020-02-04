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
