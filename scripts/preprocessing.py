import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def load_datasets(dir):
    """Read one or more files as dataframe.
    dir: files directory
    """

    path_files = [os.path.join(dir, path) for path in os.listdir(dir)]
    df = [pd.read_csv(file, sep='\s+') for file in path_files]
    df = pd.concat(df, sort=False)
    df = df.rename(str.lower, axis='columns')

    return df

def save_dataframe_by_month(df):
    import time
    start = time.time()

    df.to_csv('total.csv', sep=',', index=False)
    print('dataset saved')

    february = df[df['month'] == 2]
    february.to_csv('february.csv', sep=',', index=False)
    print('february saved')

    march = df[df['month'] == 3]
    march.to_csv('march.csv', sep=',', index=False)
    print('march saved')

    august = df[df['month'] == 8]
    august.to_csv('august.csv', sep=',', index=False)
    print('august saved')

    september = df[df['month'] == 9]
    september.to_csv('september.csv', sep=',', index=False)
    print('september saved')

    october = df[df['month'] == 10]
    october.to_csv('october.csv', sep=',', index=False)
    print('october saved')

    end = time.time()
    print('Final in ', end-start)



def load_dataset(dir):
    """Read one file as dataframe.
    dir: files directory
    """
    df = pd.read_csv(dir, sep=',')
    df = df.rename(str.lower, axis='columns')

    return df


def aggregate_by_day(df):
    df = df.groupby(['day']).agg({
        'yyyyy_xx1': ['sum'],
        'yyyyy_xx2': ['sum'],
        'yyyyyyy_xx3': ['sum'],
        'yyy_xx4': ['sum'],
        'yyy_xx5': ['sum'],
        'vil': ['max']
    })

    return df

if __name__ == "__main__":
    MAT_PATH = "../data/full/exp/mat"
    matdf = load_datasets(MAT_PATH)
    print(matdf)



