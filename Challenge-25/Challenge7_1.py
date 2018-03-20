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
    #数据清洗
    #有缺失值的年份数据进行填充，挑战规定使用近邻数据填充
    test=df_climate[df_climate['Series code'] == "EN.ATM.CO2E.KT"]

    sum=test.iloc['1990':'2008']
    test['Country Code','Country name','Series Code','Sum']
    

    # 必须返回最终得到的 DataFrame
    return results
