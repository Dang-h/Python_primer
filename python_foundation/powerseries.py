#!/usr/bin/env python3
x = float(input("Enter the value of x: "))
n = term = num = 1
result = 1.0
while n <= 100:
    term *= x / n
    print("term= {:.2f}".format(term))
    result += term
    print("result= {:.2f}".format(result))
    n += 1
    print("n=",n)
    if term < 0.0001:
        break
print("No of Times= {} and Sum= {:.2f}".format(n, result))
