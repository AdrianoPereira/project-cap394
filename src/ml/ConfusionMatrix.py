import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np


def plot_confusion_matrix(cm, ax, n):
    cmap = plt.cm.Blues
    #     figsize = (16, 8)
    #     fig, ax = plt.subplots(figsize=figsize)
    ax = ax
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.4)

    total_samples = cm.sum(axis=1)[:, np.newaxis]
    normed_conf_mat = cm.astype('float') / total_samples
    labels = ['Sem raios', 'Com raios']
    label_font = dict(fontweight='normal')
    title_font = dict(fontweight='normal', size=18)

    matshow = ax.matshow(cm, cmap=cmap)
    cb = plt.colorbar(matshow, cax=cax, orientation='vertical')

    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            cell_text = str(cm[i, j])
            cell_text += '\n(%.2f%%)' % (normed_conf_mat[i, j] * 100)
            ax.text(x=j,
                    y=i,
                    s=cell_text,
                    va='center',
                    ha='center',
                    color="white" if normed_conf_mat[i, j] > 0.5 else "black")

    ax.set_xticklabels([''] + labels)
    ax.set_yticklabels([''] + labels, rotation=90, va='center')
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')

    #     ax.set_title('Matriz de confusão para %d testes'%((n*2)*0.2), fontdict=title_font)
    ax.set_xlabel('Classe prevista', fontdict=label_font)
    ax.set_ylabel('Classe real', fontdict=label_font)

    cb.ax.set_ylabel('Ocorrências', va='center', rotation=-270, labelpad=-40)


    return ax


if __name__ == "__main__":
    cm = np.array([
        [10, 2],
        [1, 15]
    ])

    fig, ax = plt.subplots()

    plot_confusion_matrix(cm, ax, 1)

    plt.show()