# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import Series,DataFrame
def co2_gdp_plot():
    #阅读文件
    df_climate = pd.read_excel("ClimateChange.xlsx", sheet_name=0)
    df_co2=df_climate[df_climate['Series code'] == "EN.ATM.CO2E.KT"].set_index('Country name').iloc[:,5:27]
    df_gdp=df_climate[df_climate['Series code'] == "NY.GDP.MKTP.CD"].set_index('Country name').iloc[:,5:27]
    co2_fill=df_co2.replace({'..':pd.np.NaN}).fillna(method='ffill',axis=1).fillna(method='bfill',axis=1)
    gdp_fill=df_gdp.replace({'..':pd.np.NaN}).fillna(method='ffill',axis=1).fillna(method='bfill',axis=1)
    co2_sum=pd.DataFrame(co2_fill.sum(axis=1),columns=['CO2 sum'])
    gdp_sum=pd.DataFrame(gdp_fill.sum(axis=1),columns=['GDP sum'])
    norm_fuc=lambda x: (x - np.min(x)) / (np.max(x) - np.min(x))
    co2_norm=co2_sum.apply(norm_fuc)
    gdp_norm=gdp_sum.apply(norm_fuc)
    df_all=co2_norm.join(gdp_norm)
    #作图
    china = list(df_all.loc['China'].values.round(3))
    name_list=['China','United States','United Kingdom','France','Russian Federation']
    loc_list=[]
    for country in name_list:
        loc_list.append(co2_norm.index.get_loc(country))
    short_list=['CHN', 'USA', 'GBR', 'FRA','RUS']
    fig = plt.subplot()
    df_all.plot()
    plt.title('GDP-CO2')
    plt.xlabel('Countries')
    plt.ylabel('Values')
    plt.xticks(loc_list,short_list,rotation=90)
    return fig, china
