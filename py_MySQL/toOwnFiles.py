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
from functions import files
from time import sleep as s


def files1():
	fs = ["auth", "syslog","ufw","access","error", "proftpd" ]
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

def logCreator():
    # this needs to be the non file extension
    files = files1()
    x = 0
    db = c1()
    cursor = db.cursor()
    while(x != len(files)):
        temp = str(files[x])
        temp = temp.strip("{[',']}")
        temp = temp.strip('""')
        print("Making the %s database." % temp)
        s1 = "CREATE TABLE IF NOT EXISTS " 
        s3 = " (id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT, ipAddr VARCHAR(30) NOT NULL, timeSubmitted TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL, dateSubmitted DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL);" 
        state = s1 + temp + s3
        print("\n\n",state,"\n\n")
        #cursor.execute(state,)
        #db.commit()
        s(1)
        x += 1
    #db.close()

def getBasedOnFile(file):
    # this needs to be the full extension
    db = c1()
    cursor = db.cursor()
#    file2 = matchfileToExt(file)
    
    cursor.execute("SELECT ipAddr FROM fromLogs WHERE logFile = %s;", (str(file)),)
    temp = cursor.fetchall()
    db.close()
    x = 0
    ipArr = []
    while(x != len(temp)):
        temp2 = str(temp[x])
        temp2 = temp2.strip("[(',')]")
        ipArr.append(temp2)
        x += 1
    return ipArr

def matchfileToExt(file):
    # this does conversion
    file2 = files()
    if(file == "auth"):
        filePath = file2[0]
    elif(file == "syslog"):
        filePath = file2[1]
    elif(file == "ufw"):
        filePath = file2[2]
    elif(file == "access"):
        filePath = files2[3]
    elif(file == "error"):
        filePath = files2[4]
    elif(file == "proftpd"):
        filePath = files2[5]
    else:
        filePath = "0"
    
    return filePath

def matchExtToFile(file):
    # this does conversion
    x = 0
    file2 = files()
    file3 = files1()
    while(x != len(file3)):
        if(file == file2[x]):
            return file3[x]
        x += 1
    return "0"


def insertToLog(file1, arr): 
    # this needs to be the non file extension 
    x = 0
    db = c1()
    cursor = db.cursor()
   
    while(x != len(arr)):
        val = str(arr[x])
        state = "INSERT INTO %s(ipAddr) VALUES (%s);"
        tup = (file1,val)
        tup2 = (state, file1, val)
        print("Will be excuted: ", tup)
        #cursor.execute(state, tup)
        #db.commit()
        x += 1
    #db.close()
