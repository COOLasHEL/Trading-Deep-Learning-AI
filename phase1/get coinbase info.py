
import cbpro


public_client = cbpro.PublicClient()

result = public_client.get_currencies()
time = public_client.get_time()
print('AVAILABLE PRODUCTS:')
print()
#for row in result:
    #print(row['id'])



print('Time:', time)

#Get specific info
print('!! add -USD/-EUR/-USDT behind product name !!')
product = 'LINK-EUR'

info = public_client.get_product_order_book(product)
ticker = public_client.get_product_ticker(product)
stats = public_client.get_product_24hr_stats(product)
trades = public_client.get_product_trades(product)

print('Product info1 of', product, ':', info)
print('Product info2 of', product, ':', ticker)
print('24hr stats of', product, ':', stats)
print()

while True:
    print(next(trades))

