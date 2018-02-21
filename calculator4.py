# /usr/bin/env python3

import sys
from multiprocessing import Process, Queue
import queue


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


class Calculator(Process):
    TAX_START = 3500
    TAX_TABLE = [
        (80000, 0.45, 13505),
        (55000, 0.35, 5505),
        (9000, 0.25, 1005),
        (4500, 0.2, 555),
        (1500, 0.1, 105),
        (0, 0.03, 0)
    ]

    def __init__(self, file, in_queue, out_queue):
        self.__rate, self.__jishu_high, self.__jishu_low = self.__parse_file(file)
        self.__in_queue = in_queue
        self.__out_queue = out_queue
        super().__init__()

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

    def run(self):
        while True:
            try:
                item = self.__in_queue.get()
            except queue.Empty:
                return
            result = self.calculate(item)
            self.__out_queue.put(result)


class EmployeeData(Process):
    def __init__(self, file, queue):
        self.__file = file
        # self.__data = self.__parse_file()
        self.__queue = queue
        super().__init__()

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

    # def __iter__(self):
    #     return iter(self.__data)

    def run(self):
        for item in self.__parse_file():
            self.__queue.put(item)


class Exporter(Process):
    def __init__(self, file, queue):
        self.__file = open(file, 'a')
        self.__queue = queue
        super().__init__()

    # def export(self, results):
    #     content = ''
    #     for it in results:
    #         content += it + '\n'
    #     with open(self.__file, 'w') as f:
    #         f.write(content)

    def run(self):
        while True:
            try:
                item = self.__queue.get()
            except queue.Empty:
                print("no_item")
                self.__file.close() # VIP
                return
            self.__file.write(item + '\n')
            print("write" + item)


if __name__ == '__main__':
    args = Args(sys.argv[1:])

    q1 = Queue()
    q2 = Queue()

    calc = Calculator(args.get_arg('-c'), q1, q2)
    employee_data = EmployeeData(args.get_arg('-d'), q1)
    exporter = Exporter(args.get_arg('-o'), q2)

    employee_data.start()
    calc.start()
    exporter.start()

    employee_data.join()
    calc.join()
    exporter.join()




