import matplotlib.pyplot as plt
import numpy as np
import time
from mpl_toolkits.basemap import Basemap
import matplotlib as mpl
import matplotlib.gridspec as gridspec

def plot_precipitation(df, title=''):
    # define marker style
    red_square = dict(markerfacecolor='r', marker='s')
    font = {'family': 'sans-serif',
        'color':  'black',
        'fontweight': 'semibold',
    }

    #define plot layout
    fig = plt.figure(figsize=(17, 10))
    ax = fig.add_subplot(111)

    #define max and min values for apply highlight
    temp = df[df['day'] == 1]['precipit'].values.ravel()
    minv, maxv = (0, np.sum(temp)), (0, np.sum(temp))
    precipit, days, count = [], [], []

    for x in range(31):
        #get rows of current day
        temp = df[df['day'] == x+1]['precipit'].values.ravel()

        #maybe there are days that didn't have measurements
        if not len(temp):
            continue

        #obtaining precipitation values and quantity of
        # measurements in the logarithmic base
        precipit.append(np.log10(temp))
        count.append(np.log10(len(temp)))
        days.append(x+1)

        #updating variables with max and min precipitation values
        amount = np.sum(temp)
        minv = (x, amount) if amount < minv[1] else minv
        maxv = (x, amount) if amount > maxv[1] else maxv

    #
    bplot = ax.boxplot(precipit, flierprops=red_square,  \
                       patch_artist=True, vert=True, whis=0.75, positions=days)
    ax.set_title(title, fontdict=font)
    ax.plot(days, count, 'r', marker='d', linewidth=1)
    ax.set_ylabel('Total de precipitação por dia $(log_{10})$')
    ax.set_xlabel('Dia do mês')
    ax.grid(b=True, axis='y', which='major')

    colors = ['#FFFFFF' for x in days]

    for x, patch in enumerate(bplot['boxes']):
        if x == minv[0]:
            patch.set_facecolor('#FFD07B')
        elif x == maxv[0]:
            patch.set_facecolor('#098EE8')
        else:
            patch.set_facecolor('#FFFFFF')

    for x in days:
        ax.axvline(x=x, color='gray', alpha=.175)

    ax.legend([bplot['boxes'][minv[0]], \
                  bplot['boxes'][maxv[0]]], \
                 ['Acumulado mínimo', 'Acumulado máximo'], loc='upper right')

    rowsprecipit = ax.twinx()
    rowsprecipit.set_ylabel('Ocorrências $(log_{10})$')

    ltemp = ['Dia {}'.format(x+1) for x in np.arange(30)]
    plt.savefig('../images/results/total.png', dpi=300)
    plt.show()

def plot_year_precipitation(df):
    m2 = df[df['month'] == 2]
    m3 = df[df['month'] == 3]
    m8 = df[df['month'] == 8]
    m9 = df[df['month'] == 9]
    m10 = df[df['month'] == 10]

    red_square = dict(markerfacecolor='r', marker='x')
    font = {'family': 'sans-serif',
            'color': 'black',
            'fontweight': 'semibold',
            }

    # define plot layout
    fig = plt.figure(figsize=(17, 10))
    ax = fig.add_subplot(111)

    data = [
        np.log10(m2['precipit'].values.ravel()),
        np.log10(m3['precipit'].values.ravel()),
        np.log10(m8['precipit'].values.ravel()),
        np.log10(m9['precipit'].values.ravel()),
        np.log10(m10['precipit'].values.ravel()),
    ]
    amount = [
        np.log10(m2['precipit'].count()),
        np.log10(m3['precipit'].count()),
        np.log10(m8['precipit'].count()),
        np.log10(m9['precipit'].count()),
        np.log10(m10['precipit'].count())
    ]

    months = ['Fevereiro', 'Março', 'Agosto', 'Setembro', 'Outubro']
    ax.plot([1, 2, 3, 4, 5], amount, 'r', marker='d', linewidth=1)
    bplot = ax.boxplot(data, flierprops=red_square, \
                       patch_artist=True, vert=True, whis=0.75, positions=[1, 2, 3, 4, 5])
    plt.xticks([1, 2, 3, 4, 5], months)

    plt.savefig('months.png')
    plt.show()

