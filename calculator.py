#! /usr/bin/env python3
import sys

money = 0
try:
    money = int(sys.argv[1])
except:
    print("Parameter Error")
    exit()

tex = 0.00
money -= 3500
if money < 0:
    print(format(tex, ".2f"))
    exit()
else:
    tex += money * 0.03

money -= 1500
if money < 0:
    print(format(tex, ".2f"))
    exit()
else:
    tex += money * 0.07

money -= 3000
if money < 0:
    print(format(tex, ".2f"))
    exit()
else:
    tex += money * 0.10

money -= 4500
if money < 0:
    print(format(tex, ".2f"))
    exit()
else:
    tex += money * 0.05

money -= 26000
if money < 0:
    print(format(tex, ".2f"))
    exit()
else:
    tex += money * 0.05

money -= 20000
if money < 0:
    print(format(tex, ".2f"))
    exit()
else:
    tex += money * 0.05

money -= 25000
if money < 0:
    print(format(tex, ".2f"))
    exit()
else:
    tex += money * 0.05

print(format(tex, ".2f"))
exit()
