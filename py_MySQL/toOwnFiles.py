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
from functions import files, compare
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
    
    cursor.execute("SELECT ipAddr FROM fromLogs WHERE logFile = %s;", (file,))
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
        filePath = file2[3]
    elif(file == "error"):
        filePath = file2[4]
    elif(file == "proftpd"):
        filePath = file2[5]
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

def getStatement(file):
    if(file == "auth"):
        state = "INSERT INTO auth(ipAddr) VALUES (%s);"
    elif(file == "syslog"):
        state = "INSERT INTO syslog(ipAddr) VALUES (%s);"  
    elif(file == "ufw"):
        state = "INSERT INTO ufw(ipAddr) VALUES (%s);"
    elif(file == "access"):
        state = "INSERT INTO access(ipAddr) VALUES (%s);"
    elif(file == "error"):
        state = "INSERT INTO error(ipAddr) VALUES (%s);"
    elif(file == "proftpd"):
        state = "INSERT INTO proftpd(ipAddr) VALUES (%s);"

    return state

def insertToLog(file1, arr): 
    # this needs to be the non file extension 
    x = 0
    db = c1()
    cursor = db.cursor()
    l1 = compare(arr)
    size = len(l1)

    if(size != 0):
        while(x != len(l1)):
            val = str(l1[x])
            #state = getStatement(file1)
            tup = (val,)
            if(file1 == "auth"):
                state = "INSERT INTO auth(ipAddr) VALUES (%s);"
                cursor.execute(state, tup)
            elif(file1 == "syslog"):
                state = "INSERT INTO syslog(ipAddr) VALUES (%s);"
                cursor.execute(state, tup)
            elif(file1 == "ufw"):
                state = "INSERT INTO ufw(ipAddr) VALUES (%s);"
                cursor.execute(state, tup)
            elif(file1 == "access"):
                state = "INSERT INTO access(ipAddr) VALUES (%s);"
                cursor.execute(state, tup)
            elif(file1 == "error"):
                state = "INSERT INTO error(ipAddr) VALUES (%s);"
                cursor.execute(state, tup)
            elif(file1 == "proftpd"):
                state = "INSERT INTO proftpd(ipAddr) VALUES (%s);"
                cursor.execute(state, tup)
            print("Will be excuted: ", state)
            
            db.commit()
            s(1)
            x += 1
    db.close()

def getTotalEnt():
    entries = 0
    temp = returnAuthLog()
    entries += len(temp)
    temp = returnSysLog()
    entries += len(temp)
    temp = returnUfwLog()
    entries += len(temp)
    temp = returnAccessLog()
    entries += len(temp)
    temp = returnErrorLog()
    entries += len(temp)
    temp = returnProftpdLog()
    entries += len(temp)
    return entries

def returnAuthLog():
    db = c1()
    cursor = db.cursor()
    cursor.execute("SELECT ipAddr FROM auth;")
    temp1 = cursor.fetchall()
    db.close()
    x = 0
    finial = []
    while(x != len(temp1)):
        temp2 = str(temp1[x])
        temp2 = temp2.strip("[(',')]")
        finial.append(temp2)
        x += 1

    return finial

def returnSysLog():
    db = c1()
    cursor = db.cursor()
    cursor.execute("SELECT ipAddr FROM syslog;")
    temp1 = cursor.fetchall()
    db.close()
    x = 0
    finial = []
    while(x != len(temp1)):
        temp2 = str(temp1[x])
        temp2 = temp2.strip("[(',')]")
        finial.append(temp2)
        x += 1

    return finial

def returnUfwLog():
    db = c1()
    cursor = db.cursor()
    cursor.execute("SELECT ipAddr FROM ufw;")
    temp1 = cursor.fetchall()
    db.close()
    x = 0
    finial = []
    while(x != len(temp1)):
        temp2 = str(temp1[x])
        temp2 = temp2.strip("[(',')]")
        finial.append(temp2)
        x += 1

    return finial

def returnAccessLog():
    db = c1()
    cursor = db.cursor()
    cursor.execute("SELECT ipAddr FROM access;")
    temp1 = cursor.fetchall()
    db.close()
    x = 0
    finial = []
    while(x != len(temp1)):
        temp2 = str(temp1[x])
        temp2 = temp2.strip("[(',')]")
        finial.append(temp2)
        x += 1

    return finial

def returnErrorLog():
    db = c1()
    cursor = db.cursor()
    cursor.execute("SELECT ipAddr FROM error;")
    temp1 = cursor.fetchall()
    db.close()
    x = 0
    finial = []
    while(x != len(temp1)):
        temp2 = str(temp1[x])
        temp2 = temp2.strip("[(',')]")
        finial.append(temp2)
        x += 1

    return finial

def returnProftpdLog():
    db = c1()
    cursor = db.cursor()
    cursor.execute("SELECT ipAddr FROM proftpd;")
    temp1 = cursor.fetchall()
    db.close()
    x = 0
    finial = []
    while(x != len(temp1)):
        temp2 = str(temp1[x])
        temp2 = temp2.strip("[(',')]")
        finial.append(temp2)
        x += 1

    return finial

###########################################
# created by Samuel Schatz                #
# github: https://github.com/sschatz1997  #
# email: sjschatz@captechu.edu            #
###########################################