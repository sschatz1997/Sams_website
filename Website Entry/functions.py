import csv
import sqlite3
import random
import numpy as np
from random import randint

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