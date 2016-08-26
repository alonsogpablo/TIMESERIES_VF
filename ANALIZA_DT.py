import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns



ts=pd.read_csv('/Users/Pablo/Desktop/DT_3G_ERI.csv',parse_dates=[0])

data= ts.pivot(index='fecha', columns='nodo', values='sum_dt')


data.fillna(0,inplace=True)

for column in data:
    if data[column].mean()==0: del data[column]
    elif data[column].mean()>50000: del data[column]
    elif data[column].mean()<100: del data[column]


print data.mean().sort_values(ascending=False)

