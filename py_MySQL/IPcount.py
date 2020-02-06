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

def getAllIPs():
   	db = c1()
	cursor = db.cursor()
    cursor.execute("SELECT ipAddr FROM fromLogs;")
    unform = str(cursor.fetchall())
    temp1 = unform.strip("[(',')]")
    return temp1
