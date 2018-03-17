import pandas as pd
from matplotlib import pyplot as plt
import os

def data_plot():
    path=os.path.abspath('user_study.json')
    data= pd.read_json(path)
    df=data[['user_id','minutes']].groupby('user_id').sum()
    fig=plt.figure()
    ax=fig.add_subplot(1,1,1)
    df.plot()
    plt.show()
    return ax
