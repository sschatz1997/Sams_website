import csv
import random
import base64
import sqlite3
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
		host="10.1.126.36",
		passwd = temp2,
		user="localUser1", 
		database="main", 
		auth_plugin='mysql_native_password'
	)
	return db  

def openSqlite():
	conn = sqlite3.connect('BB.db')
	#T = conn.cursor()
	return conn

def openSqlite2():
	conn = sqlite3.connect('/var/www/html/BB.db')
	#T = conn.cursor()
	return conn
	
def closeSqlite():
	conn = openSqlite()
	conn.close()
	
def createDB():
	conn = openSqlite()
	T = conn.cursor()
	T.execute("""CREATE TABLE IF NOT EXISTS companiesBasic(
		id INTEGER NOT NULL PRIMARY KEY,
		name VARCHAR(500) NOT NULL,
		website VARCHAR(500) NOT NULL,
		scope VARCHAR(500) NOT NULL
	);""")
	closeSqlite()

def createDB2():
	db = c1()
	cursor = db.cursor()
	cursor.execute("""CREATE TABLE IF NOT EXISTS companiesBasic(
		id INTEGER NOT NULL PRIMARY KEY,
		name VARCHAR(500) NOT NULL,
		website VARCHAR(500) NOT NULL,
		scope VARCHAR(500) NOT NULL
	);""")
	db.close()

def createDB3():
	db = c1()
	cursor = db.cursor()
	cursor.execute("""CREATE TABLE IF NOT EXISTS log(
		id INTEGER NOT NULL PRIMARY KEY,
		ip VARCHAR(40) NOT NULL,
		time VARCHAR(50) NOT NULL,
		browser VARCHAR(100) NOT NULL
	);""")
	db.close()

def firstEntry():
	conn = openSqlite()
	T = conn.cursor()
	id = 1 
	chapter = "null"
	term = "testing"
	defi = "this is so that the program doesnt pull an NULL value"
	T.execute("INSERT INTO companiesBasic(id, name, website, scope) VALUES (?,?,?,?);", (id, chapter, term, defi,))
	conn.commit()
	closeSqlite()

def loging():
	conn = openSqlite()
	T = conn.cursor()
