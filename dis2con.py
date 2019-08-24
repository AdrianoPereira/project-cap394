import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

start = time.time()
df = pd.read_csv('./data/full/exp/csv/february.csv')

print('loaded in ', start-time.time())

mat = np.zeros((241, 241))

lat = df['lat'].values.ravel()[:50]
lon = df['lon'].values.ravel()[:50]
indx = df['ind_x'].values.ravel()[:50]
indy = df['ind_y'].values.ravel()[:50]
pre = df['precipit'].values.ravel()[:50]

coords = []
values = []
for a, b, c, d, e in zip(lat, lon, indx, indy, pre):
    temp = (c, d)
    if temp in coords:
        idx = coords.index(temp)
        values[idx] = (b, a, values[idx][2]+e)
    else:
        coords.append(temp)
        values.append((b, a, e))

print(len(values))
x, y, z = [], [], []

# print(values)
for i, j, k in values:
    x.append(i)
    y.append(j)
    z.append(k)

# print(len(x))
# print(len(y))
# print(len(z))

# plt.scatter(x, y, c=z, marker='s')
# plt.show()

print('loaded in ', start-time.time())
