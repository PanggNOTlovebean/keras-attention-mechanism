import pandas as pd
import numpy as np


def make_timeseries_data():
    
    train_test_split=0.7
    timesteps=128

    data=pd.read_csv('./examples/sh.000001.csv')
    data.set_index('Date',inplace=True)
    data=data['2010':]
    split_position=int(len(data)*train_test_split)
    print(data)

    data_set=[]
    for i in range(len(data)):
        if(i>=timesteps):
            step_input=[]
            for j in np.arange(i-128,i):
                feature=[]
                for column in ['open','close','high','low','pctChg','volume','amount','turn']:
                    feature.append(data.iloc[i][column])
                step_input.append(feature)
            data_set.append(step_input)
            print(np.array(data_set).shape)
    print(data_set.shape)

def main():
    make_timeseries_data()
    return

if __name__ == '__main__':
    main()