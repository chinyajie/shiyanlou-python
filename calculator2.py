#! /usr/bin/env python3
import sys

def calculate(pid, wage):
    money = 0
    try:
        money = int(wage)
        pid = int(pid)
    except:
        print("Parameter Error")
        return

    tex = 0.00
    basic = money * (1 - 0.165)
    money = basic - 3500
    if money <= 0:
        print(str(pid)+":"+str(format(basic - tex, ".2f")))
        return
    else:
        tex += money * 0.03

    money -= 1500
    if money < 0:
        print(str(pid)+":"+str(format(basic - tex, ".2f")))
        return
    else:
        tex += money * 0.07

    money -= 3000
    if money < 0:
        print(str(pid)+":"+str(format(basic - tex, ".2f")))
        return
    else:
        tex += money * 0.10

    money -= 4500
    if money < 0:
        print(str(pid)+":"+str(format(basic - tex, ".2f")))
        return
    else:
        tex += money * 0.05

    money -= 26000
    if money < 0:
        print(str(pid)+":"+str(format(basic - tex, ".2f")))
        return
    else:
        tex += money * 0.05

    money -= 20000
    if money < 0:
        print(str(pid)+":"+str(format(basic - tex, ".2f")))
        return
    else:
        tex += money * 0.05

    money -= 25000
    if money < 0:
        print(str(pid)+":"+str(format(basic - tex, ".2f")))
        return
    else:
        tex += money * 0.05

    print(str(pid)+":"+str(format(basic - tex, ".2f")))
    return

if __name__ == '__main__':
    for arg in sys.argv[1:]:
        it = arg.split(':')
        calculate(it[0], it[1])

