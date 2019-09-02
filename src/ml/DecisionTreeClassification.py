import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier, export_graphviz
import time
import matplotlib.pyplot as plt


def load_data(filenames):
    df = [pd.read_csv(filename) for filename in filenames]
    df = pd.concat(df, sort=False)

    query = '(month == 8 and day >= 27) or (month == 9) or (month == 10 and day <= 7)'

    return df.query(query)


def dt_classifier(df, threshold=1, records=1000, test_size=.2):
    columns = [
        'ttyyyxx3', 'riverfrac', 'convfrac',
        'strafrac', 'meanz', 'maxz', 'meanvil',
        'ttvil', 'meanprec', 'maxprec'
    ]
    # columns = [
    #     'ttyyyxx3', 'riverfrac', 'convfrac',
    #     'strafrac', 'meanz', 'ttvil', 'meanprec'
    # ]

    labels = []
    for i, row in df.iterrows():
        if row[columns[0]] < threshold:
            labels.append(0)
        else:
            labels.append(1)

    df['label'] = labels

    yes = df[df['label'] >= threshold].sample(records)
    no = df[df['label'] < threshold].sample(records)


    df_ = pd.concat([yes, no], sort=False).sample(records*2)

    X_train, X_test, y_train, y_test = train_test_split(df_[columns[1:]],
                                                        df_[['label']], test_size=test_size)

    dt = DecisionTreeClassifier().fit(X_train, y_train)

    dotfilename = 'dotfile-%s.dot'%str(time.time()).split(('.'))[0]
    with open(dotfilename, 'w') as dotfile:
        export_graphviz(dt, out_file=dotfile, feature_names=columns[1:],
                        class_names=['com raios', 'sem raios'])

    return dt, df, X_test, y_test


def validation(model, df):
    columns = [
        'ttyyyxx3', 'riverfrac', 'convfrac',
        'strafrac', 'meanz', 'maxz', 'meanvil',
        'ttvil', 'meanprec', 'maxprec'
    ]
    scores = cross_val_score(model, df[columns[1:]], df[['label']], cv=10)

    print("Accuracy: %0.2f (+/- %0.2f%%)" % (scores.mean()*100, scores.std() * 2))

    return scores.mean()*100

def plot(data):
    values = list(data.values())
    labels = np.arange(len(values))+1

    plt.plot(labels, values, 'ro--', label='Taxa de aprendizado')
    plt.legend()
    plt.grid()
    plt.title('Validação cruzada')
    plt.xlabel('Teste')
    plt.ylabel('Acurácia %%')
    plt.savefig('cross_validadtion.png', dpi=300)
    plt.show()


if __name__ == "__main__":
    files = ['august.csv', 'september.csv', 'october.csv']
    PATH = "../../data/private/csv/fam"
    filenames = [os.path.join(PATH, file) for file in files]

    df = load_data(filenames)

    data = {}
    for x in np.arange(10)+1:
        dt, df_, X_test, y_test = dt_classifier(df)
        val = validation(dt, df_)
        data[x] = val

    plot(data)




