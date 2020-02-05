from time import sleep as s
from functions import files, getLinesFromFile, getIPs, nmapScan

files = files()
x = 0
y = 0
#d1 = {'a':[]}
#d2 = {'b':[]}
#d3 = {'c':[]}
#d4 = {'d':[]}
#d5 = {'e':[]}
#d6 = {'f':[]}
d1 = {'a':[],'b':[],'c':[],'d':[],'e':[],'f':[]}
while(x < len(files)):
	print("FILE: ", files[x]," and has ", getLinesFromFile(files[x]))
		
	if(x == 0):
		temp = []
		temp = getIPs(files[x])
		d1['a'] = temp4
	elif(x == 1):
		temp = []
		temp = getIPs(files[x])
		d1['b'] = temp
	elif(x == 2):
		temp = []
		temp = getIPs(files[x])
		d1['c'] = temp
	elif(x == 3):
		temp = []
		temp = getIPs(files[x])
		d1['d'] = temp
	elif(x == 4):
		temp = []
		temp = getIPs(files[x])
		d1['e'] = temp
	elif(x == 5):
		temp = []
		temp = getIPs(files[x])
		d1['f'] = temp

	s(1)
	x += 1
#print(files)

