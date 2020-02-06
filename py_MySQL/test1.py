import pprint
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
		
	if(x == 0):
		print("FILE: ", files[x]," and has ", getLinesFromFile(files[x]))
		temp = []
		temp = getIPs(files[x])
		d1['a'] = temp
		pprint(d1['a'])
	elif(x == 1):
		print("FILE: ", files[x]," and has ", getLinesFromFile(files[x]))
		temp = []
		temp = getIPs(files[x])
		d1['b'] = temp
		pprint(d1['b'])
	elif(x == 2):
		print("FILE: ", files[x]," and has ", getLinesFromFile(files[x]))
		temp = []
		temp = getIPs(files[x])
		d1['c'] = temp
		pprint(d1['c'])
	elif(x == 3):
		print("FILE: ", files[x]," and has ", getLinesFromFile(files[x]))
		temp = []
		temp = getIPs(files[x])
		d1['d'] = temp
		pprint(d1['d'])
	elif(x == 4):
		print("FILE: ", files[x]," and has ", getLinesFromFile(files[x]))
		temp = []
		temp = getIPs(files[x])
		d1['e'] = temp
		pprint(d1['e'])
	elif(x == 5):
		print("FILE: ", files[x]," and has ", getLinesFromFile(files[x]))
		temp = []
		temp = getIPs(files[x])
		d1['f'] = temp
		pprint(d1['f'])

	s(1)
	x += 1
#print(files)

