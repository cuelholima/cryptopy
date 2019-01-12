import json
import requests

# URL DA API
api_key = '?CMC_PRO_API_KEY=6dd7829d-a182-4ff8-8870-223d22b058be'
url = ('https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest' + api_key)

# MONTANDO A API
request = requests.get(url)
results = request.json()

# TESTANDO API
#print(json.dumps(results, sort_keys=True, indent=4))

# TRABALHANDO COM DADOS RANKEADOS
data = results['data']

for currency in data:
    rank = currency['id']
    name = currency['name']
    symbol = currency['symbol']
    print('Rank ' + str(rank) + ': ' + name + ' (' + symbol + ')')
