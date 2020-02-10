from time import sleep as s
from toOwnFiles import files1, logCreator, getBasedOnFile, matchfileToExt, insertToLog
from functions import files

x1 = 0
file1 = files()
file2 = files1()

logCreator()
print("Done!")

while(x1 != len(file1)):
    
    print("Proccessing %s." % file1[x])
    temp2 = getBasedOnFile(file1[x])
    TF1 = matchfileToExt()
    


