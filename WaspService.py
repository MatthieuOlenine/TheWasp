import WaspDataAccount
import requests, json, copy

class Service:
    def __init__(self) -> None:
        self.Winner = ['', 0]
        self.Pointer = ['', 0, 0]
        self.Normed = [['', 0], ['', 0], ['', 0], ['', 0]]
        self.NormedLess1 = [['', 0], ['', 0], ['', 0], ['', 0]]
        self.SpotWallet = [['', 0, 0], ['', 0, 0], ['', 0, 0], ['', 0, 0], ['', 0, 0]]
        self.Url = 'https://api.binance.com'        # 'https://api.binance.com' : comte accurate | 'https://testnet.binance.vision' : compte démo
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
        self.Winner = ['', 0]
        for j in range(0, (len(self.Normed))):
            transit.append([self.Normed[j][0], round(float(self.NormedLess1[j][1])-float(self.Normed[j][1]), 6)])
        for l in range(0, len(transit)):
            if self.Winner[1] > transit[l][1]:
                self.Winner = transit[l]

    def ApplyConvert(self, pointerfromabove, winnerfromabove):
        print(round(pointerfromabove[1], 3))
        if not pointerfromabove[0] == winnerfromabove[0]:                               # verifie que le wallet et le winner ne sont pas de l'USDT
            if not pointerfromabove[0] == winnerfromabove[0][:-4]:                      # vérifie que le wallet et le winner ne sont pas identiques
                if pointerfromabove[0] == 'XRP' and winnerfromabove[0][:-4] == 'BTC':
                    self.AccountInstance.SellXrpBtc(round(pointerfromabove[1], 3))
                if pointerfromabove[0] == 'BTC' and winnerfromabove[0][:-4] == 'XRP':
                    self.AccountInstance.BuyXrpBtc(round(pointerfromabove[1], 3))
                if pointerfromabove[0] == 'BNB' and winnerfromabove[0][:-4] == 'BTC':
                    self.AccountInstance.SellBnbBtc(round(pointerfromabove[1], 3))
                if pointerfromabove[0] == 'BTC' and winnerfromabove[0][:-4] == 'BNB':
                    self.AccountInstance.BuyBnbBtc(round(pointerfromabove[1], 3))
                if pointerfromabove[0] == 'XRP' and winnerfromabove[0][:-4] == 'ETH':
                    self.AccountInstance.SellXrpEth(round(pointerfromabove[1], 3))
                if pointerfromabove[0] == 'ETH' and winnerfromabove[0][:-4] == 'XRP':
                    self.AccountInstance.BuyXrpEth(round(pointerfromabove[1], 3))
                if pointerfromabove[0] == 'XRP' and winnerfromabove[0][:-4] == 'BNB':
                    self.AccountInstance.SellXrpBnb(round(pointerfromabove[1], 3))
                if pointerfromabove[0] == 'BNB' and winnerfromabove[0][:-4] == 'XRP':
                    self.AccountInstance.BuyXrpBnb(round(pointerfromabove[1], 3))
                if pointerfromabove[0] == 'BNB' and winnerfromabove[0][:-4] == 'ETH':
                    self.AccountInstance.SellBnbEth(round(pointerfromabove[1], 3))
                if pointerfromabove[0] == 'ETH' and winnerfromabove[0][:-4] == 'BNB':
                    self.AccountInstance.BuyBnbEth(round(pointerfromabove[1], 3))
                if pointerfromabove[0] == 'ETH' and winnerfromabove[0] == 'USDT':
                    self.AccountInstance.SellEthUsdt(round(pointerfromabove[1], 3))
                if pointerfromabove[0] == 'USDT' and winnerfromabove[0][:-4] == 'ETH':
                    self.AccountInstance.BuyEthUsdt(round(pointerfromabove[1], 3))
                if pointerfromabove[0] == 'BTC' and winnerfromabove[0] == 'USDT':
                    self.AccountInstance.SellBtcUsdt(round(pointerfromabove[1], 3))
                if pointerfromabove[0] == 'USDT' and winnerfromabove[0][:-4] == 'BTC':
                    self.AccountInstance.BuyBtcUsdt(round(pointerfromabove[1], 3))
                if pointerfromabove[0] == 'BNB' and winnerfromabove[0] == 'USDT':
                    self.AccountInstance.SellBnbUsdt(round(pointerfromabove[1], 3))
                if pointerfromabove[0] == 'USDT' and winnerfromabove[0][:-4] == 'BNB':
                    self.AccountInstance.BuyBnbUsdt(round(pointerfromabove[1], 3))
                if pointerfromabove[0] == 'XRP' and winnerfromabove[0] == 'USDT':
                    self.AccountInstance.SellXrpUsdt(round(pointerfromabove[1], 3))
                if pointerfromabove[0] == 'USDT' and winnerfromabove[0][:-4] == 'XRP':
                    self.AccountInstance.BuyXrpUsdt(round(pointerfromabove[1], 3))

    def GetWinner(self):
        if float(self.Winner[1]) < 0:
            return self.Winner
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