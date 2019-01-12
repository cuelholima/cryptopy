import json
import urllib.request

# URL DA API
api_key = '6dd7829d-a182-4ff8-8870-223d22b058be'
url = ('https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?CMC_PRO_API_KEY=' + api_key)

# MONTANDO A API
response = urllib.request.urlopen(url).read() #puxa conteudo da url
json_obj = str(response, 'utf-8') #converte conteudo em string
data = json.loads(json_obj) #carrega strings na variavel data

# TESTANDO A API
print(data)

# FILTRANDO API, TRABALHANDO COM DADOS DE UM ITEM
print('Listando criptomoedas e seus ranks')
for item in data['data']:
    print(('Rank:'), item['id'], ('Criptomoeda:'), item['symbol'])