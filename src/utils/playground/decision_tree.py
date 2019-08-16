import os
import pandas as pd # data processing
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import rasterio
from rasterio.plot import show
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn import tree
from IPython.display import Image
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO
import pydotplus
from sklearn import metrics
import graphviz
import preprocessing

def read_data(dir):
    """Read one or more files as dataframe.
    dir: files directory
    """
    path_files = [os.path.join(dir, path) for path in os.listdir(dir)[500:550]]
    df = [pd.read_csv(file, sep='\s+') for file in path_files]
    df = pd.concat(df, sort=False)
    df = df.rename(str.lower, axis='columns')

    return df


def prepreocessing(df):
    # newdf = df[['reflect', 'precipit', 'vil', 'river', 'cxe', 'lat', 'lon']]
    newdf = df
    newdf = newdf.assign(s1=df['yyyyy_xx1'] + df['yyyyy_xx2'])
    newdf = newdf.assign(s2=df['yyyyyyy_xx3'])
    newdf = newdf.assign(s3=df['yyy_xx4'] + df['yyy_xx5'])

    # newdf = newdf.loc[newdf['precipit'] > 160]

    return newdf


def train_model(df, test_size=0.2):
    model = tree.DecisionTreeClassifier()

    X, Y = df[['reflect', 'precipit']], df[['s1']]
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=test_size)

    model = model.fit(x_train, y_train)

    return model, x_train, x_test, y_train, y_test

def foo(df):
    mat = np.zeros(58081)
    mat = np.reshape(mat, (241, 241))

    for i, row in df.iterrows():
        x, y = int(row.ind_x), int(row.ind_y)
        mat[x][y] += row.yyyyy_xx1 + row.yyyyy_xx2

    return mat




def get_graph(tree, feature_names, class_name):
    labels = [
        0, 1, 2  # 0: nada provavel, 1: provavel, 2: muito provavel
    ]

    dot_data = StringIO()
    export_graphviz(tree, out_file=dot_data,
                    filled=True, rounded=True, special_characters=True,
                    feature_names=feature_names, class_names=class_name)

    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
    graph.write_png('./decision_tree.pdf')
    graph.set_size('"15,20!"')
    Image(graph.create_png())


if __name__ == "__main__":
    PATH = '../../data/full/exp'
    df = prepreocessing(read_data(PATH))

    # X, Y = df[['reflect', 'precipit']], df[['s1']]
    # x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3)
    # model = tree.DecisionTreeClassifier()
    # model = model.fit(x_train, y_train)

    # mat = foo(df)
    preprocessing.foo()

    plt.matshow(mat)
    plt.colorbar()
    plt.show()

    print(mat.shape)
