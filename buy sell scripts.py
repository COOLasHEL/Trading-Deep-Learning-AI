import cbpro

data = open('passphrase', 'r').read().splitlines()

public = data[0]
passphrase = data[1]
secret = data[2]

auth_client = cbpro.AuthenticatedClient(public, secret, passphrase)

print(auth_client.get_accounts())
#Buy at certain price limit
print(auth_client.buy(price='10.0', size="0.1", order_type="limit", product_id="ETH-EUR"))
#Sell at current market price
print(auth_client.buy(size="10", order_type="market", product_id="ETH-EUR"))
#Buy at certain price limit
print(auth_client.sell(price="200000.00", size="10", order_type="limit", product_id="BTC-EUR"))
#Sell at current market price
print(auth_client.sell(size="10", order_type="market", product_id='BTC-EUR'))

#buy directly

print(auth_client.place_limit_order(product_id="BTC-EUR", side="buy", price="10.00", size="2"))
print(auth_client.cancel_all(product_id="BTC-EUR"))


import time

sell_price = 30000
sell_amount = 0.3

buy_price = 250000
buy_amount = 0.2

while True:
    price = float(auth_client.get_product_ticker(product_id="BTC-EUR")['price'])
    if price <= buy_price:
        auth_client.buy(size=buy_amount, order_type="market", product_id="BTC-EUR")
    elif price >= sell_price:
        print('selling BTC')
        auth_client.sell(size=sell_amount, order_type="market", product_id="BTC-EUR")
    else:
        print('Nothing...')
    time.sleep(0)










