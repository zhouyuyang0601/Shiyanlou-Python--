# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from pandas import DataFrame,Series
from matplotlib import pyplot as plt

def climate_plot():
    # 直接读取 NASA 全球温度变化数据集
    df_temperature = pd.read_excel("GlobalTemperature.xlsx")
    # 传入世界银行气候变化数据集
    df_climate = pd.read_excel("ClimateChange.xlsx", sheet_name='1')
    #EN.ATM.CO2E.KT,EN.ATM.METH.KT.CE,EN.ATM.NOXE.KT.CE,EN.ATM.GHGO.KT.CE,EN.CLC.GHGR.MT.CE 
    greenhouse_list=["EN.ATM.CO2E.KT","EN.ATM.METH.KT.CE","EN.ATM.NOXE.KT.CE","EN.ATM.GHGO.KT.CE","EN.CLC.GHGR.MT.CE"]
    df_greenhouse = df_climate[df_climate.loc[:,'Series code'].isin(greenhouse_list)].set_index('Series code').iloc[:,5:57]
    #gh is short for GreenHouse
    gh_fill=df_greenhouse.replace({'..':pd.np.NaN}).fillna(method='ffill',axis=1).fillna(method='bfill',axis=1).dropna(how='all')
    #groupby labels
    gh_sum=gh_fill.groupby("Series code").sum().sum()
    #Create DataFrame 全球历年温室气体排放总量
    df_gh=DataFrame(gh_sum,columns=['Greenhouse gas sum'])

    #历年陆地平均温度
    #历年陆地-海洋平均温度
    #各季度地面平均温度
    #各季度地面-海洋平均温度

    #TS重采样，'Q','3M,'Y'


  


    '''
    补充代码：
    1. 查看数据文件结构。
    2. 读取数据并对缺失值处理
    3. 对时间序列数据集进行处理并重新采样
    4. 按规定选择数据

    5. 按规定绘图
    '''

    # 务必在绘图前设置子图对象,并返回
    fig = plt.subplot()

    # 返回 fig 对象
    return fig
