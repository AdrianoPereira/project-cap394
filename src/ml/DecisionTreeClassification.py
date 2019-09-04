import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.externals import joblib as jb
import time
import matplotlib.pyplot as plt


def load_data(filenames):
    df = [pd.read_csv(filename) for filename in filenames]
    df = pd.concat(df, sort=False)

    query = '(month == 8 and day >= 27) or (month == 9) or (month == 10 and day <= 7)'

    return df.query(query)


def dt_classifier(df, threshold=1, records=1, test_size=.2):
    columns = [
        'ttyyyxx3', 'riverfrac', 'convfrac',
        'strafrac', 'meanz', 'maxz', 'meanvil',
        'ttvil', 'meanprec', 'maxprec'
    ]

    labels = []

    for i, row in df.iterrows():
        if row[columns[0]] < threshold:
            labels.append(0)
        else:
            labels.append(1)

    df['label'] = labels

    yes = df[df['label'] == 1]
    no = df[df['label'] == 0]

    lyes = yes['label'].count()
    lno = no['label'].count()
    less = lyes if lyes < lno else lno

    records = int((less*(records*100))/100)
    print(records, ' ---')

    df_= pd.concat([yes, no], sort=False).sample(records*2)

    X_train, X_test, y_train, y_test = train_test_split(df_[columns[1:]],
                                                        df_[['label']], test_size=test_size)

    dt = DecisionTreeClassifier().fit(X_train, y_train)

    # dotfilename = 'dotfile-%s.dot'%str(time.time()).split(('.'))[0]
    # with open(dotfilename, 'w') as dotfile:
    #     export_graphviz(dt, out_file=dotfile, feature_names=columns[1:],
    #                     class_names=['com raios', 'sem raios'])

    return dt, df, X_test, y_test


def cross_validation(model, df):
    columns = [
        'ttyyyxx3', 'riverfrac', 'convfrac',
        'strafrac', 'meanz', 'maxz', 'meanvil',
        'ttvil', 'meanprec', 'maxprec'
    ]
    scores = cross_val_score(model, df[columns[1:]], df[['label']], cv=10)

    print("Accuracy: %0.2f (+/- %0.2f%%)" % (scores.mean()*100, scores.std() * 2))

    save_model(model, 'dtc_acc%.0f.pkl'%(scores.mean()*100))

    return scores.mean()*100


def plot(data):
    values = list(data.values())
    labels = np.arange(len(values))+1

    plt.plot(labels, values, 'ro--', label='Taxa de aprendizado')
    plt.legend()
    plt.grid()
    plt.title('Validação cruzada')
    plt.xlabel('Época')
    plt.ylabel('Acurácia (%)')
    plt.savefig('cross_validadtion.png', dpi=300)
    plt.show()

def save_model(model, name):
    print('Saving model...')

    folder = 'models'
    if not os.path.exists(folder):
        os.makedirs(folder)
    filename = os.path.join(folder, name)
    jb.dump(model, filename)

    print('Model saved')


if __name__ == "__main__":
    files = ['august.csv', 'september.csv', 'october.csv']
    PATH = "../../data/private/csv/fam"
    filenames = [os.path.join(PATH, file) for file in files]

    df = load_data(filenames)

    data = {}

    for x in np.arange(30)+1:
        dt, df_, X_test, y_test = dt_classifier(df, threshold=3)
        val = cross_validation(dt, df_)

        filename = 'dt_mode'

        data[x] = val

    plot(data)




