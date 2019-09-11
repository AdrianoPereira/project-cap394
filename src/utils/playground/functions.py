import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib import gridspec


def read_data(dir):
    """Read one or more files as dataframe.
    dir: files directory
    """
    path_files = [os.path.join(dir, path) for path in os.listdir(dir)]
    df = [pd.read_csv(file, sep='\s+') for file in path_files]
    df = pd.concat(df, sort=False)
    df = df.rename(str.lower, axis='columns')

    return df


def aggregate_data(df, groupby, *aggregateby):
    """Aggregate dataframe.

    df: dataframe to aggregate.
    groupby: a string or list with column that will be the group.
    *aggregateby: (optional) dictionary with values that will be grouped.

    return an dataframe aggregated.
    """
    if not aggregateby:
        aggregated = df.groupby(groupby).agg({
            'reflect': ['min', 'mean', 'max'],
            'precipit': ['min', 'mean', 'max'],
            'yyyyy_xx1': ['sum'],
            'yyyyy_xx2': ['sum'],
            'yyyyyyy_xx3': ['sum'],
            'yyy_xx4': ['sum'],
            'yyy_xx5': ['sum'],
        })
    else:
        aggregateby = aggregateby[0]
        aggregated = df.groupby(groupby).agg(aggregateby)

    return aggregated


if __name__ == "__main__":
    PATH = '../../data/full/exp'

    df = read_data(PATH)
    ag = {'reflect': ['min', 'mean'] }
    aggregated = aggregate_data(df, ['month'])

    fig = plt.figure(figsize=(15, 8))
    gs = gridspec.GridSpec(2, 3)

    months = ['Fev', 'Mar', 'Ago', 'Set', 'Out']
    min_reflect = aggregated.reflect['min'].to_list()
    mean_reflect = aggregated.reflect['mean'].to_list()
    max_reflect = aggregated.reflect['max'].to_list()
    min_precipit = aggregated.precipit['min'].to_list()
    mean_precipit = aggregated.precipit['mean'].to_list()
    max_precipit = aggregated.precipit['max'].to_list()
    total_light1 = aggregated.yyyyy_xx1['sum'] + aggregated.yyyyy_xx2['sum']
    total_light1 = total_light1.to_list()
    total_light2 = aggregated.yyyyyyy_xx3['sum']
    total_light2 = total_light2.to_list()
    total_light3 = aggregated.yyy_xx4['sum'] + aggregated.yyy_xx5['sum']
    total_light3 = total_light3.to_list()

    ax1 = fig.add_subplot(gs[0, 0])
    ax1.set_title('Refletividade')
    ax1.set_xlabel('Mês')
    ax1.set_ylabel('Refletividade (dBZ)')
    ax1.plot(months, min_reflect, 'go--', color='r', label='Mínima')
    ax1.plot(months, mean_reflect, 'go--', color='g', label='Média')
    ax1.plot(months, max_reflect, 'go--', color='b', label='Máxima')
    ax1.legend()
    ax1.grid()

    ax2 = fig.add_subplot(gs[0, 1])
    ax2.set_title('Precipitação')
    ax2.set_xlabel('Mês')
    ax2.set_ylabel('Precipitação (mm/h)')
    ax2.plot(months, min_precipit, 'go--', color='r', label='Mínima')
    ax2.plot(months, mean_precipit, 'go--', color='g', label='Média')
    ax2.plot(months, max_precipit, 'go--', color='b', label='Máxima')
    ax2.legend()
    ax2.grid()

    ax3 = fig.add_subplot(gs[0, 2])
    ax3.set_title('Total raios')
    ax3.set_xlabel('Mês')
    ax3.set_ylabel('Incidências')
    ax3.plot(months, total_light1, 'go--', color='b', label='Rede GLD360')
    ax3.grid()
    ax3.set_title('Total raios')
    ax3.set_xlabel('Mês')
    ax3.set_ylabel('Incidências')
    ax3.plot(months, total_light2, 'go--', color='r', label='Rede STARNET')
    ax3.grid()
    ax3.set_title('Total raios')
    ax3.set_xlabel('Mês')
    ax3.set_ylabel('Incidências')
    ax3.plot(months, total_light3, 'go--', color='g', label='Rede LINET')
    ax3.grid()
    ax3.legend()

    plt.show()