def plot_daily_precipitation(df):
    days = list(df.groupby('day').groups.keys())
    plt.figure(figsize=(17, 8), dpi=100)
    for day in days:
        print('check day ', day)
        data = df[df['day'] == day]
        data = data.groupby(['hour']).agg({'precipit': ['sum']})
        x = list(map(int, data.index.ravel()))
        y = list(map(float, data['precipit']['sum'].values))
        plt.plot(x, y, label='Dia %d'%int(day))
        # print(y)

    plt.grid()
    plt.xlabel('Hora')
    plt.ylabel('Total de precipitaćão (mm/d)')
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    # plt.savefig('day.png')
    plt.show()

def plot_daily_lightning(df):
    days = list(df.groupby('day').groups.keys())
    plt.figure(figsize=(17, 8), dpi=100)
    for day in days:
        print('check day ', day)
        data = df[df['day'] == day]
        data = data.groupby(['hour']).agg({'yyy_xx4': ['sum']})
        x = list(map(int, data.index.ravel()))
        y = list(map(float, data['yyy_xx4']['sum'].values))
        plt.plot(x, y, label='Dia %d' % int(day))
        # print(y)

    plt.grid()
    plt.xlabel('Hora')
    plt.ylabel('Total de precipitaćão (mm/d)')
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    # plt.savefig('day.png')
    plt.show()

def detail(df):
    my_coords = [-3.2, -60.00000000]
    zoom_scale = 2
    font = {
        'fontweight': 'bold'
    }

    bbox = [my_coords[0] - zoom_scale, my_coords[0] + zoom_scale, \
            my_coords[1] - zoom_scale, my_coords[1] + zoom_scale]

    fig = plt.figure(figsize=(20, 8))
    m = Basemap(projection='merc', llcrnrlat=bbox[0], urcrnrlat=bbox[1], \
                llcrnrlon=bbox[2], urcrnrlon=bbox[3], lat_ts=10, resolution='i')

    m.drawcoastlines()
    m.fillcontinents(color='#FAFAFA', lake_color='dodgerblue')

    m.drawparallels(np.arange(bbox[0], bbox[1], (bbox[1] - bbox[0]) / 5), labels=[1, 0, 0, 0])
    m.drawmeridians(np.arange(bbox[2], bbox[3], (bbox[3] - bbox[2]) / 5), labels=[0, 0, 0, 1], rotation=45)
    m.drawmapboundary(fill_color='dodgerblue')

    x, y = m(my_coords[1], my_coords[0])
    plt.title("Raios no mês Setembro", fontdict=font)
    # plt.ylabel('Longitude', labelpad=40)
    # plt.xlabel('Latitude', labelpad=60)

    lights = df[(df['yyy_xx4'] > 0) & (df['yyy_xx5'] > 0)]
    land = np.zeros((241, 241))

    for line in lights[['ind_x', 'ind_y', 'yyy_xx4', 'yyy_xx4']].values:
        # coords = (line[0], line[1])
        x, y = m(line[0], line[1])

        if line[2] + line[3] > 0:
            land[0][1] += 1
        # if line[2] + line[3] < 3:
        #     m.plot(x, y, marker='x', color='gray')
        # elif line[2] + line[3] < 5:
        #     m.plot(x, y, marker='x', color='blue')
        # elif line[2] + line[3] < 7:
        #     m.plot(x, y, marker='x', color='green')
        # elif line[2] + line[3] < 10:
        #     m.plot(x, y, marker='x', color='orange')
        # else:
        #     m.plot(x, y, marker='x', color='red')

        # m.plot(x, y, marker='s', color='b', alpha=0.2)
    m.matshow(land, alpha=.3)
    # cmap = mpl.colors.ListedColormap(['black', 'gray',
    #                                   'yellow', 'orange', 'red'])
    # cmap.set_over('red')
    # cmap.set_under('black')
    # bounds = [1, 3, 5, 10, 20]
    # norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
    # cb3 = mpl.colorbar.ColorbarBase(fig, cmap=cmap,
    #                                 norm=norm,
    #                                 boundaries=[-10] + bounds + [10],
    #                                 extend='both',
    #                                 extendfrac='auto',
    #                                 ticks=bounds,
    #                                 spacing='uniform',
    #                                 orientation='vertical')
    # cb3.set_label('Custom extension lengths, some other units')
    plt.savefig('land.png')
    plt.show()



if __name__ == "__main__":
    try:
        from .preprocessing import *
    except ModuleNotFoundError:
        from preprocessing import *

    MAT_PATH = "../data/full/exp/mat"

    df = pd.read_csv('../data/full/exp/csv/september.csv', sep=',')

    plot_daily_lightning(df)
    # plot_year_precipitation(df)
    # plot_precipitation(df, title='Total de precipitação no meses observados em 2014')



