import WaspDataAccount
import requests, json

class Service:
    def __init__(self) -> None:
        self.Pointer = [0, 0, 0]
        self.Normed = [['', 0], ['', 0], ['', 0], ['', 0]]
        self.Watched = [['', 0], ['', 0], ['', 0], ['', 0], ['', 0], ['', 0]]
        self.WatchedLess1 = [['', 0], ['', 0], ['', 0], ['', 0], ['', 0], ['', 0]]
        self.SpotWallet = [['', 0, 0], ['', 0, 0], ['', 0, 0], ['', 0, 0], ['', 0, 0]]
        self.Url = 'https://api1.binance.com'
        self.ApiCall = '/api/v3/ticker/price'
        self.AccountInstance = WaspDataAccount.Account()
        self.Headers = {'content/type': 'application/json', 'X-MBX-APIKEY': self.AccountInstance.GetApiKey()}
        self.AccountInfo = self.AccountInstance.Login()
        self.BalanceInfo = self.AccountInfo['balances']

    def AtributResponse(self):
        # attribue les données du marchée dans 'response'
        # trie les données à surveiller dans 'watched'
        # trie les données à utiliser pour normer en USDT dans 'normed'
        response = requests.get(self.Url + self.ApiCall, headers=self.Headers)
        response = json.loads(response.text)
        iteration_n = 0
        iteration_w = 0
        for e in response:
            if e['symbol']=='ETHUSDT' or e['symbol']=='BNBUSDT' or e['symbol']=='XRPUSDT' or e['symbol']=='BTCUSDT':
                self.Normed[iteration_n][0] = e['symbol']
                self.Normed[iteration_n][1] = e['price']
                iteration_n += 1
            if e['symbol']=='ETHBTC' or e['symbol']=='BNBETH' or e['symbol']=='XRPBNB' or e['symbol']=='XRPBTC' or e['symbol']=='BNBBTC' or e['symbol']=='XRPETH':
                self.Watched[iteration_w][0] = e['symbol']
                self.Watched[iteration_w][1] = e['price']
                iteration_w += 1

    def AtributWallet(self):
        # norme les valeur du portefeuille spot avec 'normed' puis attribue le wallet avec le plus gros actif à 'pointed'
        SpotPlace = 0
        for i in self.BalanceInfo:
            if i['asset']=='BNB' or i['asset']=='ETH' or i['asset']=='BTC' or i['asset']=='XRP' or i['asset']=='USDT':
                if i['asset']=='USDT':
                    normedvalue = float(i['free'])
                else:
                    for k in self.Normed:
                        if (self.Normed[self.Normed.index(k)][0])[:-4]==i['asset']:
                            normedvalue = float(i['free'])*float(self.Normed[self.Normed.index(k)][1])
                if normedvalue > float(self.Pointer[2]):
                    self.Pointer = [i['asset'], i['free'], normedvalue]
                self.SpotWallet[SpotPlace][0] = i['asset']
                self.SpotWallet[SpotPlace][1] = i['free']
                self.SpotWallet[SpotPlace][2] = normedvalue
                SpotPlace += 1
        
    def CompareMarket(self):
        print('à faire')

    def GetPointer(self):
        # obtenir 'pointer' (actif le + important du portefeuille)
        return self.Pointer

    def GetWatched(self):
        # obtenir 'watched' (market surveillé par TheWasp)
        return self.Watched

    def GetNormed(self):        
        # obtenir 'normed' (prix du market utilisés pour normer les valeurs du portefeuille)
        return self.Normed

    def GetSpotWallet(self):
        # obtenir les données du portefeuille
        return self.SpotWallet