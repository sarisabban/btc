#!/usr/bin/python3

import re , urllib.request, time , json , sys

#https://www.bitstamp.net/api/

#Live Update
while True:
	web = urllib.request.urlopen('https://www.bitstamp.net/api/ticker/')
	for line in web:
		line = line.decode()
		line = json.loads(line)
		#----------------------
		price = line['last']		#Live BTC price
		high = line['high']		#Last 24 hours price high
		low = line['low']		#Last 24 hours price low
		vwap = line['vwap']		#Last 24 hours volume weighted average price
		volume = line['volume']		#Last 24 hours volume
		bid = line['bid']		#Highest buy order
		ask = line['ask']		#Lowest sell order
		timestamp = line['timestamp']	#Unix timestamp date and time
		opening = line['open']		#First price of the day
		#----------------------
		print('BTC/USD = ' + price , end = '\r')
	time.sleep(1.1)				#1.1 second rest becuase Bitstamp's WebSocket allows only 600 requests per 10 minutes (1 second requests), I use 1.1 to be safe so my IP address does not get blocked


'''
#Order Book
web = urllib.request.urlopen('https://www.bitstamp.net/api/order_book/ ')
for line in web:
	line = line.decode()
	line = json.loads(line)
	#----------------------
	bids = line['bids'][0]
	bids_num = len(line['bids'])
	asks = line['asks'][0]
	asks_num = len(line['asks'])
	#----------------------
	print(bids)
	print(asks)
time.sleep(1.1)
'''
