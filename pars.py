import requests

url = 'https://www.nicehash.com/profitability-calculator/-bitmain-antminer-s17e-(64th)?selCurr=RUB&elCost='+ x + '&devices=1&utm_source=referral&utm_medium=widget&utm_campaign=profitability_calculator'
x = '35'
r = requests.get(url)
r.text