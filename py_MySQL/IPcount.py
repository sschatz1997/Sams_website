import base64
import mysql.connector
from time import sleep as s
from functions import files, getLinesFromFile, getIPs, nmapScan, toLogFile

#fromLogs
#+---------------+--------------+------+-----+-------------------+-------------------+
#| Field         | Type         | Null | Key | Default           | Extra             |
#+---------------+--------------+------+-----+-------------------+-------------------+
#| id            | int          | NO   | PRI | NULL              | auto_increment    |
#| logFile       | varchar(100) | NO   |     | NULL              |                   |
#| ipAddr        | varchar(30)  | NO   |     | NULL              |                   |
#| timeSubmitted | timestamp    | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
#| dateSubmitted | datetime     | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
#+---------------+--------------+------+-----+-------------------+-------------------+

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
    #temp1 = unform.strip("[(',')]")
    return finial
