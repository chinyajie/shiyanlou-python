# -*- coding:utf-8 -*-
import numpy 
import pandas as pd
from pandas import Series
def quarter_volume():
    data = pd.read_csv('apple.csv', header=0)

    print(data)
    print(data['Volume'])
    data_series = Series(numpy.array(data['Volume']), index=pd.to_datetime(data['Date']))
    print(data_series)
    qdata = data_series.resample('Q').sum()
    qdata = qdata.sort_values()
    print(qdata[-2])
    return qdata[-2]


if __name__ == '__main__':
    print(quarter_volume())
