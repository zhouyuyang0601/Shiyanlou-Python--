import pandas as pd
data=pd.read_excel('ClimateChange.xlsx',sheet_name=['Data','Country','Series']

)
type(data)
data['AZE']
data.first_five()
data
climate_data=pd.read_excel('ClimateChange.xlsx',sheet_name=0)
type(climate_data)
climate_data.descripe()
climate_data.describe()
cliamte_data.dim()
climate_data.dim()
dim(climate_data)
df.climate=pd.read_excel('ClimateChange.xlsx',sheet_name=0)
df_climate=pd.read_excel('ClimateChange.xlsx',sheet_name=0)
df_country=pd.read_excel('ClimateChange.xlsx',sheet_name=1)
df_country.describe()
df_climate.describe()
test=df_climate[df_climate['Series code'] == "EN.ATM.CO2E.KT"]
test
sum=test.loc['1990':'2008'].apply(sum(),axis=1)
sum=test.loc['1990':'2008'].sum(axis=1)
sum
sum=test.loc['1990':'2008']
sum.descirbe()
sum.describe()
test.describe()
 df_co2=df_climate[df_climate['Series code'] == "EN.ATM.CO2E.KT"]
df_co2.describe()
test=df_co2[df.co2['Country Name','1990':'2011']]
test=df_co2[df_co2['Country Name','1990':'2011']]
 co2_data=df_co2[df_co2['1990':'2011']]
 co2_data=df_co2[df_co2.loc['1990':'2011']]
