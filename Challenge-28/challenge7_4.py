# -*- coding: utf-8 -*-
import pandas as pd
from matplotlib import pyplot as plt

def Temperature():
    # 读取所需数据文件

    '''
    补充代码：
    1. 查看数据文件结构。
    2. 读取数据并对缺失值处理
    3. 对时间序列数据集进行处理并重新采样
    4. 整理数据
    5. 使用 scikit-learn 预测
    6. 将预测结果按列表返回
    '''

    # 将预测结果按 2011-2017 年份顺序，并保留 3 位小数后以列表形成储存
    UpperPredict = [0.521,0.532,0.559,0.578,0.623,0.691] #示例列表
    MedianPredict = []
    LowerPredict = []

    # 按高、中、低依次返回预测结果列表
    return UpperPredict, MedianPredict, LowerPredict
