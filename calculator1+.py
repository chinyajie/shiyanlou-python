def calc(income):
    TAX_BASE = 3500
    INCOME_TAX_TABLE = [
        (80000, 0.45, 13505),
        (55000, 0.35, 5505),
        (9000, 0.25, 1005),
        (4500, 0.2, 555),
        (1500, 0.1, 105),
        (0, 0.03, 0)
    ]

    taxable = income - TAX_BASE
    if taxable <= 0:
        return '0.00'
    for item in INCOME_TAX_TABLE:
        if taxable > item[0]:
            result = taxable * item[1] - item[2]
            return '{:.2f}'.format(result)

def main():
    import sys
    if len(sys.argv) != 2:
        print("Parameter Eroor")
        exit()
    try:
        income = int(sys.argv[1])
    except ValueError:
        print("Parameter Error")
        exit()
    print(calc(income))

if __name__ == '__main__':
    main()
