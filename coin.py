import json
import requests

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'YOUR API KEY',
}

def bitcoin_price():
    response = requests.get(url, headers=headers)
    response_json = response.json()
    btc_price = response_json['data'][0]

    price = btc_price['quote']['USD']['price']
    percent_change_24h = btc_price['quote']['USD']['percent_change_24h']
    percent_change_7d = btc_price['quote']['USD']['percent_change_7d']

    print ('Bitcoin Price : '
    ,f" $ {price:000,.2f}"
    ,'\n                 ',f"24 hour ({percent_change_24h:0,.2f} %)"
    ,'\n                 ',f"07 day  ({percent_change_7d:0,.2f} %)\n"
    )
bitcoin_price()

def ethereum_price():
    response = requests.get(url, headers=headers)
    response_json = response.json()
    btc_price = response_json['data'][1]

    price = btc_price['quote']['USD']['price']
    percent_change_24h = btc_price['quote']['USD']['percent_change_24h']
    percent_change_7d = btc_price['quote']['USD']['percent_change_7d']

    print ('Ethereum Price : '
    ,f"$ {price:000,.2f}"
    ,'\n                 ',f"24 hour ({percent_change_24h:0,.2f} %)"
    ,'\n                 ',f"07 day  ({percent_change_7d:0,.2f} %)"
    )

ethereum_price()
