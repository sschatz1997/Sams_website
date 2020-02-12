from time import sleep as s
from toOwnFiles import files1, logCreator, getBasedOnFile, matchfileToExt, insertToLog, matchExtToFile
from toOwnFiles import returnAuthLog, returnSysLog, returnUfwLog, returnAccessLog, returnErrorLog
from toOwnFiles import returnProftpdLog
from functions import files, compare


def insertIntoOtherDB():
    x1 = 0
    file1 = files()
    file2 = files1()

    while(x1 != len(file1)):
        print("Proccessing %s." % file1[x1])
        temp2 = getBasedOnFile(file1[x1])
        TF1 = matchExtToFile(file1[x1])
        insertToLog(TF1, temp2)
        x1 += 1
        


###########################################
# created by Samuel Schatz                #
# github: https://github.com/sschatz1997  #
# email: sjschatz@captechu.edu            #
###########################################