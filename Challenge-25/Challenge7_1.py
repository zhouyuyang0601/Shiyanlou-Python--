# -*- coding: utf-8 -*-
import pandas as pd
from pandas import DataFrame
name_list=[]
sum_list=[]
highest_name=[]
highest_ems=[]
lowest_name=[]
lowest_ems=[]

def co2():

    # 读取世界银行气候变化数据集
    df_climate = pd.read_excel("ClimateChange.xlsx", sheet_name=0)
    df_country = pd.read_excel("ClimateChange.xlsx", sheet_name=1)
    """
    #数据清洗
    #有缺失值的年份数据进行填充，挑战规定使用近邻数据填充
    #挑战不统计原始数据全部缺失的国家，也就是排放量最低的国家对应的排放量数值不会为 0
    """
    #读取CO2年份并累加
    #读取含有二氧化碳数据的年份，并且
    co2_data=df_climate[df_climate['Series code'] == "EN.ATM.CO2E.KT"].set_index('Country name').iloc[:,5:24].drop_duplicates(keep=False)
    co2_fill=co2_data.replace({'..':pd.np.NaN}).fillna(method='ffill',axis=1).fillna(method='bfill',axis=1)
    co2=pd.DataFrame(co2_fill.sum(axis=1),columns=['CO2 sum emission'])

    #根据索引合并country
    country=df_country.iloc[:,[1,4]].set_index('Country name')
    country_co2=co2.join(country,how='inner')
    
    #求和
    col1=country_co2.groupby('Income group').sum()
    df_co2=country_co2.groupby('Income group')
    """
    for name,income_group in test:
        print(name,end='   ')
        print(income_group['CO2 sum emission'].sum())
    
    High income: OECD       222798900.271
    High income: nonOECD    12849934.403
    Low income              4828276.561
    Lower middle income     51508409.157
    Upper middle income     171410713.709
    """
    for name,income_group in df_co2:
        name_list.append(name)
        sum_list.append(income_group['CO2 sum emission'].sum())
        highest_name.append(income_group['CO2 sum emission'].idxmax())
        highest_ems.append(income_group['CO2 sum emission'].max())
        lowest_name.append(income_group['CO2 sum emission'].idxmin())
        lowest_ems.append(income_group['CO2 sum emission'].min())
    column_name=['Sum emissions','Highest emission country','Highest emissions','Lowest emission country','Lowest emissions']
    results=DataFrame(list(zip(sum_list,highest_name,highest_ems,lowest_ems,lowest_name)),columns=column_name,index=name_list)

    # 必须返回最终得到的 DataFrame
    return results
