#add token ID from tokens.py
from tokens import cmc_token

import requests

def get_cmc_data(crypto):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    params = {'symbol':crypto,'convert':'USD'}
    headers = {'X-CMC_PRO_API_KEY': cmc_token}

    r = requests.get(url,params= params,headers= headers).json()
    print(r)


def main():
    get_cmc_data('BTC')

if __name__ == '__main__':
    main()