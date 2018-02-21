# /usr/bin/env python3

import sys
from multiprocessing import Process, Queue
import queue
from getopt import getopt, GetoptError
import configparser
from datetime import datetime


class ArgError(Exception):
    pass


class Args:
    def __init__(self, args):
        self.__args = self.__options(args)

    def __options(self, args):
        try:
            opts, obj = getopt(args, 'hC:c:d:o:', ['help'])
            #opts, _ = getopt(sys.argv[1:], 'hC:c:d:o:', ['help'])
        except GetoptError:
            print('Parameter Error')
            exit()
        options = dict(opts)
        if len(options) == 1 and ('-h' in options or '--help' in options):
            print('Usage: calculator.py -C cityname -c configfile -d userdata -o resultdata')
            exit()
        return options

    def __get_arg(self, arg):
        value = self.__args.get(arg)
        if value is None and arg != '-C':
            raise ArgError('not found arg %s' % arg)
        return value

    @property
    def city(self):
        return self.__get_arg('-C')

    @property
    def config_path(self):
        return self.__get_arg('-c')

    @property
    def userdata_path(self):
        return self.__get_arg('-d')

    @property
    def export_path(self):
        return self.__get_arg('-o')


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

    def __init__(self, file, city, in_queue, out_queue):
        self.__in_queue = in_queue
        self.__out_queue = out_queue
        self.__file = file
        self.__city = city
        self.config = self.__read_config()
        super().__init__()

    def __read_config(self):
        config = configparser.ConfigParser()
        config.read(self.__file)
        if self.__city and self.__city.upper() in config.sections():
            return config[args.city.upper()]
        else:
            return config['DEFAULT']


    def _get_config(self, name):
        try:
            return float(self.config[name])
        except (ValueError, KeyError):
            print('Parameter Error')
            exit()


    @property
    def social_insurance_baseline_low(self):
        return self._get_config('JiShuL')


    @property
    def social_insurance_baseline_high(self):
        return self._get_config('JiShuH')


    @property
    def social_insurance_total_rate(self):
        return sum([
            self._get_config('YangLao'),
            self._get_config('YiLiao'),
            self._get_config('ShiYe'),
            self._get_config('GongShang'),
            self._get_config('ShengYu'),
            self._get_config('GongJiJin')
        ])

    def calculate(self, data_item):
        employee_id, income = data_item

        if income < self.social_insurance_baseline_low:
            shebao = self.social_insurance_baseline_low * self.social_insurance_total_rate
        elif income > self.social_insurance_baseline_high:
            shebao = self.social_insurance_baseline_high * self.social_insurance_total_rate
        else:
            shebao = self.social_insurance_total_rate * income

        taxable = income - shebao - self.TAX_START

        tax = 0
        if taxable > 0:
            for it in self.TAX_TABLE:
                if taxable > it[0]:
                    tax = taxable * it[1] - it[2]
                    break
        final_income = income - shebao - tax

        return "%d,%d,{:.2f},{:.2f},{:.2f},%s".format(shebao, tax, final_income) \
               % (employee_id, income, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    def run(self):
        while True:
            try:
                item = self.__in_queue.get(timeout=1)
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
        self.__file = open(file, 'w')
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
                item = self.__queue.get(timeout=1)
            except queue.Empty:
                #print("no_item")
                self.__file.close() # VIP
                return
            self.__file.write(item + '\n')
            #print("write" + item)


if __name__ == '__main__':
    args = Args(sys.argv[1:])

    q1 = Queue()
    q2 = Queue()


    employee_data = EmployeeData(args.userdata_path, q1)
    calc = Calculator(args.config_path, args.city, q1, q2)
    exporter = Exporter(args.export_path, q2)

    employee_data.start()
    calc.start()
    exporter.start()

    employee_data.join()
    calc.join()
    exporter.join()




