#add token ID from tokens.py
from tokens import cmc_token


def get_cmc_data(crypto):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    params = {'symbol':crypto,'convert':'USD'}
    header = {'X-CMC_PRO_API_KEY': cmc_token}


def main():
    pass

if __name__ == '__main__':
    main()