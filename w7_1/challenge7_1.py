# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
def co2():


    country_sheet = pd.read_excel("ClimateChange.xlsx", sheetname='Country')
    data_sheet = pd.read_excel("ClimateChange.xlsx", sheetname='Data')
    #series_sheet = pd.read_excel("ClimateChange.xlsx", sheetname='Series')

    #data_sheet = data_sheet.fillna(method='ffill', axis=1).fillna(method='bfill', axis=1)
    #data_sheet.set_index('Country name')

    main_data = data_sheet.merge(country_sheet[['Country code', 'Income group']], on='Country code', how='outer')
    #main_data = pd.merge(data_sheet, country_sheet)
    main_data = main_data.replace('..', np.nan)
    threshNum = len(main_data.columns)-22+1
    print(threshNum)

    main_data = main_data.dropna(axis=0, thresh=threshNum)   # VIP

    #main_data = main_data.fillna(method='ffill', axis=1).fillna(method='bfill', axis=1)

    all = main_data[main_data['Series code'] == 'EN.ATM.CO2E.KT']

    #sum = all[list(range(1990, 2012))].fillna(method='ffill', axis=1).fillna(method='bfill', axis=1).sum(axis=1)
    all['sum'] = all[list(range(1990, 2012))].fillna(method='ffill', axis=1).fillna(method='bfill', axis=1).sum(axis=1)
    all = all[['sum','Country name','Income group']]


    groupdata = all.groupby('Income group')
    result = groupdata.sum()

    result.columns = ['Sum emissions']
    #WRONG result[['Highest emission country', 'Highest emissions']] = all.loc(all.groupby('Income group').idxmax())[['Country name','Sum emissions']]
    #WRONG result[['Lowest emission country', 'Lowest emissions']] = all.loc(all.groupby('Income group').idxmin())[['Country name', 'Sum emissions']]
    # result[['Highest emission country', 'Highest emissions']] = all.groupby('Income group').max()[['Country name','Sum emissions']]
    # result[['Lowest emission country', 'Lowest emissions']] = all.groupby('Income group').min()[['Country name', 'Sum emissions']]

    result[['Highest emission country', 'Highest emissions']] = (  #VIP
        groupdata.apply(lambda x: x.loc[x['sum'].idxmax()])[['Country name', 'sum']]
    )
    result[['Lowest emission country', 'Lowest emissions']] = (
        groupdata.apply(lambda x: x.loc[x['sum'].idxmin()])[['Country name', 'sum']]
    )
    print("hahahahahhahahahhaha----------")
    print(all[all['Country name']=='Turks and Caicos Islands'])
    print(result)
    print(result.index)
    print(result.columns)
    return result




    #return results
co2()