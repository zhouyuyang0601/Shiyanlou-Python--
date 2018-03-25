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
    df_gh.index=pd.to_datetime(df_gh.index)

    #填充温度数据并且转换为时间戳索引
    temp_fill=df_temperature.fillna(method='ffill',axis=0).fillna(method='bfill',axis=0).dropna(how='all').set_index('Date')
    temp_fill.index=pd.to_datetime(temp_fill.index)
    temp_y_mean=temp_fill.resample('AS').mean()[240:261]
    #历年陆地平均温度
    land_avg_y=temp_y_mean['Land Average Temperature']
    #历年陆地-海洋平均温度
    land_ocean_avg_y=temp_y_mean['Land And Ocean Average Temperature']
    #各季度地面平均温度
    temp_q_mean=temp_fill.resample('Q').mean()
    land_avg_q=temp_q_mean['Land Average Temperature']
    #各季度地面-海洋平均温度
    land_ocean_avg_q=temp_q_mean['Land And Ocean Average Temperature']
    
    #作图
    #图一图二作图前需要归一化

    fig = plt.subplot()
    norm_func=lambda x: (x - np.min(x)) / (np.max(x) - np.min(x))
    #图一
    #绘制 1990 年 - 2010 年间，「全球历年温室气体排放总量」与「历年陆地平均温度」及「历年陆地-海洋平均温度」三者之间的线形图。
    """  
    plot1.columns.get_loc(1990)
    240
    plot1.columns.get_loc(2010)
    260
    """
    fig=plt.figure(figsize=(20, 15))
    ax1=fig.add_subplot(2,2,1)
    ax1.set_xlabel('Years')
    ax1.set_ylabel('Values')
    plot1_land=norm_func(land_avg_y)
    plot1_land.index=plot1_land.index.year
    plot1_land_ocean=norm_func(land_ocean_avg_y)
    plot1_land_ocean.index=plot1_land_ocean.index.year
    plot1_GHG=norm_func(gh_sum)
    plot1=DataFrame([plot1_GHG,plot1_land,plot1_land_ocean]).rename({'Unnamed 0':'Total GHG'}).transpose()
    plot1.plot(ax=ax1)


    #图二 
    ax2=fig.add_subplot(2,2,2)
    ax2.set_xlabel('Years')
    ax2.set_ylabel('Values')

    plot2=plot1
    plot2.plot(ax=ax2,kind='bar')
    #图三
    ax3=fig.add_subplot(2,2,3)
    ax3.set_xlabel('Quaters')
    ax3.set_ylabel('Temperature')

    plot3=DataFrame([land_avg_q,land_ocean_avg_q]).transpose()
    plot3.plot(ax=ax3,kind='area')

    #图四
    ax4=fig.add_subplot(2,2,4)
    ax4.set_xlabel('Values')
    ax4.set_ylabel('Values')
    plot3.plot(ax=ax4,kind='kde')
    # 返回 fig 对象
    return fig
