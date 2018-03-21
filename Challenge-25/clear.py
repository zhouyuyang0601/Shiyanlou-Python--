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

    df_climate = pd.read_excel("ClimateChange.xlsx", sheet_name=0)
    df_country = pd.read_excel("ClimateChange.xlsx", sheet_name=1)
    co2_data=df_climate[df_climate['Series code'] == "EN.ATM.CO2E.KT"].set_index('Country name').iloc[:,5:27].drop_duplicates(keep=False)
    co2_fill=co2_data.replace({'..':pd.np.NaN}).fillna(method='ffill',axis=1).fillna(method='bfill',axis=1)
    co2=pd.DataFrame(co2_fill.sum(axis=1),columns=['CO2 sum emission'])

    country=df_country.iloc[:,[1,4]].set_index('Country name')
    country_co2=co2.join(country,how='inner')

    df_co2=country_co2.groupby('Income group')
   
    for name,income_group in df_co2:
        name_list.append(name)
        sum_list.append(income_group['CO2 sum emission'].sum())
        highest_name.append(income_group['CO2 sum emission'].idxmax())
        highest_ems.append(income_group['CO2 sum emission'].max())
        lowest_name.append(income_group['CO2 sum emission'].idxmin())
        lowest_ems.append(income_group['CO2 sum emission'].min())
    column_name=['Sum emissions','Highest emission country','Highest emissions','Lowest emission country','Lowest emissions']
    results=DataFrame(list(zip(sum_list,highest_name,highest_ems,lowest_name,lowest_ems)),columns=column_name,index=name_list)
    results.index.name='Income group'
    return results
