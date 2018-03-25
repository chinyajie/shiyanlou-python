# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# def co2_gdp_plot0():
#     # 读取世界银行气候变化数据集
#     df_climate = pd.read_excel("ClimateChange.xlsx", sheetname='Data')
#
#     '''
#     补充代码：
#     1. 查看数据文件结构。
#     2. 选择 CO2 和 GDP 数据。
#     3. 针对缺失数据进行处理。
#     4. 分国家计算数据总和。
#     5. 归一化数据。
#     6. 绘图。
#     '''
#     # 务必在绘图前子图对象，并返回 fig
#     fig = plt.subplot()
#
#     # 务必返回中国所对应的数据（归一化后，且保留 3 位小数）
#     #china = [CO2数据, GDP数据]
#
#     # 按示例顺序返回 fig 对象，以及中国对应的数据列表
#     #return fig, china

def co2_gdp_plot():


    country_sheet = pd.read_excel("ClimateChange.xlsx", sheetname='Country')
    data_sheet = pd.read_excel("ClimateChange.xlsx", sheetname='Data')

    fig = plt.subplot(111)
    #ax = fig.add_subplot(1, 1, 1)

    # 设置标题
    fig.set_title("GDP-CO2")


    main_data = data_sheet.merge(country_sheet[['Country code', 'Income group']], on='Country code', how='outer')
    main_data = main_data.replace('..', np.nan)


    #main_data = main_data.fillna(method='ffill', axis=1).fillna(method='bfill', axis=1)

    co2all = main_data[main_data['Series code'] == 'EN.ATM.CO2E.KT']
    gdpall = main_data[main_data['Series code'] == 'NY.GDP.MKTP.CD']

    #sum = all[list(range(1990, 2012))].fillna(method='ffill', axis=1).fillna(method='bfill', axis=1).sum(axis=1)
    co2all['sum'] = co2all[list(range(1990, 2012))].fillna(method='ffill', axis=1).fillna(method='bfill',
                                                                                          axis=1).replace(np.nan,
                                                                                                          0).sum(axis=1)
    co2all = co2all[['sum', 'Country code']]

    gdpall['sum'] = gdpall[list(range(1990, 2012))].fillna(method='ffill', axis=1).fillna(method='bfill',
                                                                                          axis=1).replace(np.nan,
                                                                                                          0).sum(axis=1)
    gdpall = gdpall.replace(np.nan, 0)
    gdpall['sum'] = gdpall[list(range(1990, 2012))].fillna(method='ffill', axis=1).fillna(method='bfill', axis=1).sum(axis=1)
    gdpall = gdpall[['sum', 'Country code']]

    # major_ticks = co2all['Country name']
    # fig.set_xticks(major_ticks)
    a = list(co2all['Country code'])
    # abak = list()
    # for item in a:
    #     if item in  ['CHN', 'USA', 'GBR', 'FRA','RUS']:
    #         abak.append(item)
    #     else:
    #         abak.append('')

    #plt.xticks(range(len(a)), abak, rotation=90, fontsize=5)

    fig.set_xticks([a.index('CHN'), a.index('USA'), a.index('GBR'), a.index('FRA'), a.index('RUS')])
    fig.set_xticklabels(['CHN', 'USA', 'GBR', 'FRA','RUS'], rotation=90 )

    # 设置 X, Y 轴 标签
    fig.set_xlabel("Countries")
    fig.set_ylabel("Values")

    x = range(len(co2all))
    y = co2all['sum']

    y = y.apply(lambda x: (x-min(y))/(max(y)-min(y)))

    yy = gdpall['sum']
    yy = yy.apply(lambda x: (x - min(yy)) / (max(yy) - min(yy)))

    fig.plot(x, y, label="CO2-SUM")
    fig.plot(x, yy, label="GDP-SUM")
    fig.legend()
    #print(list(co2all['Country name']))yy



    y = list(y)
    yy = list(yy)
    china = ['%.3f' % y[a.index('CHN')], '%.3f' % yy[a.index('CHN')]]
    print(china)
    plt.show()
    return fig, china

co2_gdp_plot()