# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from pandas import DataFrame,Series
from matplotlib import pyplot as plt
from sklearn.metrics import mean_absolute_error
from sklearn import linear_model
from sklearn.cross_validation import train_test_split

def Temperature():
    # 读取所需数据文件
    df_temp=pd.read_csv('GlobalSurfaceTemperature.csv').set_index('Year')
    #GHG排放总量，包括No2,CH4,CO2
    df_GHG=pd.read_csv('GreenhouseGas.csv').set_index('Year')
    #二氧化碳浓度，单位为ppm
    df_co2=pd.read_csv('CO2ppm.csv').set_index('Year')
    df_co2.columns=['co2PPM']
    """
    三段数据的时间开始节点不一样
    GHG的开始是从1960
    CO2是从1980
    温度是从1850
    统一选取1980作为起点，预测2011-2017年的温度
    """
    #合并
    df_feature=pd.concat([df_GHG,df_co2],axis=1)
    df_feature.index=pd.to_datetime(df_feature.index.astype(str))
    #补齐缺失值
    df_feature=df_feature.fillna(method='ffill').fillna(method='bfill')
    #提取出预测对象
    df_temp.index=pd.to_datetime(df_temp.index.astype(str))
    med=df_temp.iloc[:,0]
    upp=df_temp.iloc[:,1]
    low=df_temp.iloc[:,2]
    #合并训练集
    feature_train=df_feature['1970-1-1':'2010-1-1']
    #提取预测集
    feature_predict=df_feature['2010-1-1':]

    #使用linear model进行预测med
    med_model = linear_model.LinearRegression()
    #历史数据拟合预测med
    med_model.fit(feature_train,med['1970-1-1':'2010-1-1'])
    MedianPredict=np.around(med_model.predict(feature_predict),decimals=3)

    #Upp
    upp_model = linear_model.LinearRegression()
    #历史数据拟合预测upp
    upp_model.fit(feature_train,upp['1970-1-1':'2010-1-1'])
    UpperPredict=np.around(upp_model.predict(feature_predict),decimals=3)
    
    #Low
    low_model = linear_model.LinearRegression()
    #历史数据拟合预测med
    low_model.fit(feature_train,low['1970-1-1':'2010-1-1'])
    LowerPredict=np.around(low_model.predict(feature_predict),decimals=3)


    # 按高、中、低依次返回预测结果列表
    return list(UpperPredict), list(MedianPredict), list(LowerPredict)
