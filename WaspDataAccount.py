from binance.client import Client
from binance.enums import *

class Account:
    def __init__(self) -> None:
        self.api_key = 'c2e8B1YSb0yfV6JvjqPEWb35WUmrWiSWyJGGgYSVdGgbm3QmAfbvCqvcygOxAfOz'
        self.api_secret = 'UtGQjXSZQEOPEyPJM8Qdza6PicUgqbmXcuR5H6DA1Gs8IgzFqdLqkQ6Ia6i2wAUu'
        self.Client = Client(self.GetApiKey(), self.GetApiSecret())

    def GetApiKey(self):
        return self.api_key
    
    def GetApiSecret(self):
        return self.api_secret
    
    def Login(self):
        account_info = self.Client.get_account()
        return account_info

    def BuyBnbBtc(self, Qty):
        self.Client.create_order(
            symbol = 'BNBBTC',
            side = SIDE_BUY,
            type = ORDER_TYPE_MARKET,
            quantity = Qty,
        )

    def SellBnbBtc(self, Qty):
        self.Client.create_order(
            symbol = 'BNBBTC',
            side = SIDE_SELL,
            type = ORDER_TYPE_MARKET,
            quantity = Qty,
        )

    def BuyXrpEth(self, Qty):
        self.Client.create_order(
            symbol = 'XRPETH',
            side = SIDE_BUY,
            type = ORDER_TYPE_MARKET,
            quantity = Qty,
        )
    
    def SellXrpEth(self, Qty):
        self.Client.create_order(
            symbol = 'XRPETH',
            side = SIDE_SELL,
            type = ORDER_TYPE_MARKET,
            quantity = Qty,
        )

    def BuyXrpBtc(self, Qty):
        self.Client.create_order(
            symbol = 'XRPBTC',
            side = SIDE_BUY,
            type = ORDER_TYPE_MARKET,
            quantity = Qty,
        )

    def SellXrpBtc(self, Qty):
        self.Client.create_order(
            symbol = 'XRPBTC',
            side = SIDE_SELL,
            type = ORDER_TYPE_MARKET,
            quantity = Qty,
        )

    def BuyXrpBnb(self, Qty):
        self.Client.create_order(
            symbol = 'XRPBNB',
            side = SIDE_BUY,
            type = ORDER_TYPE_MARKET,
            quantity = Qty,
        )

    def SellXrpBnb(self, Qty):
        self.Client.create_order(
            symbol = 'XRPBNB',
            side = SIDE_SELL,
            type = ORDER_TYPE_MARKET,
            quantity = Qty,
        )

    def BuyBnbEth(self, Qty):
        self.Client.create_order(
            symbol = 'BNBETH',
            side = SIDE_BUY,
            type = ORDER_TYPE_MARKET,
            quantity = Qty,
        )

    def SellBnbEth(self, Qty):
        self.Client.create_order(
            symbol = 'BNBETH',
            side = SIDE_SELL,
            type = ORDER_TYPE_MARKET,
            quantity = Qty,
        )

    def BuyEthBtc(self, Qty):
        self.Client.create_order(
            symbol = 'ETHBTC',
            side = SIDE_BUY,
            type = ORDER_TYPE_MARKET,
            quantity = Qty,
        ) 

    def SellEthBtc(self, Qty):
        self.Client.create_order(
            symbol = 'ETHBTC',
            side = SIDE_SELL,
            type = ORDER_TYPE_MARKET,
            quantity = Qty,
        )

    def BuyBtcUsdt(self, Qty):
        self.Client.create_order(
            symbol = 'BTCUSDT',
            side = SIDE_BUY,
            type = ORDER_TYPE_MARKET,
            quantity = Qty,
        )

    def SellBtcUsdt(self, Qty):
        self.Client.create_order(
            symbol = 'BTCUSDT',
            side = SIDE_SELL,
            type = ORDER_TYPE_MARKET,
            quantity = Qty,
        )

    def BuyEthUsdt(self, Qty):
        self.Client.create_order(
            symbol = 'ETHUSDT',
            side = SIDE_BUY,
            type = ORDER_TYPE_MARKET,
            quantity = Qty,
        )

    def SellEthUsdt(self, Qty):
        self.Client.create_order(
            symbol = 'ETHUSDT',
            side = SIDE_SELL,
            type = ORDER_TYPE_MARKET,
            quantity = Qty,
        )

    def BuyBnbUsdt(self, Qty):
        self.Client.create_order(
            symbol = 'BNBUSDT',
            side = SIDE_BUY,
            type = ORDER_TYPE_MARKET,
            quantity = Qty,
        )

    def SellBnbUsdt(self, Qty):
        self.Client.create_order(
            symbol = 'BNBUSDT',
            side = SIDE_SELL,
            type = ORDER_TYPE_MARKET,
            quantity = Qty,
        )

    def BuyXrpUsdt(self, Qty):
        self.Client.create_order(
            symbol = 'XRPUSDT',
            side = SIDE_BUY,
            type = ORDER_TYPE_MARKET,
            quantity = Qty,
        )

    def SellXrpUsdt(self, Qty):
        self.Client.create_order(
            symbol = 'XRPUSDT',
            side = SIDE_SELL,
            type = ORDER_TYPE_MARKET,
            quantity = Qty,
        )