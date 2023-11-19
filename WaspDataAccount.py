from binance.client import Client

class Account:
    def __init__(self) -> None:
        self.api_key = 'o9jpkeFk9cszV6WtzZkJCO9MBJDJrQIw1IVESOLVrpZGsDh5Rc3TZkx5udoq6DCe'
        self.api_secret = 'ZQlH4Fa7vJG17L1mmG2SDXjpVrl0TG0RGiKLyGSxGzE0XlInVGuBTxm3EDgjHUHX'
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
            side = 'SIDE_BUY',
            type = 'ORDER_TYPE_MARKET',
            quantity = Qty,
        )

    def SellBnbBtc(self, Qty):
        self.Client.create_order(
            symbol = 'BNBBTC',
            side = 'SIDE_SELL',
            type = 'ORDER_TYPE_MARKET',
            quantity = Qty,
        )

    def BuyXrpEth(self, Qty):
        self.Client.create_order(
            symbol = 'XRPETH',
            side = 'SIDE_BUY',
            type = 'ORDER_TYPE_MARKET',
            quantity = Qty,
        )
    
    def SellXrpEth(self, Qty):
        self.Client.create_order(
            symbol = 'XRPETH',
            side = 'SIDE_SELL',
            type = 'ORDER_TYPE_MARKET',
            quantity = Qty,
        )

    def BuyXrpBtc(self, Qty):
        self.Client.create_order(
            symbol = 'XRPBTC',
            side = 'SIDE_BUY',
            type = 'ORDER_TYPE_MARKET',
            quantity = Qty,
        )

    def SellXrpBtc(self, Qty):
        self.Client.create_order(
            symbol = 'XRPBTC',
            side = 'SIDE_SELL',
            type = 'ORDER_TYPE_MARKET',
            quantity = Qty,
        )

    def BuyXrpBnb(self, Qty):
        self.Client.create_order(
            symbol = 'XRPBNB',
            side = 'SIDE_BUY',
            type = 'ORDER_TYPE_MARKET',
            quantity = Qty,
        )

    def SellXrpBnb(self, Qty):
        self.Client.create_order(
            symbol = 'XRPBNB',
            side = 'SIDE_SELL',
            type = 'ORDER_TYPE_MARKET',
            quantity = Qty,
        )

    def BuyBnbEth(self, Qty):
        self.Client.create_order(
            symbol = 'BNBETH',
            side = 'SIDE_BUY',
            type = 'ORDER_TYPE_MARKET',
            quantity = Qty,
        )

    def SellBnbEth(self, Qty):
        self.Client.create_order(
            symbol = 'BNBETH',
            side = 'SIDE_SELL',
            type = 'ORDER_TYPE_MARKET',
            quantity = Qty,
        )

    def BuyEthBtc(self, Qty):
        self.Client.create_order(
            symbol = 'ETHBTC',
            side = 'SIDE_BUY',
            type = 'ORDER_TYPE_MARKET',
            quantity = Qty,
        ) 

    def SellEthBtc(self, Qty):
        self.Client.create_order(
            symbol = 'ETHBTC',
            side = 'SIDE_SELL',
            type = 'ORDER_TYPE_MARKET',
            quantity = Qty,
        )