#!/usr/bin/python3
from matplotlib import pyplot as plt
from datetime import datetime
from sys import argv

LOG_FILE='prices.csv'

TIMES = []
PRICES = []

with open( LOG_FILE, 'r' ) as f:
    for line in f:
        timeStr, priceStr = line.split(', ')
        TIMES.append( datetime.strptime(timeStr, '%x %X') )
        PRICES.append( float(priceStr[1:]) )

plt.title('Battefield 1 on G2A')
plt.ylabel('Min. Price ($)')
plt.xlabel('Date and Time')
plt.plot( TIMES, PRICES, marker='o', color='g' )

if len(argv) == 1:
    plt.show()
else:
    saveFile = argv[1]
    plt.savefig(saveFile, bbox_inches='tight')
