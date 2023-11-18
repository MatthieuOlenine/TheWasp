from binance.client import Client

class Account:
    def __init__(self) -> None:
        self.api_key = 'o9jpkeFk9cszV6WtzZkJCO9MBJDJrQIw1IVESOLVrpZGsDh5Rc3TZkx5udoq6DCe'
        self.api_secret = 'ZQlH4Fa7vJG17L1mmG2SDXjpVrl0TG0RGiKLyGSxGzE0XlInVGuBTxm3EDgjHUHX'

    def GetApiKey(self):
        return self.api_key
    
    def GetApiSecret(self):
        return self.api_secret
    
    def Login(self):
        client = Client(self.GetApiKey(), self.GetApiSecret())
        account_info = client.get_account()
        return account_info

    
    
