# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

def climate_plot():
    # 直接读取 NASA 全球温度变化数据集
    df_temperature = pd.read_excel("GlobalTemperature.xlsx")

    # 传入世界银行气候变化数据集
    country_sheet = pd.read_excel("ClimateChange.xlsx", sheetname='Country')
    data_sheet = pd.read_excel("ClimateChange.xlsx", sheetname='Data')

    data_sheet = data_sheet.replace('..', np.nan)
    threshNum = len(data_sheet.columns) - 22 + 1

    main_data = data_sheet.dropna(axis=0, thresh=threshNum)  # VIP

    # main_data = main_data.fillna(method='ffill', axis=1).fillna(method='bfill', axis=1)

    green_gas = pd.concat([
        data_sheet[data_sheet['Series code'] == 'EN.ATM.CO2E.KT' ],
        data_sheet[data_sheet['Series code'] == 'EN.ATM.METH.KT.CE'],
        data_sheet[data_sheet['Series code'] == 'EN.ATM.NOXE.KT.CE'],
        data_sheet[data_sheet['Series code'] == 'EN.ATM.GHGO.KT.CE'],
        data_sheet[data_sheet['Series code'] == 'EN.CLC.GHGR.MT.CE']])

    # sum = all[list(range(1990, 2012))].fillna(method='ffill', axis=1).fillna(method='bfill', axis=1).sum(axis=1)
    green_gas = green_gas[list(range(1990, 2012))].fillna(method='ffill', axis=1).fillna(method='bfill', axis=1)
    green_gas = green_gas.sum(axis=0)
    print(green_gas)


    fig = plt.figure()

    ax1 = fig.add_subplot(2, 2, 1)
    ax2 = fig.add_subplot(2, 2, 2)
    ax3 = fig.add_subplot(2, 2, 3)
    ax3 = fig.add_subplot(2, 2, 4)

    x = range(len(green_gas))
    y = green_gas

    y = y.apply(lambda x: (x - min(y)) / (max(y) - min(y)))


    ax1.plot(x, y, label="CO2-SUM")

    ax1.legend()
    plt.show()



climate_plot()