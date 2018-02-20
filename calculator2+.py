# /usr/bin/etc python3
def calc(income, pid):
    TAX_BASE = 3500
    INSURE_RATE = 0.165
    INCOME_TAX_TABLE = [
        (80000, 0.45, 13505),
        (55000, 0.35, 5505),
        (9000, 0.25, 1005),
        (4500, 0.2, 555),
        (1500, 0.1, 105),
        (0, 0.03, 0)
    ]
    taxable = income * (1 - INSURE_RATE)
    taxable -= TAX_BASE
    if taxable <= 0:
        return pid + ':' + '{:.2f}'.format(taxable + TAX_BASE)
    for item in INCOME_TAX_TABLE:
        if taxable > item[0]:
            tax = taxable * item[1] - item[2]
            return '{}:{:.2f}'.format(pid, taxable + TAX_BASE - tax)

def main():
    import sys
    if len(sys.argv) < 2:
        print("Parameter Eroor")
        exit()
    for item in sys.argv[1:]:
        try:
            income = int(item.split(':')[1])
        except ValueError:
            print("Parameter Error")
            exit()
        pid = item.split(':')[0]
        print(calc(income, pid))

if __name__ == '__main__':
    main()
