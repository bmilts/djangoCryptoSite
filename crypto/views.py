from django.shortcuts import render

def home(request):
	import requests
	import json

	# Get crypto price data
	price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,BCH,XRP,XLM,EOS,LTC,ADA,USDT,MIOTA,TRX&tsyms=USD")
	price = json.loads(price_request.content)

	# Get crypto news data
	api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
	api = json.loads(api_request.content)

	# Get blockchain data
	blockchain_request = requests.get("https://blockchain.info/balance?active=1MDUoxL1bGvMxhuoDYx6i11ePytECAk9QK")
	api2 = json.loads(blockchain_request.content)
	
	return render(request, 'home.html', {'api': api, 'api2': api2, 'price': price})

def prices(request):
		if request.method == 'POST':
			import requests
			import json
			
			quote = request.POST['quote']
			quote = quote.upper()
			pricing_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=USD")
			pricing = json.loads(pricing_request.content)
			return render(request, 'prices.html', {'quote':quote, 'pricing':pricing})

		else:
			notfound = "Please enter a cryptocurrency name in the navigation price search bar above, for example BTC,ETH,XLM"
			return render(request, 'prices.html', {'notfound':notfound})

def identity(request):
	return render(request, 'identity.html', {})

def address(request):
		if request.method == 'POST':
			import requests
			import json
			address = request.POST['address']
			address_request = requests.get("https://api.blockcypher.com/v1/btc/main/addrs/" + address + "/balance")
			address = json.loads(address_request.content)
			return render(request, 'address.html', {'address':address})

		else:
			notfound = "Please enter a BTC address in the navigation address search bar above, for example 1DEP8i3QJCsomS4BSMY2RpU1upv62aGvhD"
			return render(request, 'address.html', {'notfound':notfound})

# ETH Address https://api.blockcypher.com/v1/eth/main/addrs/738d145faabb1e00cf5a017588a9c0f998318012