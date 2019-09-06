![](https://raw.githubusercontent.com/AdrianoPereira/project-cap394/master/assets/images/header-pt.png)

<a id="index"></a>
## Index
- [Index](#index)
- [1. Visão geral](#overview)
- [2. Numpy](#numpy)
  - [2.1 Instalação](#numpy-installation)
- [3. Pandas](#pandas)
  - [3.1 Instalação](#pandas-installation)
- [4. Jupyter notebook](#jupyter)
  - [4.1 Instalação](#jupyter-installation)
- [4. Matplotlib](#matplotlib)
  - [4.1 Instalação](#matplotlib-installation)
- [4. Basemap](#basemap)
  - [4.1 Instalação](#basemap-installation)
- [4. Plotly](#plotly)
  - [4.1 Instalação](#plotly-installation)
- [4. Scikit-learn](#scikit)
  - [4.1 Instalação](#scikit-installation)

*By: Adriano P. Almeida*


<a id="overview"></a>
## 1. Visão geral [⬆](#index)

---

Este documento tem como objetivo fundamental expor as principais dependências utilizadas no trabalho, bem como os passos essenciais para a instalação, com isso, facilitando na reprodutibilidade do projeto por outras pessoas.

<a id="numpy"></a>
## 2. Numpy [⬆](#index)

---

Numpy é uma biblioteca para a linguagem de programação Python utilizada principalmente no processamento de dados tabulados em estruturas de uma ou mais dimensões. Além de sua robustez na manipulação de conjunto de dados massivos, a biblioteca Numpy possui uma vasta coleção de funções matemáticas.

<a id="numpy-installation"></a>
### 2.1 Instalação [⬆](#index)

---

Tradicionalmente instalação da biblioeteca Numpy pode ser feita  via [conda](https://docs.conda.io/en/latest/) ou [pip](https://pip.pypa.io/en/stable/).

Instalação do Numpy via conda.
```console
conda install -y numpy
```
Instalação do Numpy via pip.
```console
pip install numpy
```
A versão do numpy utilizada neste trabalho foi `1.15`. Para mais informações visite o repositório do github onde o código fonte está hoespedado, ou seu site oficial:

- Site oficial: [https://numpy.org](https://numpy.org/)
- Repositório github: [https://github.com/numpy/numpy](https://github.com/numpy/numpy)


<a id="pandas"></a>
## 3. Pandas [⬆](#index)

---

Pandas é uma robusta biblioteca para manipulação e análise de dados desenvolvida para a linguagem de programação Python. Escrito na linguagem *C*, o Pandas possui um alto desempenho no carregamento massivo de dados, e também na realização de operações complexas de forma simples e otimizada, tornando-a uma das bibliotecas mais populares bibliotecas na área de *DataScience*.

<a id="pandas-installation"></a>
### 3.1 Instalação [⬆](#index)

---

A instalação do Pandas pode ser feita de várias maneiras, dentre elas via [conda](https://docs.conda.io/en/latest/) ou [pip](https://pip.pypa.io/en/stable/).

Instalação do Pandas via conda.
```console
conda install -y pandas
```
Instalação do Pandas via pip.
```console
pip install pandas
```
A versão do pandas utilizada neste trabalho foi `0.25.1`. Para mais informações visite o repositório do github onde o código fonte está hoespedado, ou seu site oficial:

- Site oficial: [https://pandas.pydata.org](https://pandas.pydata.org/)
- Repositório github: [https://github.com/pandas-dev/pandas](https://github.com/pandas-dev/pandas)


<a id="jupyter"></a>
## 4. Jupyter notebook [⬆](#index)

---

O Jupyter notebook é uma ambiente computacional web que permite a criação de documentos interativos. O Jupyter notebook é amplamente utilizada na área de *DataScience* graças à sua facilidade em executar códigos e receber o resultado diretamente no documento de forma imediata. Os documentos podem ser exporatos para vários formatos, incluindo `.tex`, `.html` e `.pdf`.

<a id="jupyter-installation"></a>
### 4.1 Instalação [⬆](#index)

---

A instalação do Jupyter notebook pode ser feita de várias maneiras, dentre elas via [conda](https://docs.conda.io/en/latest/) ou [pip](https://pip.pypa.io/en/stable/).

Instalação do Jupyter notebook via conda.
```console
conda install -c conda-forge -y jupyter_conda
```
Instalação do Jupyter notebook via pip.
```console
pip install jupyter-conda
```
A versão do Jupyter notebook utilizada neste trabalho foi `3.1.0`. Para mais informações visite o repositório do github onde o código fonte está hoespedado, ou seu site oficial:

- Site oficial: [https://jupyter.org/](https://jupyter.org/)
- Repositório github: [https://github.com/fcollonval/jupyter_conda](https://github.com/fcollonval/jupyter_conda)


<a id="matplotlib"></a>
## 4. Matplotlib [⬆](#index)

---

Matplotlib é uma biblioteca Python para visualização de dados por meio de gráficos estáicos 2D ou 3d.

<a id="matplotlib-installation"></a>
### 4.1 Instalação [⬆](#index)

---

Algumas formas de instalalção da biblioeteca são através dos gerenciadores [conda](https://docs.conda.io/en/latest/) ou [pip](https://pip.pypa.io/en/stable/).

Instalação via conda.
```console
conda install -c conda-forge -y matplotlib
```
Instalação via pip.
```console
pip install matplotlib
```
A versão do Matplotlib utilizada neste trabalho foi `3.11`. Para mais informações visite o repositório do github onde o código fonte está hoespedado, ou seu site oficial:

- Site oficial: [https://matplotlib.org](https://matplotlib.org/)
- Repositório github: [https://github.com/matplotlib/matplotlib](https://github.com/matplotlib/matplotlib/)

<a id="basemap"></a>
## 4. Basemap [⬆](#index)

---

O Basemap é uma extensão do Matplotlib, que tem como principal funcionalidade a plotagem de mapas estáticos no Python.

<a id="basemap-installation"></a>
### 4.1 Instalação [⬆](#index)

---

O Matplotlib é uma dependência obrigatória para o pleno funcionamento do Basemap. Após certificar-se de que o Matplotlib está instalado, é necessário baixar o pacote do Basemap no seguinte link: [https://sourceforge.net/projects/matplotlib/files/matplotlib-toolkits/basemap-1.0.7](https://sourceforge.net/projects/matplotlib/files/matplotlib-toolkits/basemap-1.0.7/). O Basemap funciona com o auxílio da biblioteca [GEOS](https://trac.osgeo.org/geos/), sendo assim, após baixar e descompactar o pacote, deverá ser definiada a variável de ambiente para os binários do GEOS que se encontra dentro da pasta do Basemap, usando os seguintes comandos: 

```console
cd geos-3.3.3
export GEOS_DIR = ~ /
./configure --prefix = $ GEOS_DIR
make
make install
```
E então, após a instalação e configuração do GEOS, finalmente a instalação do Basemap com o seguinte comando na diretório raiz do pacote:

```console
python setup.py install
```
A versão do Basemap utilizada neste trabalho foi `1.0.7`. Para mais informações visite o repositório do github onde o código fonte está hoespedado, ou seu site oficial:

- Site oficial: [https://basemaptutorial.readthedocs.io/en/latest](https://basemaptutorial.readthedocs.io/en/latest/)
- Repositório github: [https://github.com/rveciana/BasemapTutorial](https://github.com/rveciana/BasemapTutorial)

<a id="plotly"></a>
## 4. Plotly [⬆](#index)

---

Plotly é uma biblioeteca para visualização e integração de gráficos, possuindo uma vasta e agradável gama de layouts. 

<a id="plotly-installation"></a>
### 4.1 Instalação [⬆](#index)

---

A instalação do Plotly pode ser feita via [conda](https://docs.conda.io/en/latest/):

```console
conda install -c plotly plotly
```

Ou via [pip](https://pip.pypa.io/en/stable/):
```console
pip install plotly
```
A versão do Plotly utilizada neste trabalho foi `4.1.0`. Para mais informações visite o repositório do github onde o código fonte está hoespedado, ou seu site oficial:

- Site oficial: [https://plot.ly/python/getting-started](https://plot.ly/python/getting-started/)
- Repositório github: [https://github.com/plotly/plotly.py](https://github.com/plotly/plotly.py)

<a id="scikit"></a>
## 4. Scikit-learn [⬆](#index)

---

A Scikit-learn é uma biblioteca com uma vasta gama de ferramentas para análise de dados. Diversos algoritmos de aprendizado de máquina estão inclusos no Scikit-learn.

<a id="scikit-installation"></a>
### 4.1 Instalação [⬆](#index)

---

A instalação do Scikit-learn pode ser feita via [conda](https://docs.conda.io/en/latest/):

```console
conda install -c anaconda scikit-learn
```

Ou via [pip](https://pip.pypa.io/en/stable/):
```console
pip install scikit-learn
```
A versão do Scikit-learn utilizada neste trabalho foi `0.19.1`. Para mais informações visite o repositório do github onde o código fonte está hoespedado, ou seu site oficial:

- Site oficial: [https://scikit-learn.org/stable](https://scikit-learn.org/stable/)
- Repositório github: [https://github.com/scikit-learn/scikit-learn](https://github.com/scikit-learn/scikit-learn)