#!/usr/bin/env python3
while True:
    n = int(input("Please enter an Integer: "))
    if n < 0:
        continue
    elif n == 0:
        break
    print("Squara is ", n ** 2)
print("Bye")