co2_data.descirbe
co2_data.descirbe()
co2_data.describe()
co2_data
co2_data=df_co2[df_co2.columns['1990':'2011']]
df = DataFrame(np.random.randn(4, 4), index=['a', 'b', 'c', 'd'], columns=['A', 'B', 'C', 'D'])
from np import DataFrame
from pandas import DataFrame
df = DataFrame(np.random.randn(4, 4), index=['a', 'b', 'c', 'd'], columns=['A', 'B', 'C', 'D'])
import numpy as np
df = DataFrame(np.random.randn(4, 4), index=['a', 'b', 'c', 'd'], columns=['A', 'B', 'C', 'D'])
df
df[:,['A':'D']

]
df[:,['A','D']]
df[,['A','D']]
df.loc[:,['A','D']]
df.loc[:,['A':'D']]
df.ix[:,0:3]
df.ix[:,0:2]
df.iloc[:,0:3]
df.iloc[:,'A':'C']
df_co2
df_co2.iloc[:,7]
df_co2.iloc[:,6]
df_co2.iloc[:,29]
df_co2.iloc[:,28]
df_co2.iloc[:,27]
df_co2.iloc[:,25]
df_co2.iloc[:,24]
df_co2.iloc[:,7]
co2_data=df_co2.iloc[:,7:24]
co2_data
test=co2_data.sum(axis=1)
test
test=co2_data.apply(sum.axis=1)
test=co2_data.apply(sum(),axis=1)
df_climate[df_climate['Series code'] == "EN.ATM.CO2E.KT"].iloc[:,7:24]
test=df_climate[df_climate['Series code'] == "EN.ATM.CO2E.KT"].iloc[:,6:28]
test
co2_data=df_climate[df_climate['Series code'] == "EN.ATM.CO2E.KT"].iloc[:,6:28]
co2_data
co2_data.sum(axis=1)
co2_data.sum()
df
df.sum()
df.sum(axis=1)
test.add(co2_data,fill_value=0)
co2_data.to_json()
co2_data.to_csv('C:\Code\Shiyanlou-Python--\Challenge-25\co2.csv')
co2_data.replace({'..':0})
co2_data
co2_data=co2_data.replace({'..':0})
co2_data=df_climate[df_climate['Series code'] == "EN.ATM.CO2E.KT"].iloc[:,6:28].replace({'..':0})
co2_data
co2_data=df_climate[df_climate['Series code'] == "EN.ATM.CO2E.KT"].iloc[:,6:28].replace({'..':NaN})
co2_data=df_climate[df_climate['Series code'] == "EN.ATM.CO2E.KT"].iloc[:,6:28].replace({'..':'NaN'})
co2_data.dropna(axia=0,how='all')
co2_data.dropna(axis=0,how='all')
co2_data.drop_duplicate()
co2_data.drop_duplicates()
co2_data.drop_duplicates(axis=0)
test=df_climate[df_climate['Series code'] == "EN.ATM.CO2E.KT"].iloc[:,6:28]
test.describe()
pd.dims(test)
test
test_1=test.drop_duplicates()
test_1
test_1.to_csv('C:\Code\Shiyanlou-Python--\Challenge-25\1.csv')
test_1.to_csv('C:\Code\Shiyanlou-Python--\Challenge-25\\1.csv')
co2_data=df_climate[df_climate['Series code'] == "EN.ATM.CO2E.KT"].iloc[:,6:25].drop_duplicates()
co2_data
co2_data.to_csv('C:\Code\Shiyanlou-Python--\Challenge-25\\co2.csv')
test=co2_data
test.equals(co2_data)
test.drop('..')
test.drop_duplicates(keep='False')
test.drop_duplicates(keep=False)
test.drop('1534')
test.drop(['1534'])
test.drop([1534])
test.to_csv('C:\\1.csv')
test.to_csv('C:\1.csv')
test.to_csv('C:\\1.csv')
test.to_csv('C:\code\\1.csv')
co2_data=df_climate[df_climate['Series code'] == "EN.ATM.CO2E.KT"].iloc[:,6:25].drop_duplicates(keep=False)
co2_data.to_csv('C:\Code\Shiyanlou-Python--\Challenge-25\\co2.csv')
co2_data=df_climate[df_climate['Series code'] == "EN.ATM.CO2E.KT"].iloc[:,[2,6:25].drop_duplicates(keep=False)

]
co2_data=df_climate[df_climate['Series code'] == "EN.ATM.CO2E.KT"].iloc[:,[2,6:25]].drop_duplicates(keep=False)
co2_data=df_climate[df_climate['Series code'] == "EN.ATM.CO2E.KT"].iloc[:,(2,6:25]).drop_duplicates(keep=False)
co2_data=df_climate[df_climate['Series code'] == "EN.ATM.CO2E.KT"].iloc[:,(2,6:25)].drop_duplicates(keep=False)
co2_data=df_climate[df_climate['Series code'] == "EN.ATM.CO2E.KT"].set_index('country name').iloc[:,6:25]
co2_data=df_climate[df_climate['Series code'] == "EN.ATM.CO2E.KT"].set_index('Country name').iloc[:,6:25]
co2_data
co2_data=df_climate[df_climate['Series code'] == "EN.ATM.CO2E.KT"].iloc[:,5:24].drop_duplicates(keep=False)
co2_data
co2_data=df_climate[df_climate['Series code'] == "EN.ATM.CO2E.KT"].iloc[:,5:25].drop_duplicates(keep=False)
co2_data
co2_data=df_climate[df_climate['Series code'] == "EN.ATM.CO2E.KT"].set_index('Country name').iloc[:,4:24].drop_duplicates(keep=False)
co2_data
co2_data=df_climate[df_climate['Series code'] == "EN.ATM.CO2E.KT"].set_index('Country name').iloc[:,5:24].drop_duplicates(keep=False)
co2_data
co2_data.to_csv('C:\Code\Shiyanlou-Python--\Challenge-25\\co2.csv')
co2_nan=co2_data.replace({'..':NaN})
co2_nan=co2_data.replace({'..':pd.np.NaN})
co2_fill=co2_data.replace({'..':pd.np.Nan}).fillna(method='ffill',axis=1).fillna(method='bfill',axis=1)
co2_fill=co2_data.replace({'..':pd.np.NaN}).fillna(method='ffill',axis=1).fillna(method='bfill',axis=1)
co2_fill
co2_sum=co2_fill.sum(axis=1)
co2_sum
df_country
country=df_country.iloc[,1,4]
country=df_country.iloc[:,1,4]
country=df_country.iloc[:,[1,4]]
country
country=df_country[:,[1,4]].set_index('Country name')
country=df_country.iloc[:,[1,4]].set_index('Country name')
country
co2=co2_fill
co2=co2_sum
pandas.concat([co2,country])
import pandas
pandas.concat([co2,country])
country
co2
type(co2)
type(country)
pandas.join([co2,country])
co2.join(country)
country.join(co2)
co2.set_index('Sum submission')
type(co2_sum)
co2=pd.DataFrame(co2_sum)
co2
co2=pd.DataFrame(co2_sum,index='CO2 sum submission')
co2=pd.DataFrame(co2_sum,index=['CO2 sum submission'])
co2
co2=pd.DataFrame(co2_sum,columns=['CO2 sum submission'])
co2
pandas.concat([country,co2])
co2
country
%hist -f history.py
