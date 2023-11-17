from binance.client import Client
from binance.enums import *
import requests, json
import WaspDataAccount

# Connexion compte client
AccountInstance = WaspDataAccount.Account()
client = Client(AccountInstance.GetApiKey(), AccountInstance.GetApiSecret())

# Récupére les informations du compte client
account_info = client.get_account()

pointer = [0, 0, 0]                                                             # correspond au wallet qui détient les fond (que l'on s'apprète à transférer)
normed = [['', 0], ['', 0], ['', 0], ['', 0]]                                   # permet de normer les devises du portefeuille en USDT
watched = [['', 0], ['', 0], ['', 0], ['', 0], ['', 0], ['', 0], ['', 0]]       # derniers prix des 6 marchés à surveiller

'''
# Transaction du BTC vers le BNB /!\ problème de valeur NOTIONAL
order = client.create_order(
    symbol = 'BNBBTC',
    side = SIDE_BUY,
    type = ORDER_TYPE_MARKET,
    quantity = 0.002,
)
'''
# enregistre l'intégralité des valeurs du marché dans 'response'
url = 'https://api1.binance.com'
api_call = '/api/v3/ticker/price'
headers = {'content/type': 'application/json', 'X-MBX-APIKEY': AccountInstance.GetApiKey()}
response = requests.get(url + api_call, headers=headers)
response = json.loads(response.text)

# trie les valeurs de 'response' pour garder les pairs à multiplier dans 'normed' afin de ramener les valeurs en USDT
# trie les valeurs de 'response' pour garder les pairs à surveiller dans 'watched'
# la création de 'normed' permet d'éviter de trier 'response' à chaque fois qu'on ramène nos actifs spot en USDT
print('\nMarket TheWasp is looking at :\n')
iteration_n = 0
iteration_w = 0
for e in response:
    if e['symbol']=='ETHUSDT' or e['symbol']=='BNBUSDT' or e['symbol']=='XRPUSDT' or e['symbol']=='BTCUSDT':
        normed[iteration_n][0] = e['symbol']
        normed[iteration_n][1] = e['price']
        iteration_n += 1
    if e['symbol']=='ETHBTC' or e['symbol']=='BNBETH' or e['symbol']=='XRPBNB' or e['symbol']=='XRPBTC' or e['symbol']=='BNBBTC' or e['symbol']=='XRPETH':
        watched[iteration_w][0] = e['symbol']
        watched[iteration_w][1] = e['price']
        iteration_w += 1

print(f"{watched[0][0]}: {watched[0][1]}\n{watched[1][0]}: {watched[1][1]}\n{watched[2][0]}: {watched[2][1]}\n{watched[3][0]}: {watched[3][1]}\n{watched[4][0]}: {watched[4][1]}\n{watched[5][0]}: {watched[5][1]}\n")
print('current prices of devices\n')
print(f"{normed[0][0]}: {normed[0][1]}\n{normed[1][0]}: {normed[1][1]}\n{normed[2][0]}: {normed[2][1]}\n{normed[3][0]}: {normed[3][1]}")

# Afficher les soldes du BNB, BTC, ETH, XRP et USDT (hors earn)
# 'pointer' détermine le wallet à transférer (actif le + important)
print('\nWallet pointed by TheWasp :\n')
for i in account_info['balances']:
    if i['asset']=='BNB' or i['asset']=='ETH' or i['asset']=='BTC' or i['asset']=='XRP' or i['asset']=='USDT':
        if i['asset']=='USDT':
            normedvalue = float(i['free'])
        else:
            for k in normed:
                if (normed[normed.index(k)][0])[:-4]==i['asset']:
                    normedvalue = float(i['free'])*float(normed[normed.index(k)][1])
        if normedvalue > float(pointer[2]):
            pointer = [i['asset'], i['free'], normedvalue]
        print(f"{i['asset']}: {i['free']} -> {normedvalue} USDT")
print(f"\nWallet to transfer -> {pointer[0]}: {pointer[1]} -> {pointer[2]}\n")

