--- 
title: "CAP-394 Introdção à Data Science"
author: "Adriano P. Almeida"
---



# Visão geral {-}

<a href="https://www.crcpress.com/product/isbn/9781138700109" target="_blank"><img src="images/header-br.png" style="display: block; margin: auto;" /></a>

Este projeto faz parte do trabalho final da disciplina **CAP-394 - Introdução**
**à *DataScience*** que é oferecida no programa de pós graduação em computação 
aplicada do Instituto Nacional de Pesquisas Espaciais (INPE) e ministradas pelos 
professores [Dr. Rafael Santos](http://www.lac.inpe.br/~rafael.santos/) e 
[Dr. Gilberto Queiroz](http://www.dpi.inpe.br/~gribeiro/doku.php). O trabalho 
tem como principal objetivo analizar dados meteorológicos relacionados à 
descargas elétricas atmosfércas, e assim responder as tentar responder as 
seguintes questões: 

1. Através da análise de atributos, é possível identificar prováveis 
tempestades?

2. Quais os dias que apresentaram maiores índices de severidades?

3. É possível serem identificadas correlações entre a ocorrência de 
descargas elétricas e altos índices de severidade em tempestades?

4. Quais os atributos meteorológicos que mais influênciaram na 
ocorrências de descargas elétricas?

5. Quais os atributos podem ser omitidos totalmente neste trabalho?

6. Caso existam correlações entre atributos meteorológicos e ocorrência 
de raios, quais os limiares aproximados que podem ser definidos?

7. Qual a classificação de cobertura do solo da área de estudo?

8. Qual a infuência da cobertura de solo na ocorrência de raios?

9. Em qual tipo de solo, foram registados as maiores taxas de incidências
 de raios?

10. É possível aplicar alguma abordagem computacional para separar dados 
que possuem detecções de descargas elétricas dos dados que não possuem?

11. É possível aplicar alguma abordagem computacional que faça a previsão 
de descargas elétricas?

# Instalação das dependências

Afim de facilitar a reprodutibilidade deste projeto, nesta seção serão 
apresentadas brevemente as bibliotecas utilizadas e os passos essenciais para a 
fazer sua instalação.

## Numpy

Numpy é uma biblioteca para a linguagem de programação Python utilizada 
principalmente no processamento de dados tabulados em estruturas de uma ou mais 
dimensões. Além de sua robustez na manipulação de conjunto de dados massivos, a 
biblioteca Numpy possui uma vasta coleção de funções matemáticas.


### Instalação

Tradicionalmente instalação da biblioeteca Numpy pode ser feita  via 
[conda](https://docs.conda.io/en/latest/) ou 
[pip](https://pip.pypa.io/en/stable/).

Instalação do Numpy via conda.
```console
conda install -y numpy
```
Instalação do Numpy via pip.
```console
pip install numpy
```
A versão do numpy utilizada neste trabalho foi `1.15`. Para mais informações 
visite o repositório do github onde o código fonte está hoespedado, ou seu site 
oficial:

- Site oficial: [https://numpy.org](https://numpy.org/)
- Repositório github: 
[https://github.com/numpy/numpy](https://github.com/numpy/numpy)


## Pandas

Pandas é uma robusta biblioteca para manipulação e análise de dados desenvolvida 
para a linguagem de programação Python. Escrito na linguagem *C*, o Pandas 
possui um alto desempenho no carregamento massivo de dados, e também na 
realização de operações complexas de forma simples e otimizada, tornando-a uma 
das bibliotecas mais populares bibliotecas na área de *DataScience*.

### Instalação

A instalação do Pandas pode ser feita de várias maneiras, dentre elas via 
[conda](https://docs.conda.io/en/latest/) ou 
[pip](https://pip.pypa.io/en/stable/).

Instalação do Pandas via conda.
```console
conda install -y pandas
```
Instalação do Pandas via pip.
```console
pip install pandas
```
A versão do pandas utilizada neste trabalho foi `0.25.1`. Para mais informações 
visite o repositório do github onde o código fonte está hoespedado, ou seu site 
oficial:

- Site oficial: [https://pandas.pydata.org](https://pandas.pydata.org/)
- Repositório github: 
[https://github.com/pandas-dev/pandas](https://github.com/pandas-dev/pandas)


## Jupyter notebook

O Jupyter notebook é uma ambiente computacional web que permite a criação de 
documentos interativos. O Jupyter notebook é amplamente utilizada na área de 
*DataScience* graças à sua facilidade em executar códigos e receber o resultado 
diretamente no documento de forma imediata. Os documentos podem ser exporatos 
para vários formatos, incluindo `.tex`, `.html` e `.pdf`.


### Instalação

A instalação do Jupyter notebook pode ser feita de várias maneiras, dentre elas 
via [conda](https://docs.conda.io/en/latest/) ou 
[pip](https://pip.pypa.io/en/stable/).

Instalação do Jupyter notebook via conda.
```console
conda install -c conda-forge -y jupyter_conda
```
Instalação do Jupyter notebook via pip.
```console
pip install jupyter-conda
```
A versão do Jupyter notebook utilizada neste trabalho foi `3.1.0`. Para mais 
informações visite o repositório do github onde o código fonte está hoespedado, 
ou seu site oficial:

- Site oficial: [https://jupyter.org/](https://jupyter.org/)
- Repositório github: 
[https://github.com/fcollonval/jupyter_conda](https://github.com/fcollonval/jupyter_conda)


## Matplotlib

Matplotlib é uma biblioteca Python para visualização de dados por meio de 
gráficos estáicos 2D ou 3d.

<a id="matplotlib-installation"></a>
### Instalação

Algumas formas de instalalção da biblioeteca são através dos gerenciadores 
[conda](https://docs.conda.io/en/latest/) ou 
[pip](https://pip.pypa.io/en/stable/).

Instalação via conda.
```console
conda install -c conda-forge -y matplotlib
```
Instalação via pip.
```console
pip install matplotlib
```
A versão do Matplotlib utilizada neste trabalho foi `3.11`. Para mais 
informações visite o repositório do github onde o código fonte está hoespedado, 
ou seu site oficial:

- Site oficial: [https://matplotlib.org](https://matplotlib.org/)
- Repositório github: 
[https://github.com/matplotlib/matplotlib](https://github.com/matplotlib/matplotlib/)


## Raster IO

Raster IO é uma biblioteca que permite trabalhar com dados geográficos 
matriciais no Python.

### Instalação

O pacote Raser IO pode ser instalado via 
[conda](https://docs.conda.io/en/latest/):
```console
conda install -c conda-forge rasterio
```
Ou via [pip](https://pip.pypa.io/en/stable/)
```console
pip install rasterio
```
A versão do Raster IO utilizada neste trabalho foi `1.0.26`. Para mais 
informações visite o repositório do github onde o código fonte está hoespedado, 
ou seu site oficial:

- Site oficial: 
[https://rasterio.readthedocs.io/en/stable/index.html](https://rasterio.readthedocs.io/en/stable/index.html)
- Repositório github: 
[https://github.com/mapbox/rasterio](https://github.com/mapbox/rasterio)


## Basemap

O Basemap é uma extensão do Matplotlib, que tem como principal funcionalidade a 
plotagem de mapas estáticos no Python.

### Instalação

O Matplotlib é uma dependência obrigatória para o pleno funcionamento do 
Basemap. Após certificar-se de que o Matplotlib está instalado, é necessário 
baixar o pacote do Basemap no seguinte link: 
[https://sourceforge.net/projects/matplotlib/files/matplotlib-toolkits/basemap-1.0.7](https://sourceforge.net/projects/matplotlib/files/matplotlib-toolkits/basemap-1.0.7/). O Basemap funciona com o auxílio da biblioteca [GEOS](https://trac.osgeo.org/geos/), sendo assim, após baixar e descompactar o pacote, deverá ser definiada a variável de ambiente para os binários do GEOS que se encontra dentro da pasta do Basemap, usando os seguintes comandos: 

```console
cd geos-3.3.3
export GEOS_DIR = ~ /
./configure --prefix = $ GEOS_DIR
make
make install
```
E então, após a instalação e configuração do GEOS, finalmente a instalação do 
Basemap com o seguinte comando na diretório raiz do pacote:

```console
python setup.py install
```
A versão do Basemap utilizada neste trabalho foi `1.0.7`. Para mais informações 
visite o repositório do github onde o código fonte está hoespedado, ou seu site 
oficial:

- Site oficial: 
[https://basemaptutorial.readthedocs.io/en/latest](https://basemaptutorial.readthedocs.io/en/latest/)
- Repositório github: 
[https://github.com/rveciana/BasemapTutorial](https://github.com/rveciana/BasemapTutorial)


## Plotly

Plotly é uma biblioeteca para visualização e integração de gráficos, possuindo 
uma vasta e agradável gama de layouts. 

### Instalação

A instalação do Plotly pode ser feita via 
[conda](https://docs.conda.io/en/latest/):

```console
conda install -c plotly plotly
```

Ou via [pip](https://pip.pypa.io/en/stable/):
```console
pip install plotly
```
A versão do Plotly utilizada neste trabalho foi `4.1.0`. Para mais informações 
visite o repositório do github onde o código fonte está hoespedado, ou seu site 
oficial:

- Site oficial: [https://plot.ly/python/getting-started](https://plot.ly/python/getting-started/)
- Repositório github: [https://github.com/plotly/plotly.py](https://github.com/plotly/plotly.py)


## Scikit-learn

A Scikit-learn é uma biblioteca com uma vasta gama de ferramentas para análise 
de dados. Diversos algoritmos de aprendizado de máquina estão inclusos no 
Scikit-learn.

### Instalação

A instalação do Scikit-learn pode ser feita via 
[conda](https://docs.conda.io/en/latest/):

```console
conda install -c anaconda scikit-learn
```

Ou via [pip](https://pip.pypa.io/en/stable/):
```console
pip install scikit-learn
```
A versão do Scikit-learn utilizada neste trabalho foi `0.19.1`. Para mais 
informações visite o repositório do github onde o código fonte está hoespedado, 
ou seu site oficial:

- Site oficial: 
[https://scikit-learn.org/stable](https://scikit-learn.org/stable/)
- Repositório github: 
[https://github.com/scikit-learn/scikit-learn](https://github.com/scikit-learn/scikit-learn)
