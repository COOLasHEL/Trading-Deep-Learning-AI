
# IN THIS SCRIPT I AM JUST PLAYING AROUND WITH DIFFERENT FUNCTIONS



'''
passphrase = 23440303
stop = 0
key = 0
while stop == 0:
    if passphrase >= 1000000: #(above 7digits)
        key = key+3
    else:
        key = key+1
    if key >= 1000000:
        key = key+1
    print(key)
    if key == passphrase:
        stop = 1


print('Key=',key)
'''

#apptempt to reproduce pattern recognition and evolving trading accuracy
###

'''
import random

accuracy = 0
true = 0
false = 0

total_trades = 12232
unsuccessful_trade = 10000


if true == 1:
    accuracy = unsuccessful_trade/total_trades
    accuracy = accuracy*100
    accuracy = 100-accuracy
if false == 1:
    print('accuracy = ',accuracy,'%')
    accuracy2 = accuracy
    while accuracy2 <= 70:
        print('negative percentage, recalulating...')
        unsuccessful_trade = unsuccessful_trade - (random.randint(5,10))
        print(unsuccessful_trade)
    if unsuccessful_trade <= total_trades/2:
        accuracy2 = 71
        accuracy = 100-((unsuccessful_trade/total_trades)*100)

print('new accuracy = ', accuracy, '%')

'''

#code that makes ai retrain if the price prediction accuracy is not in a certain range of the actual price that the ai tried to predict


#for example:

'''
price = 22.33
predicted_price = 24
error_tolerance = 1
retry_status = 0

error = price - predicted_price
if error == 0:
    print('100% accuracy!!!')
elif error < 0:
    error = predicted_price - price

if error > error_tolerance:
    retry_status = 1

if retry_status == 1:
    print('recalculating...')

error_percentage = (error_tolerance/error)*10

if error < error_tolerance:

    print(error, 'price difference', error_percentage, '% accuracy')

'''

# example of a script where the ai learns patter recognition

#function to load chart data + define patterns with certain ranges and shapes that correspond to a certain pattern
#add precision over the time by defining patterns more accurately
# make AI recognize shape on graph or by certain data range ?? - both?
# give images/data with predefined solutions, make AI practice recognizing
# make AI recognize resistance? - zone where price had the most reactions - help to recognize w/m patterns etc...
# try different settings and then let AI adjust them by itself to get more accurate

# !!! JUST A SCRIP TO DECIDE WHAT TO DO BELONGING TO THE PATTERN RECOGNIZED, THERE WILL BE MORE PATTERNS!!!

cup_and_handle = 'cup and handle'
head_and_shoulders = 'head and shoulders'
inverse_cup_and_handle = 'inverse cup and handle'
inverse_head_and_shoulders = 'inverse head and shoulders'
double_top = 'double top'
double_bottom = 'double bottom'
triple_top = 'triple top'
triple_bottom = 'triple bottom'
falling_wedge = 'Falling Wedge'
diamond = 'Diamond'
consolidation = 'Consolidation'
flag = 'Flag'


data = ''
which = ''

output = input('pattern AI recognized')

input1 = output

cup_and_handle = 'cup and handle'
head_and_shoulders = 'head and shoulders'
inverse_cup_and_handle = 'inverse cup and handle'
inverse_head_and_shoulders = 'inverse head and shoulders'
double_top = 'double top'
double_bottom = 'double bottom'
triple_top = 'triple top'
triple_bottom = 'triple bottom'
falling_wedge = 'Falling Wedge'
diamond = 'Diamond'
consolidation = 'Consolidation'
flag = 'Flag'

bullish = 'Buy'
bearish = 'Sell'
neutral = 'Sell'

status = 0

pattern = input1

#while True:


if pattern == triple_bottom:
    pattern = bearish
    which = triple_bottom
    #False


if pattern == double_top:
    pattern = bearish
    which = double_bottom
    #False


if pattern == cup_and_handle:
    pattern = bullish
    which = cup_and_handle
    #False


if pattern == double_bottom:
    pattern = bullish
    which = double_bottom
    #False


if pattern == inverse_cup_and_handle:
    pattern = bearish
    which = inverse_cup_and_handle
    #False


if pattern == inverse_head_and_shoulders:
    pattern = bullish
    which = inverse_head_and_shoulders
    #False


if pattern == falling_wedge:
    pattern = bullish
    which = falling_wedge
    #False

if pattern == diamond:
    pattern = bullish
    which = diamond
    #False


if pattern == consolidation:
    pattern = neutral
    which = consolidation
    #False


if pattern == triple_top:
    pattern = bearish
    which = triple_top
    #False


if pattern == flag:
    pattern = bullish
    which = flag
    #False



if pattern == bullish:

    print(which, ': buy')

if pattern == bearish:
    print(which, ': sell')

