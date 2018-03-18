import pandas as pd
import numpy as np
import os
from pandas import Series,DataFrame

def quarter_volume()
    path=os.path.abspath('apple.csv')
    data=pd.read_csv(path)
    data['Date']=pd.to_datetime(data['Date'])
    ts=pd.Series(list(data['Volume']),index= data['Date'])
    ts_quarter=ts.resample('Q').sum().sort_values(ascending=False)
    return ts_quarter[1]


    
