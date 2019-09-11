import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


if __name__ == "__main__":
    # df = pd.read_csv('./data/full/exp/csv/february.csv')
    # df2 = pd.read_csv('./data/full/exp/csv/march.csv')
    # df3 = pd.read_csv('./data/full/exp/csv/august.csv')
    df4 = pd.read_csv('./data/full/exp/csv/september.csv')
    # df5 = pd.read_csv('./data/full/exp/csv/october.csv')

    s1 = df4[df4['yyyyyyy_xx3'] > 0]
    # s1 = df[df['ttyyyxx2'] > 0]
    # s1 = df[df['ttyyyxx1'] > 0]
    # s1 = df[df['ttyyyxx1'] > 0]
    # s1 = df[df['ttyyyxx1'] > 0]

    print(s1)