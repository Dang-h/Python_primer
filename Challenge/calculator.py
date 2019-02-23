#!/usr/bin/env python3

import sys

salary = sys.argv[1]

try:
    money = int(salary)
except:
    print("Paramenter Error")
    exit()
if money < 5000:
    tax = 0
else:
    tax_amount = money - 5000
    if tax_amount < 3000:
        tax = tax_amount * 0.03 - 0
    elif tax_amount >= 3000 and tax_amount < 12000:
        tax = tax_amount * 0.1 - 210
    elif tax_amount >= 12000 and tax_amount < 25000:
        tax = tax_amount * 0.2 - 1410
    elif tax_amount >= 25000 and tax_amount < 35000:
        tax = tax_amount * 0.25 - 2660
    elif tax_amount >= 35000 and tax_amount < 55000:
        tax = tax_amount * 0.3 - 4410
    elif tax_amount >= 55000 and tax_amount < 80000:
        tax = tax_amount * 0.35 - 7160
    elif tax_amount >= 80000:
        tax = tax_amount * 0.45 - 15160
print("{:.2f}".format(tax)) 
