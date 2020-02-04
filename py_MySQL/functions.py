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
def getID():
	db = openSqlite()
	c = db.cursor()
	c.execute("SELECT id FROM companiesBasic WHERE id > 0;")
	t0 = c.fetchall()
	t1 = str(t0.pop())
	t2 = t1.strip("([','])")
	id1 = int(t2)
	return id1 

def getName(id1):
	db = openSqlite()
	c = db.cursor()
	c.execute("SELECT name FROM companiesBasic WHERE id = (?);", (id1,))
	t0 = c.fetchall()
	t1 = str(t0.pop())
	name = t1.strip("([','])")
	return name

def getWebsite(id1):
	db = openSqlite()
	c = db.cursor()
	c.execute("SELECT website FROM companiesBasic WHERE id = (?);", (id1,))
	t0 = c.fetchall()
	t1 = str(t0.pop())
	website = t1.strip("([','])")
	return website 

def getScope(id1):
	db = openSqlite()
	c = db.cursor()
	c.execute("SELECT scope FROM companiesBasic WHERE id = (?);", (id1,))
	t0 = c.fetchall()
	t1 = str(t0.pop())
	scope = t1.strip("([','])")
	return scope
				
def insert(name, web, sc):
	db = c1()
	cursor = db.cursor()
	statement = "INSERT INTO companiesBasic(name, website, scope) VALUES(%s,%s,%s);"
	tup = (name, web, sc)
	cursor.execute(statement, tup)
	db.commit()
	db.close()
	print("Entered: ", tup)

def getFirstID():
	db = openSqlite()
	c = db.cursor()
	c.execute("SELECT COUNT(*) FROM companiesBasic;")
	t0 = c.fetchall()
	t1 = str(t0.pop())
	t2 = t1.strip("([','])")
	count = int(t2)
	return count 

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
