#add token ID from tokens.py
from tokens import cmc_token

import requests
import json
from flask import Flask

token = '2026961563:AAGadRSpDv4fe3WvmhxrlQ1_xy6UybrBrpg'

app = Flask(__name__)

@app.route('/', methods = ['POST','GET'])
def index():
    return '<p>coinmarketcap bot</p>'

def write_json(data, filename = 'response.json'):
    with open(filename,'w') as f:
        json.dump(data,f,indent=4,ensure_ascii=False)



def get_cmc_data(crypto):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    params = {'symbol':crypto,'convert':'USD'}
    headers = {'X-CMC_PRO_API_KEY': cmc_token}

    r = requests.get(url,params= params,headers= headers).json()
    write_json(r)
    price = r['data'][crypto]['quote']['USD']['price']

    return price

def main():
    print(get_cmc_data('BTC'))

#-->after 'bot' you must write your bot HTTP API
#https://api.telegram.org/bot2026961563:AAGadRSpDv4fe3WvmhxrlQ1_xy6UybrBrpg/getMe

#https://api.telegram.org/bot2026961563:AAGadRSpDv4fe3WvmhxrlQ1_xy6UybrBrpg/getMe

#--> webhook URL from vtxhub.com
#--> then you run this URL and set webhook:
#https://api.telegram.org/bot2026961563:AAGadRSpDv4fe3WvmhxrlQ1_xy6UybrBrpg/setWebHook?url=https://user7328608265265fd.app.vtxhub.com/



if __name__ == '__main__':
    app.run(debug=True)