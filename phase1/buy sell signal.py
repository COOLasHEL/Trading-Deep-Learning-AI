import cbpro
import time
# Script to get tradingview script signals via email? or other way
#We will be using buy sell v 3.0 by nick kenens on Link-Eur
# 82.67 % winrate on 1hr chart , 0.5 % fees with 100 eur buys


data = open('passphrase', 'r').read().splitlines()

public = data[0]
passphrase = data[1]
secret = data[2]

auth_client = cbpro.AuthenticatedClient(public, secret, passphrase)

SMS = 'Tradingview Signal Says Buy!'

if SMS == 'Tradingview Signal Says Buy!':
    SMS = 'Buy'

if SMS == 'Buy':
    buy_amount = 6.5  # = to 94.445 €, we will add more as we have more capital
    print('buying  ', buy_amount, 'LINK-EUR')
    auth_client.buy(size=buy_amount, order_type="market", product_id="LINK-EUR")


SMS = 'Tradingview Signal Says Buy!'
if SMS == 'Tradingview Signal Says Buy!':
    SMS = 'Buy'

if SMS == 'Buy':
    sell_amount = 6.5  # = to 94.445 €, we will add more as we have more capital
    print('selling ', sell_amount, 'LINK-EUR')
    auth_client.sell(size=sell_amount, order_type="market", product_id="LINK-EUR")



