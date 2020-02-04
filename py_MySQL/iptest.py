import re
from time import sleep as s

log = list(open("/var/log/syslog.1",'r').read().split('\n'))
newip = []

for entry in log:
	ips = re.findall(r'[0-9]+(?:\.[0-9]+){3}',entry)
	for ip in ips:
		newip.append(ip)

n = []
for i in newip:
	if i not in n:
		n.append(i)

t = list(set(newip))
x = 0
size = len(t)
print(len(t))
while(x != size):
	print("ip: ", t[x])
	x += 1
