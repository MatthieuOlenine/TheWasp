import WaspDataAccount
import requests, json, copy

class Service:
    def __init__(self) -> None:
        self.winner = ['', 0]
        self.Pointer = ['', 0, 0]
        self.Normed = [['', 0], ['', 0], ['', 0], ['', 0]]
        self.NormedLess1 = [['', 0], ['', 0], ['', 0], ['', 0]]
        self.SpotWallet = [['', 0, 0], ['', 0, 0], ['', 0, 0], ['', 0, 0], ['', 0, 0]]
        self.Url = 'https://api1.binance.com'
        self.ApiCall = '/api/v3/ticker/price'
        self.AccountInstance = WaspDataAccount.Account()
        self.Headers = {'content/type': 'application/json', 'X-MBX-APIKEY': self.AccountInstance.GetApiKey()}
        self.AccountInfo = self.AccountInstance.Login()
        self.BalanceInfo = self.AccountInfo['balances']

    def LogIn(self):
        self.AccountInfo = self.AccountInstance.Login()
        self.BalanceInfo = self.AccountInfo['balances']

    def AtributResponse(self):
        # attribue les données du marchée dans 'response'
        # trie les données à surveiller dans 'watched' et conserve la dernière itération de 'Watched' dans 'WatchedLess1'
        # trie les données à utiliser pour normer en USDT dans 'normed' et conserve la dernière itération de 'Normed' dans 'NormedLess1'
        self.NormedLess1 = copy.deepcopy(self.Normed)
        response = requests.get(self.Url + self.ApiCall, headers=self.Headers)
        response = json.loads(response.text)
        iteration = 0
        for e in response:
            if e['symbol']=='ETHUSDT' or e['symbol']=='BNBUSDT' or e['symbol']=='XRPUSDT' or e['symbol']=='BTCUSDT':
                self.Normed[iteration][0] = e['symbol']
                self.Normed[iteration][1] = e['price']
                iteration += 1

    def AtributWallet(self):
        # norme les valeur du portefeuille spot avec 'normed' puis attribue le wallet avec le plus gros actif à 'pointed'
        SpotPlace = 0
        self.Pointer = ['', 0, 0]
        for i in self.BalanceInfo:
            if i['asset']=='BNB' or i['asset']=='ETH' or i['asset']=='BTC' or i['asset']=='XRP' or i['asset']=='USDT':
                if i['asset']=='USDT':
                    normedvalue = float(i['free'])
                else:
                    for k in self.Normed:
                        if (self.Normed[self.Normed.index(k)][0])[:-4]==i['asset']:
                            normedvalue = float(i['free'])*float(self.Normed[self.Normed.index(k)][1])
                if normedvalue > float(self.Pointer[2]):
                    self.Pointer = [i['asset'], float(i['free']), normedvalue]
                self.SpotWallet[SpotPlace][0] = i['asset']
                self.SpotWallet[SpotPlace][1] = i['free']
                self.SpotWallet[SpotPlace][2] = normedvalue
                SpotPlace += 1
        
    def CompareMarket(self):
        transit = []
        self.winner = ['', 0]
        for j in range(0, (len(self.Normed))):
            transit.append([self.Normed[j][0], round(float(self.NormedLess1[j][1])-float(self.Normed[j][1]), 6)])
        for l in range(0, len(transit)):
            if self.winner[1] > transit[l][1]:
                self.winner = transit[l]

    def GetWinner(self):
        if float(self.winner[1]) < 0:
            return self.winner
        else:
            return ['USDT', -0.0]

    def GetPointer(self):
        # obtenir 'pointer' (actif le + important du portefeuille)
        return self.Pointer

    def GetNormed(self):        
        # obtenir 'normed' (prix du market utilisés pour normer les valeurs du portefeuille)
        return self.Normed

    def GetSpotWallet(self):
        # obtenir les données du portefeuille
        return self.SpotWallet