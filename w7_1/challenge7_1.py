# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
def co2():

    # 读取世界银行气候变化数据集
    country_sheet = pd.read_excel("ClimateChange.xlsx", sheetname='Country')
    data_sheet = pd.read_excel("ClimateChange.xlsx", sheetname='Data')
    series_sheet = pd.read_excel("ClimateChange.xlsx", sheetname='Series')

    data_sheet.fillna(method='ffill', axis=1).fillna(method='bfill', axis=1)
    #data_sheet.set_index('Country name')

    main_data = pd.merge(data_sheet, country_sheet)
    main_data = main_data.replace({'..': 0})
    #main_data.replace({'n/a': 0})

    all = main_data[main_data['Series code']=='EN.ATM.CO2E.KT'][['Country name','Country code','Income group',1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011]]
    #num = all.drop('Country code',1);

    #all.set_index('Country name')
    #num = num.replace({'..': '0'})
    sum = all.sum(axis=1)
    all = all[['Country name','Income group']]
    all['Sum emissions'] = sum
    all = all.replace(0.00000,np.nan)
    all = all.dropna(axis=0, how='any')
    result = all.groupby('Income group').sum()
    #all = pd.merge(all[['Country code','Income group']], sum)
    result[['Highest emission country', 'Highest emissions']] = all.groupby('Income group').max()[['Country name','Sum emissions']]
    result[['Lowest emission country', 'Lowest emissions']] = all.groupby('Income group').max()[
        ['Country name', 'Sum emissions']]
    print(all)
    print(result)
    return result



    '''
    补充代码：
    1. 查看数据文件结构。
    2. 将国家和所在的收入群体类别产生关联。
    3. 处理 DataFrame 中的不必要数据和缺失数据。
    3. 尤其是注意这里的缺失值并不是 NaN 的形式。
    4. 将最终返回的 DataFrame 处理成挑战要求的格式 。
    '''



    # 必须返回最终得到的 DataFrame
    #return results
#co2()