# -*- coding: utf-8 -*-
import pandas as pd

name_list=[]
sum_list=[]
highest_name=[]
highest_ems=[]
lowest_name=[]
lowest_ems=[]

def co2():
'''
    补充代码：
    1. 查看数据文件结构。
    2. 将国家和所在的收入群体类别产生关联。
    3. 处理 DataFrame 中的不必要数据和缺失数据。
    3. 尤其是注意这里的缺失值并不是 NaN 的形式。
    4. 将最终返回的 DataFrame 处理成挑战要求的格式 。
'''
    # 读取世界银行气候变化数据集
    df_climate = pd.read_excel("ClimateChange.xlsx", sheetname=0)
    df_country = pd.read_excel("ClimateChange.xlsx", sheetname=1)
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

    test=country_co2.groupby('Income group')
    for name,income_group in test:
        print(name,end='   ')
        print(income_group['CO2 sum emission'].sum())
    """
    High income: OECD       222798900.271
    High income: nonOECD    12849934.403
    Low income              4828276.561
    Lower middle income     51508409.157
    Upper middle income     171410713.709
    """
    for name,income_group in test:
        name_list.append(name)
        sum_list.append(income_group['CO2 sum emission'].sum())
        highest_name.append(income_group['CO2 sum emission'].idxmax())
        highest_ems.append(income_group['CO2 sum emission'].max())
        lowest_name.append(income_group['CO2 sum emission'].idxmin())
        lowest_ems.append(income_group['CO2 sum emission'].min())
    column_name=['Sum emissions','Highest emission country','Highest emissions','Lowest emission country','Lowest emissions']
    results=DataFrame(list(ip(sum_list,highest_name,highest_ems,lowest_ems,lowest_name)),columns=column_name,index=name_list)

    # 必须返回最终得到的 DataFrame
    return results
