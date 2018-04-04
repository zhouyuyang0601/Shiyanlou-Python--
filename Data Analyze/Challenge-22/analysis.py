import pandas as pd
import os
def analysis(file_name,user_id):
    try:
        path=os.path.abspath(str(filename))
    except (ValueError,KeyError):
        return 0,0
        break
    data= pd.read_json(path)
    study_time=data[data['user_id']==user_id]['minutes'].sum()
    study_freq=data[data['user_id']==user_id]['minutes'].count()
    return study_freq,study_time

if __name__ == '__main__':
    analysis()



