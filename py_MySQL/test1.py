from time import sleep as s
from functions import files, getLinesFromFile, getIPs

files = files()
x = 0
y = 0

while(x < len(files)):
	print("FILE: ", files[x]," and has ", getLinesFromFile(files[x]))
#	s(1)
	
	x += 1
#print(files)

