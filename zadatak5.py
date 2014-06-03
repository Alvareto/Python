import sys
import collections

count = collections.defaultdict(int)
with open(sys.argv[1], "r") as dat:
	datoteka = dat.readlines()
	for line in datoteka:
		ip = str(line.split()[0])		
		count[ip] += 1

for ip in sorted(count, key=count.get, reverse=True):
	print(ip + " : "  + str(count[ip]))
