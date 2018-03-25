# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def co2_gdp_plot():
    country_sheet = pd.read_excel("ClimateChange.xlsx", sheetname='Country')
    data_sheet = pd.read_excel("ClimateChange.xlsx", sheetname='Data')

    fig = plt.subplot(111)

    # 设置标题
    fig.set_title("GDP-CO2")


    main_data = data_sheet.merge(country_sheet[['Country code', 'Income group']], on='Country code', how='outer')
    main_data = main_data.replace('..', np.nan)

    co2all = main_data[main_data['Series code'] == 'EN.ATM.CO2E.KT']
    gdpall = main_data[main_data['Series code'] == 'NY.GDP.MKTP.CD']

    #sum = all[list(range(1990, 2012))].fillna(method='ffill', axis=1).fillna(method='bfill', axis=1).sum(axis=1)

    co2all['sum'] = co2all[list(range(1990, 2012))].fillna(method='ffill', axis=1).fillna(method='bfill', axis=1).replace(np.nan, 0).sum(axis=1)
    co2all = co2all[['sum','Country code']]

    gdpall['sum'] = gdpall[list(range(1990, 2012))].fillna(method='ffill', axis=1).fillna(method='bfill', axis=1).replace(np.nan, 0).sum(axis=1)
    gdpall = gdpall[['sum', 'Country code']]

    a = list(co2all['Country code'])
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

    china = ['%.3f' % list(y)[a.index('CHN')], '%.3f' % list(yy)[a.index('CHN')]]
    print(china)
    plt.show()
    return fig, china

co2_gdp_plot()