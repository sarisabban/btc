#!/usr/bin/python3
import re , urllib.request, time

while True:
	web = urllib.request.urlopen('https://blockchain.info/ticker')
	for line in web:
		line = line.decode()
		line = line.split()
		if line[0] == '"USD"':
			print('USD =\t' + line[4].split(',')[0] , end = '\r')
	time.sleep(1)
