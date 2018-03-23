# -*- coding: utf-8 -*-
import pandas as pd
def co2():

    # 读取世界银行气候变化数据集
    country_sheet = pd.read_excel("ClimateChange.xlsx", sheetname='Country')
    data_sheet = pd.read_excel("ClimateChange.xlsx", sheetname='Data')
    series_sheet = pd.read_excel("ClimateChange.xlsx", sheetname='Series')


    '''
    补充代码：
    1. 查看数据文件结构。
    2. 将国家和所在的收入群体类别产生关联。
    3. 处理 DataFrame 中的不必要数据和缺失数据。
    3. 尤其是注意这里的缺失值并不是 NaN 的形式。
    4. 将最终返回的 DataFrame 处理成挑战要求的格式 。
    '''



    # 必须返回最终得到的 DataFrame
    return results
