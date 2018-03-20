# -*- coding: utf-8 -*-
import pandas as pd
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
    co2=pd.DataFrame(co2_fill.sum(axis=1),columns=['CO2 sum submission'])

    #根据索引合并country
    country=df_country.iloc[:,[1,4]].set_index('Country name')
    pandas.concat([country,co2])
    

    # 必须返回最终得到的 DataFrame
    return results
