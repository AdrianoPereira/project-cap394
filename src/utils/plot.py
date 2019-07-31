import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import pandas as pd
import numpy as np
import os

def plot_lightning(data):
    lights = {'x': [], 'y': []}
    for i, row in data.iterrows():
        if row.yyyyy_xx1 > 0 or row.yyyyy_xx2 > 0 or row.yyyyyyy_xx3 > 0:
            lights['x'].append(row.lon)
            lights['y'].append(row.lat)
    print(len(lights['x']))
    return lights

def plot_map(data):
    vegetation = np.fromfile('./vegetacao.bin', dtype='float32')
    vegetation = np.reshape(vegetation, (241, 241))
    lat = np.array(pd.read_csv('./lat.csv', dtype='float32', header=None))
    lon = np.array(pd.read_csv('./lon.csv', dtype='float32', header=None))


    my_coords = [-3.2, -58.9990]
    zoom_scale = 1

    bbox = [my_coords[0] - zoom_scale, my_coords[0] + zoom_scale, \
            my_coords[1] - zoom_scale, my_coords[1] + zoom_scale]

    plt.figure(figsize=(15, 5))

    m = Basemap(projection='merc', llcrnrlat=bbox[0], urcrnrlat=bbox[1], \
                llcrnrlon=bbox[2], urcrnrlon=bbox[3], lat_ts=10, resolution='i')

    m.drawcoastlines()
    m.fillcontinents(color='#FAFAFA', lake_color='dodgerblue')

    m.drawparallels(np.arange(bbox[0], bbox[1], (bbox[1] - bbox[0]) / 5), labels=[1, 0, 0, 0])
    m.drawmeridians(np.arange(bbox[2], bbox[3], (bbox[3] - bbox[2]) / 5), labels=[0, 0, 0, 1], rotation=45)
    m.drawmapboundary(fill_color='dodgerblue')

    lights = plot_lightning(data)
    for i in range(len(lights['x'])):
        coords = (lights['y'][i], lights['x'][i])
        x, y = m(coords[1], coords[0])
        m.plot(x, y, marker='x', color='r')

    # for i in range(241):
    #     for j in range(241):
    #         coords = (lon[i][j], lat[i][j])
    #         x, y = m(coords[1], coords[0])
    #         m.plot(x, y, marker='x', color='b')

    plt.title("Lightning in 01 September")
    plt.ylabel('Longitude', labelpad=40)
    plt.xlabel('Latitude', labelpad=60)

    plt.show()


if __name__ == "__main__":
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

    plot_map(msep)




