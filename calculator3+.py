# /usr/bin/env python3

import sys


class ArgError(Exception):
    pass


class Args:
    def __init__(self, args):
        self.__args = args

    def __parse_cmd(self, arg):
        try:
            value = self.__args[self.__args.index(arg) + 1]
        except (ValueError, IndexError):
            value = None
        return value

    def get_arg(self, arg):
        value = self.__parse_cmd(arg)
        if value is None:
            print("Just test!")
            raise ArgError('not found arg %s' % arg)
        return value


class Calculator:
    TAX_START = 3500
    TAX_TABLE = [
        (80000, 0.45, 13505),
        (55000, 0.35, 5505),
        (9000, 0.25, 1005),
        (4500, 0.2, 555),
        (1500, 0.1, 105),
        (0, 0.03, 0)
    ]

    def __init__(self, file):
        self.__rate, self.__jishu_high, self.__jishu_low = self.__parse_file(file)

    def __parse_file(self, file):
        rate = 0
        jishu_high = 0
        jishu_low = 0
        with open(file) as f:
            for line in f:
                key, value = line.split('=')
                key = key.strip()
                try:
                    value = float(value.strip())
                except ValueError:
                    continue
                if key == 'JiShuL':
                    jishu_low = value
                elif key == 'JiShuH':
                    jishu_high = value
                else:
                    rate += value
        return rate, jishu_high, jishu_low

    def calculate(self, data_item):
        employee_id, income = data_item

        if income < self.__jishu_low:
            shebao = self.__jishu_low * self.__rate
        elif income > self.__jishu_high:
            shebao = self.__jishu_high * self.__rate
        else:
            shebao = self.__rate * income

        taxable = income - shebao - self.TAX_START

        tax = 0
        if taxable > 0:
            for it in self.TAX_TABLE:
                if taxable > it[0]:
                    tax = taxable * it[1] - it[2]
                    break
        final_income = income - shebao - tax

        return "%d,%d,{:.2f},{:.2f},{:.2f}".format(shebao, tax, final_income) % (employee_id, income)


class EmployeeData:
    def __init__(self, file):
        self.__file = file
        self.__data = self.__parse_file()

    def __parse_file(self):
        data = []
        for line in open(self.__file):
            employee_id, income = line.split(',')
            try:
                employee_id = int(employee_id.strip())
                income = int(income.strip())
            except ValueError:
                print("ValueError!")
                exit()
            data.append((employee_id, income))
        return data

    def __iter__(self):
        return iter(self.__data)


class Exporter:
    def __init__(self, file):
        self.__file = file

    def export(self, results):
        content = ''
        for it in results:
            content += it + '\n'
        with open(self.__file, 'w') as f:
            f.write(content)

if __name__ == '__main__':
    args = Args(sys.argv[1:])
    calc = Calculator(args.get_arg('-c'))
    employee_data = EmployeeData(args.get_arg('-d'))
    exporter = Exporter(args.get_arg('-o'))

    results = []
    for item in employee_data:
        result = calc.calculate(item)
        results.append(result)

    exporter.export(results)
