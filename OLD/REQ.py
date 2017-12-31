#!/usr/bin/python3

import urllib.request, time , json , os

#Inputs
buy_price 	= 0.00000723
profit_percent	= 25

#Selling Target
Sell = ((buy_price * profit_percent) / 100) + buy_price
Sell = f'{Sell:.9f}'
print('For ' + str(profit_percent) + '% profit sell at:\t' + Sell)

#Live Update
while True:
	web = urllib.request.urlopen('https://www.binance.com/api/v1/ticker/allPrices')
	for line in web:
		line = line.decode()
		line = json.loads(line)
		#Coin Price
		price = line[81]['price']
		#Calculations
		Gain_percent = round((((float(price) - buy_price) / buy_price) * 100) , 2)
		#Output
		print('REQ/BTC = ' + price , '\tGain/Loss = ' + str(Gain_percent) + '%' , end = '\r')
		if Gain_percent >= profit_percent:
			os.system('( speaker-test -t sine -f 1000 )& pid=$! ; sleep 0.1s ; kill -9 $pid')
		else:
			continue
		time.sleep(1)
