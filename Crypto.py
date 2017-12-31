#!/usr/bin/python3

import urllib.request, time , json , os , pandas


currency = ['XRP' , 'ETH' , 'IOTA' , 'REQ']

try:
	while True:
		data = pandas.read_csv('table.csv')
		web = urllib.request.urlopen('https://www.binance.com/api/v1/ticker/allPrices')
		for line in web:
			line = line.decode()
			line = json.loads(line)
			BTC = list()
			price = list()
			for coin in line:
				for MyCoin in currency:
					if coin['symbol'] == (MyCoin + 'BTC'):
						ThePrice = coin['price']
						price.append(float(ThePrice))
					if coin['symbol'] == 'BTCUSDT':
						TheBTC = coin['price']
						BTC.append(float(TheBTC))
		data.insert(3 , 'Current Price' , price)
		values = (data['Total Amount'] * data['Current Price']) - (data['Total Amount'] * data['Buy Price'])
		data.insert(4 , 'Profit/Loss' , values)
		USD = data['Profit/Loss'] * BTC
		data.insert(5 , 'USD' , USD)
		percent = ((data['Current Price'] - data['Buy Price']) / data['Buy Price']) * 100
		data.insert(6 , '%' , percent)
		os.system('clear')
		print(data)
		time.sleep(1)
except KeyboardInterrupt:
	quit()
