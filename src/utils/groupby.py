import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import math

PATH = '../../data/lite/mat'
path_files = [os.path.join(PATH, path) for path in os.listdir(PATH)]

df = [pd.read_csv(file, sep='\s+') for file in path_files]
df = pd.concat(df, sort=False)
df = df.rename(str.lower, axis='columns')

mfev = df.loc[df['month'] == 2]
mmar = df.loc[df['month'] == 3]
maug = df.loc[df['month'] == 8]
msep = df.loc[df['month'] == 9]
moct = df.loc[df['month'] == 10]

def _extractdf(df):
    ans = {}
    for i, row in df.iterrows():
        month, day = row.month, row.day
        hour, minute = row.hour, row.minute
        lat, lon = row.lat, row.lon

        if row.yyyyy_xx1 > 0 or row.yyyyy_xx2 > 0:  #sensor 1 detect
            if not ans.get(hour):
                ans[hour] = {}
            if not ans[hour].get(minute):
                ans[hour][minute] = {'total': 0, 'sensor': 1}

            ans[hour][minute]['total'] += 1     
        if row.yyyyyyy_xx3 > 0: #sensor 1 detect
            if not ans.get(hour):
                ans[hour] = {}
            if not ans[hour].get(minute):
                ans[hour][minute] = {'total': 0, 'sensor': 2}

            ans[hour][minute]['total'] += 1
        if row.yyy_xx4 > 0 or row.yyy_xx5: #sensor 1 detect
            if not ans.get(hour):
                ans[hour] = {}
            if not ans[hour].get(minute):
                ans[hour][minute] = {'total': 0, 'sensor': 3}

            ans[hour][minute]['total'] += 1
    return ans

def extractdf(df):
    ans = {}
    for i, row in df.iterrows():
        month, day = row.month, row.day
        hour, minute = row.hour, row.minute
        lat, lon = row.lat, row.lon

        if row.yyyyy_xx1 > 0 or row.yyyyy_xx2 > 0:  #sensor 1 detect
            if not ans.get(hour):
                ans[hour] = {}
            if not ans[hour].get('sensor1'):
                ans[hour]['sensor1'] = 0

            ans[hour]['sensor1'] += 1
        if row.yyyyyyy_xx3 > 0: #sensor 1 detect
            if not ans.get(hour):
                ans[hour] = {}
            if not ans[hour].get('sensor2'):
                ans[hour]['sensor2'] = 0

            ans[hour]['sensor2'] += 1
        if row.yyy_xx4 > 0 or row.yyy_xx5: #sensor 1 detect
            if not ans.get(hour):
                ans[hour] = {}
            if not ans[hour].get('sensor3'):
                ans[hour]['sensor3'] = 0

            ans[hour]['sensor3'] += 1
    
    return ans
    
def plot(data):
    print('plots: ', (data.keys()))
    keys = data.keys()
    rows, cols = math.ceil(len(keys)/2), 2
    fig, axs = plt.subplots(nrows=rows, ncols=cols, figsize=(10, 12))


    ii, jj = 0, 0
    for key in keys: #hours
        sensors = {}
        for k in data[key].keys(): #sensors
            sensors[k] = data[key][k]
        values = [int(x) for x in sensors.values()]
        labels = [str(x) for x in [*sensors]]

        axs[ii, jj].set_title('{} hrs'.format(int(key)))
        axs[ii, jj].pie(
            x=values,
            labels=labels,
            autopct='%1.1f%%'
        )
        jj += 1
        if jj >= cols:
            jj = 0
            ii += 1
    fig.suptitle('Total Lightning by Hour in September 2014')
    
    axs[ii, jj].set_visible(False)

    plt.savefig('../assets/lightnigbyhour.png', dpi=300)



data = extractdf(msep)
plot(data)

print(len(data.keys()))


