import matplotlib.pyplot as plt
import numpy as np
import time

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


if __name__ == "__main__":
    try:
        from .preprocessing import *
    except ModuleNotFoundError:
        from preprocessing import *

    MAT_PATH = "../data/full/exp/mat"

    df = pd.read_csv('../data/full/exp/csv/total.csv', sep=',')

    plot_year_precipitation(df)
    # plot_precipitation(df, title='Total de precipitação no meses observados em 2014')



