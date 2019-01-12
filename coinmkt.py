import requests
from requests_toolbelt.utils import dump

global_url = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?CMC_PRO_API_KEY=6dd7829d-a182-4ff8-8870-223d22b058be")

# Puxando toda a API do site
data = dump.dump_all(global_url)
print(data.decode('utf-8'))