from functions import files


def files1():
	fs = ["auth.log", "syslog","ufw.log","access.log","error.log", "proftpd.log" ]
	return fs

def matchfileToExt(file):
    # this does conversion
    file2 = files()
    if(file == "auth.log"):
        filePath = file2[0]
    elif(file == "syslog"):
        filePath = file2[1]
    elif(file == "ufw.log"):
        filePath = file2[2]
    elif(file == "access.log"):
        filePath = files2[3]
    elif(file == "error.log"):
        filePath = files2[4]
    elif(file == "proftpd.log"):
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

###########################################
# created by Samuel Schatz                #
# github: https://github.com/sschatz1997  #
# email: sjschatz@captechu.edu            #
###########################################