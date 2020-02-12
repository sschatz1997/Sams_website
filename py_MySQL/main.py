from time import sleep as s
from functions import getID, getName, getWebsite, getScope, insert

id1 = getID()
x = 0

while(x != getID()):
	name = getName(id1)
	web = getWebsite(id1)
	scope = getScope(id1)
	s(1)
	insert(name, web, scope)
	id1 -= 1
	x += 1

###########################################
# created by Samuel Schatz                #
# github: https://github.com/sschatz1997  #
# email: sjschatz@captechu.edu            #
###########################################