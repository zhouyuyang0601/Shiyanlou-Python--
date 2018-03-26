# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from pandas import DataFrame,Series
from matplotlib import pyplot as plt

def climate_plot():
    
    df_temperature = pd.read_excel("GlobalTemperature.xlsx")
    
    df_climate = pd.read_excel("ClimateChange.xlsx", sheet_name=1)
    
    greenhouse_list=["EN.ATM.CO2E.KT","EN.ATM.METH.KT.CE","EN.ATM.NOXE.KT.CE","EN.ATM.GHGO.KT.CE","EN.CLC.GHGR.MT.CE"]
    df_greenhouse = df_climate[df_climate.loc[:,'Series code'].isin(greenhouse_list)].set_index('Series code').iloc[:,5:57]
    
    gh_fill=df_greenhouse.replace({'..':pd.np.NaN}).fillna(method='ffill',axis=1).fillna(method='bfill',axis=1).dropna(how='all')
   
    gh_sum=gh_fill.groupby("Series code").sum().sum()
    
    df_gh=DataFrame(gh_sum,columns=['Greenhouse gas sum'])
    df_gh.index=pd.to_datetime(df_gh.index)

    
    temp_fill=df_temperature.fillna(method='ffill',axis=0).fillna(method='bfill',axis=0).dropna(how='all').set_index('Date')
    temp_fill.index=pd.to_datetime(temp_fill.index)
    temp_y_mean=temp_fill.resample('AS').mean()[240:261]
   
    land_avg_y=temp_y_mean['Land Average Temperature']
    
    land_ocean_avg_y=temp_y_mean['Land And Ocean Average Temperature']
    
    temp_q_mean=temp_fill.resample('Q').mean()
    land_avg_q=temp_q_mean['Land Average Temperature']
    
    land_ocean_avg_q=temp_q_mean['Land And Ocean Average Temperature']
    
    
    fig = plt.subplot()
    norm_func=lambda x: (x - np.min(x)) / (np.max(x) - np.min(x))
    
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


    
    ax2=fig.add_subplot(2,2,2)
    ax2.set_xlabel('Years')
    ax2.set_ylabel('Values')

    plot2=plot1
    plot2.plot(ax=ax2,kind='bar')
    
    ax3=fig.add_subplot(2,2,3)
    ax3.set_xlabel('Quaters')
    ax3.set_ylabel('Temperature')

    plot3=DataFrame([land_avg_q,land_ocean_avg_q]).transpose()
    plot3.plot(ax=ax3,kind='area')

   
    ax4=fig.add_subplot(2,2,4)
    ax4.set_xlabel('Values')
    ax4.set_ylabel('Values')
    plot3.plot(ax=ax4,kind='kde')
   
    return fig
