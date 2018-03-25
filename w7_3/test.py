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

    all = data_sheet[data_sheet['Series code'] == 'EN.ATM.CO2E.KT' or data_sheet['Series code'] == 'EN.ATM.METH.KT.CE'
                or data_sheet['Series code'] == 'EN.ATM.NOXE.KT.CE' or data_sheet['Series code'] == 'EN.ATM.GHGO.KT.CE'
                or data_sheet['Series code'] == 'EN.CLC.GHGR.MT.CE']

    # sum = all[list(range(1990, 2012))].fillna(method='ffill', axis=1).fillna(method='bfill', axis=1).sum(axis=1)
    all = all[list(range(1990, 2012))].fillna(method='ffill', axis=1).fillna(method='bfill', axis=1)
    all = all.sum(axis=0)
    print(type(all))


    '''
    补充代码：
    1. 查看数据文件结构。
    2. 读取数据并对缺失值处理
    3. 对时间序列数据集进行处理并重新采样
    4. 按规定选择数据
    5. 按规定绘图
    '''

    # 务必在绘图前设置子图对象，并返回
    #fig = plt.subplot()

    # 返回 fig 对象
    #return fig

climate_plot()