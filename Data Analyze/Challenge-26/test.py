# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import Series,DataFrame
def co2_gdp_plot():
    # 读取世界银行气候变化数据集
    df_climate = pd.read_excel("ClimateChange.xlsx", sheet_name=0)
    df_co2=df_climate[df_climate['Series code'] == "EN.ATM.CO2E.KT"].set_index('Country name').iloc[:,5:27]
    df_gdp=df_climate[df_climate['Series code'] == "NY.GDP.MKTP.CD"].set_index('Country name').iloc[:,5:27]
    #填充
    co2_data=df_co2.replace({'..':pd.np.NaN}).fillna(method='ffill',axis=1).fillna(method='bfill',axis=1)
    gdp_data=df_gdp.replace({'..':pd.np.NaN}).fillna(method='ffill',axis=1).fillna(method='bfill',axis=1)
    #归一化
    norm_fuc=lambda x: (x - np.min(x)) / (np.max(x) - np.min(x))
    co2_norm=co2_data.apply(norm_fuc,axis=1)
    gdp_norm=gdp_data.apply(norm_fuc,axis=1)
    #绘图
    # 务必在绘图前子图对象，并返回 fig
    fig = plt.subplot()

    # 务必返回中国所对应的数据（归一化后，且保留 3 位小数）
    china = [co2_norm.loc['China'].round(3),gdp_norm.loc['China'].round(3)]

    # 按示例顺序返回 fig 对象，以及中国对应的数据列表
    return fig, china
