from time import sleep as s
from toOwnFiles import files1, logCreator, getBasedOnFile, matchfileToExt, insertToLog, matchExtToFile
from functions import files

x1 = 0
file1 = files()
file2 = files1()


while(x1 != len(file1)):
    print("Proccessing %s." % file1[x1])
    temp2 = getBasedOnFile(file1[x1])
    TF1 = matchExtToFile(file)
    insertToLog(TF1, temp2)
    x += 1
    


