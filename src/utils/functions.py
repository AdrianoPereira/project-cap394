import pandas as pd
import numpy as np
import matplotlib.pyplot as np
import os


def load_dataset(dir):
    """Read one or more files as dataframe.
    dir: files directory
    """
    path_files = [os.path.join(dir, path) for path in os.listdir(dir)[500:550]]
    df = [pd.read_csv(file, sep='\s+') for file in path_files]
    df = pd.concat(df, sort=False)
    df = df.rename(str.lower, axis='columns')

    return df


def split_train_test(X, y, test_size=0.2):
    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=test_size)

    return x_train, x_test, y_train, y_test


def compute_decision_tree(X, y, test_size=0.2):
    from sklearn.tree import DecisionTreeRegressor

    x_train, x_test, y_train, y_test = split_train_test(X, y, test_size)

    regressor = DecisionTreeRegressor()
    regressor.fit(x_train, y_train)

    return regressor, x_test, y_test


def run_decision_tree(dataframe):
    X, y = dataframe[['reflect', 'precipit']], dataframe['cxe']

    model, x_test, y_test = compute_decision_tree(X, y)



