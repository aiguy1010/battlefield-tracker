#!/usr/bin/python3
import requests
import datetime
import json

URL='https://www.g2a.com/marketplace/product/auctions/?id=49383&v=0&url=https%253A%252F%252Fwww.g2a.com%252Fbattlefield-1-origin-cd-key-preorder-global.html'
LOG_FILE='prices.csv'

# Get info on current prices
r = requests.get(URL)
data = r.json()

# Find lowest price
bestPrice = None
bestPriceStr = ''
for listing in data['a']:
    priceStr = data['a'][listing]['f']
    price = float(priceStr[1:])
    if bestPrice == None or price < bestPrice:
        bestPrice = price
        bestPriceStr = priceStr

# Timestamp and write to file
nowStr = datetime.datetime.now().strftime('%x %X')
with open(LOG_FILE, 'a') as f:
    f.write('{}, {}\n'.format(nowStr, bestPriceStr))

# Report to stdout
print( 'Best price at {} was {}'.format(nowStr, bestPriceStr) )
