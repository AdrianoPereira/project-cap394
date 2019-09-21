---
title: "Metodologia"
bibliography: "references.bib"
link-citations: yes
csl: style-ref.csl
output: 
  bookdown::html_document2: 
    fig_caption: yes
references:
- id: fenner2012a
  title: One-click science marketing
  author:
  - family: Fenner
    given: Martin
  container-title: Nature Materials
  volume: 11
  URL: 'http://dx.doi.org/10.1038/nmat3283'
  DOI: 10.1038/nmat3283
  issue: 4
  publisher: Nature Publishing Group
  page: 261-263
  type: article-journal
  issued:
    year: 2012
    month: 3
---

# Metodologia

Neste seção, serão descritas as etapas metodológicas utilizadas no 
desenvolvimento deste trabalho.


## Contextualização da área de estudo

Para este trabalho foram utilizados os dados do radar meteorológico SIPAM 
(Sistema de Proteção da Amazônia) [@saraiva2016regional] e da rede de detecção 
de raios LINET (sigla do inglês, *Lightning NETwork*) [@betz2009linet]. Os dados 
são oriundos dos experimentos CHUVA-Manaus [@machado2014chuva] e GoAmazon 
[@martin2016introduction] que aconteceu no ano de 2014 na região central da 
Bacia Amazônica. O conjunto de dados, também é resultado do processamento feito 
no trabalho de [@rebeca2019propriedades], afim de se calcular alguns outros 
índices, para isso, foi utilizada a ferramenta proposta por 
[@de2009monitoramento], que ser trata adaptação do algoritmo de rastreio de 
nuvens ForTraCC (*Forecast and Tracking of Active Convective Cells*) 
[@vila2008forecast].

Os dados possuem resolução temporal de 12 minutos, e foram obtidos durante o 
período de 27 de agosto a 7 de outubro em uma área de 500 km$^{2}$, cobrindo ao 
todo 20 municípios do estado do Amazonas. A floresta é o tipo de cobertura do 
solo predominante nessa região, e na área de estudo representa mais de 85\%, 
como pode ser observado na Figura \@ref(fig:landcover). Com isso, aumenta-se os 
riscos serem iniciados incêndios florestais em decorrência de raios nuvem-solo, 
principalmente no segundo Período de Operação Intensiva (IOP - sigla do inglês, 
*Intensive Operation Period*) [@marengo1994calculations], que corresponde a 
transição entre as estações seca e chuvosa, que acontece a partir do mês de 
agosto. É nesse perı́odo que acontecem tempestades mais severas, e 
consequentemente maiores incidências de descargas elétricas 
[@rebeca2019propriedades].


<div class="figure">
<img src="images/landcoverhorizontal.png" alt="Área de estudo e sua cobertura do solo."  />
<p class="caption">(\#fig:landcover)Área de estudo e sua cobertura do solo.</p>
</div>


## Análise exploratória dos dados
Nesta seção serão feitas as devidas importações e também a análise exploratíoria
dos dados.


### Carregando base de dados
A célula abaixo faz a importação das bibliotecas que serão utilizadas na análise
dos dados.


```python
#importação das bibliotecas que serão utilizadas
import os
import numpy as np
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly
```

Como o foco deste trabalho é trabalhar com os dados da rede de detecção LINET, 
os dados carregados deverão ser filtrados, já que a rede esteve em funcionamento
somente durante um certo período do experimento. Sendo assim, a célula abaixo 
faz a importação e filtragem dos dados .

```python
#definindo arquivos para serem carregados
files = ['august.csv', 'september.csv', 'october.csv'] 
PATH ='../data/private/csv/fam/'

#Carregando e concatenando base de dados
df = [pd.read_csv(os.path.join(PATH, file)) 
      for file in files]
df = pd.concat(df, sort=False)
print('Total de registros carregados: %s'%df['month'].count())

#Filtrando base de dados
```

```
## Total de registros carregados: 53160
```

```python
query = '(month == 8 and day >= 27) or (month == 9) or (month == 10 and day <= 7)'
df = df.query(query)
print('Total de registros após a filtragem: %s'%df['month'].count())

#Exibindo primeiras linhas da base de dados
```

```
## Total de registros após a filtragem: 26218
```

```python
df.head()
```

```
##        time  sysclass   lat    lon    dir   vel  size  ...  meanprec  maxprec  year  month  day  hour  minute
## 12871   0.0       0.0 -2.75 -58.57 -999.0   0.0  13.0  ...      0.97     1.18  2014      8   27     2      24
## 12872   0.2       1.0 -2.73 -58.57    0.0  11.1  30.0  ...      1.80     4.16  2014      8   27     2      24
## 12873   0.0       0.0 -2.73 -58.57 -999.0   0.0  21.0  ...      1.02     1.32  2014      8   27     3       0
## 12874   0.2       1.0 -2.75 -58.57  180.0  11.1  13.0  ...      0.97     1.09  2014      8   27     3       0
## 12875   0.0       0.0 -1.71 -59.63 -999.0   0.0  12.0  ...      0.92     0.97  2014      8   27     3      48
## 
## [5 rows x 26 columns]
```

O código da célula abaixo mostra uma descrição básica de alguns índices do 
conjunto de dados.


```python
indexes = ['ttyyyxx3', 'riverfrac', 'convfrac', 'strafrac', 'meanz', 'maxz', 
            'meanvil', 'ttvil', 'meanprec', 'maxprec']
df[indexes].describe()
```

```
##            ttyyyxx3    riverfrac      convfrac      strafrac  ...       meanvil         ttvil      meanprec       maxprec
## count  26218.000000  26218.00000  26218.000000  26218.000000  ...  26218.000000  26218.000000  26218.000000  26218.000000
## mean       3.293691     10.87239     45.135574     54.864425  ...      1.022231    140.454784      6.696094     43.228542
## std       31.210997     19.20553     27.621304     27.621304  ...      0.926023    462.869909      7.353271     63.641824
## min        0.000000      0.00000      0.000000      0.000000  ...      0.160000      1.770000      0.820000      0.880000
## 25%        0.000000      0.00000     25.000000     37.930000  ...      0.370000     10.350000      1.940000      5.340000
## 50%        0.000000      0.00000     36.360000     63.640000  ...      0.690000     27.160000      4.020000     17.490000
## 75%        0.000000     13.64750     62.070000     75.000000  ...      1.350000     86.845000      8.940000     56.480000
## max     1493.000000    100.00000    100.000000    100.000000  ...     14.980000  13637.050000    168.770000    996.970000
## 
## [8 rows x 10 columns]
```
> **Nota**:  O atributo `ttyyyxx3` é referente a quantidade de raios detectados
> pela rede LINET a cada 12 minutos.

O código da célula abaixo tem como objetivo gerar um gráfico com a quantidade de
registro em que foram detectados raios e quantidade de registros em que não 
foram detectados raios.


```python
#Separando registros com e sem detecções de raios
no = df[df['ttyyyxx3'] < 1]
yes = df[df['ttyyyxx3'] >= 1]

#Contando quantidade de registros em cada subconjunto de dados
tn = no['month'].count()
ty = yes['month'].count()

#Organizando dados de entrada para o gráfico
labels = ['Sem raios detectados (%d)'%tn, 
         'Com raios detectados (%d)'%ty]
values= [tn, ty]

#Criando gráfico
fig = go.Figure()
fig.add_trace(
    go.Pie(labels=labels, values=values, hole=.5, 
        marker=dict(colors=['#000000', '#D82D3B'], 
                    line=dict(color='#A0A0A0', width=1)))
)

#Alterando layout do gráfico
```

```python
_ = fig.update_layout(
    title='<b>Gráfico 1</b>: Quantidade de registros com e sem detecção de \
    <br>descargas atmosféricas',
    template='plotly_dark',
    legend_orientation="v"
)

fig.show()
```



<!--html_preserve--><div id="htmlwidget-1a35633ef578c1824231" style="width:672px;height:480px;" class="plotly html-widget"></div>
<script type="application/json" data-for="htmlwidget-1a35633ef578c1824231">{"x":{"data":[{"hole":0.5,"labels":["Sem raios detectados (22820)","Com raios detectados (3398)"],"marker":{"colors":["#000000","#D82D3B"],"line":{"color":"#A0A0A0","width":1}},"values":[22820,3398],"type":"pie","frame":null}],"layout":{"template":{"data":{"barpolar":[{"marker":{"line":{"color":"rgb(17,17,17)","width":0.5}},"type":"barpolar"}],"bar":[{"error_x":{"color":"#f2f5fa"},"error_y":{"color":"#f2f5fa"},"marker":{"line":{"color":"rgb(17,17,17)","width":0.5}},"type":"bar"}],"carpet":[{"aaxis":{"endlinecolor":"#A2B1C6","gridcolor":"#506784","linecolor":"#506784","minorgridcolor":"#506784","startlinecolor":"#A2B1C6"},"baxis":{"endlinecolor":"#A2B1C6","gridcolor":"#506784","linecolor":"#506784","minorgridcolor":"#506784","startlinecolor":"#A2B1C6"},"type":"carpet"}],"choropleth":[{"colorbar":{"outlinewidth":0,"ticks":""},"type":"choropleth"}],"contourcarpet":[{"colorbar":{"outlinewidth":0,"ticks":""},"type":"contourcarpet"}],"contour":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0,"#0d0887"],[0.111111111111111,"#46039f"],[0.222222222222222,"#7201a8"],[0.333333333333333,"#9c179e"],[0.444444444444444,"#bd3786"],[0.555555555555556,"#d8576b"],[0.666666666666667,"#ed7953"],[0.777777777777778,"#fb9f3a"],[0.888888888888889,"#fdca26"],[1,"#f0f921"]],"type":"contour"}],"heatmapgl":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0,"#0d0887"],[0.111111111111111,"#46039f"],[0.222222222222222,"#7201a8"],[0.333333333333333,"#9c179e"],[0.444444444444444,"#bd3786"],[0.555555555555556,"#d8576b"],[0.666666666666667,"#ed7953"],[0.777777777777778,"#fb9f3a"],[0.888888888888889,"#fdca26"],[1,"#f0f921"]],"type":"heatmapgl"}],"heatmap":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0,"#0d0887"],[0.111111111111111,"#46039f"],[0.222222222222222,"#7201a8"],[0.333333333333333,"#9c179e"],[0.444444444444444,"#bd3786"],[0.555555555555556,"#d8576b"],[0.666666666666667,"#ed7953"],[0.777777777777778,"#fb9f3a"],[0.888888888888889,"#fdca26"],[1,"#f0f921"]],"type":"heatmap"}],"histogram2dcontour":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0,"#0d0887"],[0.111111111111111,"#46039f"],[0.222222222222222,"#7201a8"],[0.333333333333333,"#9c179e"],[0.444444444444444,"#bd3786"],[0.555555555555556,"#d8576b"],[0.666666666666667,"#ed7953"],[0.777777777777778,"#fb9f3a"],[0.888888888888889,"#fdca26"],[1,"#f0f921"]],"type":"histogram2dcontour"}],"histogram2d":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0,"#0d0887"],[0.111111111111111,"#46039f"],[0.222222222222222,"#7201a8"],[0.333333333333333,"#9c179e"],[0.444444444444444,"#bd3786"],[0.555555555555556,"#d8576b"],[0.666666666666667,"#ed7953"],[0.777777777777778,"#fb9f3a"],[0.888888888888889,"#fdca26"],[1,"#f0f921"]],"type":"histogram2d"}],"histogram":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"histogram"}],"mesh3d":[{"colorbar":{"outlinewidth":0,"ticks":""},"type":"mesh3d"}],"parcoords":[{"line":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"parcoords"}],"scatter3d":[{"line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatter3d"}],"scattercarpet":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattercarpet"}],"scattergeo":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattergeo"}],"scattergl":[{"marker":{"line":{"color":"#283442"}},"type":"scattergl"}],"scattermapbox":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattermapbox"}],"scatterpolargl":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatterpolargl"}],"scatterpolar":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatterpolar"}],"scatter":[{"marker":{"line":{"color":"#283442"}},"type":"scatter"}],"scatterternary":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatterternary"}],"surface":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0,"#0d0887"],[0.111111111111111,"#46039f"],[0.222222222222222,"#7201a8"],[0.333333333333333,"#9c179e"],[0.444444444444444,"#bd3786"],[0.555555555555556,"#d8576b"],[0.666666666666667,"#ed7953"],[0.777777777777778,"#fb9f3a"],[0.888888888888889,"#fdca26"],[1,"#f0f921"]],"type":"surface"}],"table":[{"cells":{"fill":{"color":"#506784"},"line":{"color":"rgb(17,17,17)"}},"header":{"fill":{"color":"#2a3f5f"},"line":{"color":"rgb(17,17,17)"}},"type":"table"}]},"layout":{"annotationdefaults":{"arrowcolor":"#f2f5fa","arrowhead":0,"arrowwidth":1},"colorscale":{"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]],"sequential":[[0,"#0d0887"],[0.111111111111111,"#46039f"],[0.222222222222222,"#7201a8"],[0.333333333333333,"#9c179e"],[0.444444444444444,"#bd3786"],[0.555555555555556,"#d8576b"],[0.666666666666667,"#ed7953"],[0.777777777777778,"#fb9f3a"],[0.888888888888889,"#fdca26"],[1,"#f0f921"]],"sequentialminus":[[0,"#0d0887"],[0.111111111111111,"#46039f"],[0.222222222222222,"#7201a8"],[0.333333333333333,"#9c179e"],[0.444444444444444,"#bd3786"],[0.555555555555556,"#d8576b"],[0.666666666666667,"#ed7953"],[0.777777777777778,"#fb9f3a"],[0.888888888888889,"#fdca26"],[1,"#f0f921"]]},"colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#f2f5fa"},"geo":{"bgcolor":"rgb(17,17,17)","lakecolor":"rgb(17,17,17)","landcolor":"rgb(17,17,17)","showlakes":true,"showland":true,"subunitcolor":"#506784"},"hoverlabel":{"align":"left"},"hovermode":"closest","mapbox":{"style":"dark"},"paper_bgcolor":"rgb(17,17,17)","plot_bgcolor":"rgb(17,17,17)","polar":{"angularaxis":{"gridcolor":"#506784","linecolor":"#506784","ticks":""},"bgcolor":"rgb(17,17,17)","radialaxis":{"gridcolor":"#506784","linecolor":"#506784","ticks":""}},"scene":{"xaxis":{"backgroundcolor":"rgb(17,17,17)","gridcolor":"#506784","gridwidth":2,"linecolor":"#506784","showbackground":true,"ticks":"","zerolinecolor":"#C8D4E3"},"yaxis":{"backgroundcolor":"rgb(17,17,17)","gridcolor":"#506784","gridwidth":2,"linecolor":"#506784","showbackground":true,"ticks":"","zerolinecolor":"#C8D4E3"},"zaxis":{"backgroundcolor":"rgb(17,17,17)","gridcolor":"#506784","gridwidth":2,"linecolor":"#506784","showbackground":true,"ticks":"","zerolinecolor":"#C8D4E3"}},"shapedefaults":{"line":{"color":"#f2f5fa"}},"sliderdefaults":{"bgcolor":"#C8D4E3","bordercolor":"rgb(17,17,17)","borderwidth":1,"tickwidth":0},"ternary":{"aaxis":{"gridcolor":"#506784","linecolor":"#506784","ticks":""},"baxis":{"gridcolor":"#506784","linecolor":"#506784","ticks":""},"bgcolor":"rgb(17,17,17)","caxis":{"gridcolor":"#506784","linecolor":"#506784","ticks":""}},"title":{"x":0.05},"updatemenudefaults":{"bgcolor":"#506784","borderwidth":0},"xaxis":{"automargin":true,"gridcolor":"#283442","linecolor":"#506784","ticks":"","zerolinecolor":"#283442","zerolinewidth":2},"yaxis":{"automargin":true,"gridcolor":"#283442","linecolor":"#506784","ticks":"","zerolinecolor":"#283442","zerolinewidth":2}}},"legend":{"orientation":"v"},"title":{"text":"<b>Gráfico 1<\/b>: Quantidade de registros com e sem detecção de     <br>descargas atmosféricas"},"hovermode":"closest","showlegend":true},"attrs":[],"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.2,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script><!--/html_preserve-->

Como mostrado no Gráfico 1, a quantidade de registros em que foram detectados 
raios é muito menor do que a quantidade de registros em que não foi detectado
nenhum raio. Nesse comjunto de dados, a quantidade de registros tende a diminuir
conforme aumenta a quantidade de detecções, ou seja, registros com muitos raios
detectados a cada 12 minutos, é muito menor que a quantidade de registros com
poucos raios detectados. Essa relação pode ser observado no Gráfico 2.


```python
#Contando a quantidade de registros em cada número de detecções
group = df.groupby(['ttyyyxx3']).agg({'ttyyyxx3': 'count'})

#Organizando dados de entrada para o gráfico
labels = [int(x) for x in group.index][:100]
values = group['ttyyyxx3'].values[:100]
ranges = [
    (1, 5), 
    (5, 10), (10, 20), (20, 30), (30, 40), (40, 50)
]

#Criando estrutura do gráfico
fig = go.Figure()
for r in ranges:
    labels = [int(x) for x in group.index][r[0]:r[1]]
    values = group['ttyyyxx3'].values[r[0]:r[1]]

    _ = fig.add_trace(
        go.Bar(x=labels, y=values, name='%d a %d detecções de raios'%(r[0], 
        r[1]))
    )

#Alterando layout do gráfico
fig.update_yaxes(title_text='Quantidade de registros')
```

```python
fig.update_xaxes(title_text='Raios detectados a cada 12 minutos')
```

```python
fig.update_layout(template='plotly_dark', title='Frequência do \
número de raios detectados a cada 12 minutos')

# fig.show()
```



<!--html_preserve--><div id="htmlwidget-7e37d2d24c96e7846aa5" style="width:672px;height:480px;" class="plotly html-widget"></div>
<script type="application/json" data-for="htmlwidget-7e37d2d24c96e7846aa5">{"x":{"data":[{"name":"1 a 5 detecções de raios","x":[1,2,3,4],"y":[1134,453,249,194],"type":"bar","xaxis":"x","yaxis":"y","frame":null},{"name":"5 a 10 detecções de raios","x":[5,6,7,8,9],"y":[134,87,74,88,58],"type":"bar","xaxis":"x","yaxis":"y","frame":null},{"name":"10 a 20 detecções de raios","x":[10,11,12,13,14,15,16,17,18,19],"y":[43,50,38,28,29,28,22,20,13,24],"type":"bar","xaxis":"x","yaxis":"y","frame":null},{"name":"20 a 30 detecções de raios","x":[20,21,22,23,24,25,26,27,28,29],"y":[26,15,23,16,14,12,15,11,13,7],"type":"bar","xaxis":"x","yaxis":"y","frame":null},{"name":"30 a 40 detecções de raios","x":[30,31,32,33,34,35,36,37,38,39],"y":[12,11,7,11,6,9,6,8,6,4],"type":"bar","xaxis":"x","yaxis":"y","frame":null},{"name":"40 a 50 detecções de raios","x":[40,41,42,43,44,45,46,47,48,49],"y":[7,2,5,9,7,7,5,7,5,4],"type":"bar","xaxis":"x","yaxis":"y","frame":null}],"layout":{"template":{"data":{"barpolar":[{"marker":{"line":{"color":"rgb(17,17,17)","width":0.5}},"type":"barpolar"}],"bar":[{"error_x":{"color":"#f2f5fa"},"error_y":{"color":"#f2f5fa"},"marker":{"line":{"color":"rgb(17,17,17)","width":0.5}},"type":"bar"}],"carpet":[{"aaxis":{"endlinecolor":"#A2B1C6","gridcolor":"#506784","linecolor":"#506784","minorgridcolor":"#506784","startlinecolor":"#A2B1C6"},"baxis":{"endlinecolor":"#A2B1C6","gridcolor":"#506784","linecolor":"#506784","minorgridcolor":"#506784","startlinecolor":"#A2B1C6"},"type":"carpet"}],"choropleth":[{"colorbar":{"outlinewidth":0,"ticks":""},"type":"choropleth"}],"contourcarpet":[{"colorbar":{"outlinewidth":0,"ticks":""},"type":"contourcarpet"}],"contour":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0,"#0d0887"],[0.111111111111111,"#46039f"],[0.222222222222222,"#7201a8"],[0.333333333333333,"#9c179e"],[0.444444444444444,"#bd3786"],[0.555555555555556,"#d8576b"],[0.666666666666667,"#ed7953"],[0.777777777777778,"#fb9f3a"],[0.888888888888889,"#fdca26"],[1,"#f0f921"]],"type":"contour"}],"heatmapgl":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0,"#0d0887"],[0.111111111111111,"#46039f"],[0.222222222222222,"#7201a8"],[0.333333333333333,"#9c179e"],[0.444444444444444,"#bd3786"],[0.555555555555556,"#d8576b"],[0.666666666666667,"#ed7953"],[0.777777777777778,"#fb9f3a"],[0.888888888888889,"#fdca26"],[1,"#f0f921"]],"type":"heatmapgl"}],"heatmap":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0,"#0d0887"],[0.111111111111111,"#46039f"],[0.222222222222222,"#7201a8"],[0.333333333333333,"#9c179e"],[0.444444444444444,"#bd3786"],[0.555555555555556,"#d8576b"],[0.666666666666667,"#ed7953"],[0.777777777777778,"#fb9f3a"],[0.888888888888889,"#fdca26"],[1,"#f0f921"]],"type":"heatmap"}],"histogram2dcontour":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0,"#0d0887"],[0.111111111111111,"#46039f"],[0.222222222222222,"#7201a8"],[0.333333333333333,"#9c179e"],[0.444444444444444,"#bd3786"],[0.555555555555556,"#d8576b"],[0.666666666666667,"#ed7953"],[0.777777777777778,"#fb9f3a"],[0.888888888888889,"#fdca26"],[1,"#f0f921"]],"type":"histogram2dcontour"}],"histogram2d":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0,"#0d0887"],[0.111111111111111,"#46039f"],[0.222222222222222,"#7201a8"],[0.333333333333333,"#9c179e"],[0.444444444444444,"#bd3786"],[0.555555555555556,"#d8576b"],[0.666666666666667,"#ed7953"],[0.777777777777778,"#fb9f3a"],[0.888888888888889,"#fdca26"],[1,"#f0f921"]],"type":"histogram2d"}],"histogram":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"histogram"}],"mesh3d":[{"colorbar":{"outlinewidth":0,"ticks":""},"type":"mesh3d"}],"parcoords":[{"line":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"parcoords"}],"scatter3d":[{"line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatter3d"}],"scattercarpet":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattercarpet"}],"scattergeo":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattergeo"}],"scattergl":[{"marker":{"line":{"color":"#283442"}},"type":"scattergl"}],"scattermapbox":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattermapbox"}],"scatterpolargl":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatterpolargl"}],"scatterpolar":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatterpolar"}],"scatter":[{"marker":{"line":{"color":"#283442"}},"type":"scatter"}],"scatterternary":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatterternary"}],"surface":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0,"#0d0887"],[0.111111111111111,"#46039f"],[0.222222222222222,"#7201a8"],[0.333333333333333,"#9c179e"],[0.444444444444444,"#bd3786"],[0.555555555555556,"#d8576b"],[0.666666666666667,"#ed7953"],[0.777777777777778,"#fb9f3a"],[0.888888888888889,"#fdca26"],[1,"#f0f921"]],"type":"surface"}],"table":[{"cells":{"fill":{"color":"#506784"},"line":{"color":"rgb(17,17,17)"}},"header":{"fill":{"color":"#2a3f5f"},"line":{"color":"rgb(17,17,17)"}},"type":"table"}]},"layout":{"annotationdefaults":{"arrowcolor":"#f2f5fa","arrowhead":0,"arrowwidth":1},"colorscale":{"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]],"sequential":[[0,"#0d0887"],[0.111111111111111,"#46039f"],[0.222222222222222,"#7201a8"],[0.333333333333333,"#9c179e"],[0.444444444444444,"#bd3786"],[0.555555555555556,"#d8576b"],[0.666666666666667,"#ed7953"],[0.777777777777778,"#fb9f3a"],[0.888888888888889,"#fdca26"],[1,"#f0f921"]],"sequentialminus":[[0,"#0d0887"],[0.111111111111111,"#46039f"],[0.222222222222222,"#7201a8"],[0.333333333333333,"#9c179e"],[0.444444444444444,"#bd3786"],[0.555555555555556,"#d8576b"],[0.666666666666667,"#ed7953"],[0.777777777777778,"#fb9f3a"],[0.888888888888889,"#fdca26"],[1,"#f0f921"]]},"colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#f2f5fa"},"geo":{"bgcolor":"rgb(17,17,17)","lakecolor":"rgb(17,17,17)","landcolor":"rgb(17,17,17)","showlakes":true,"showland":true,"subunitcolor":"#506784"},"hoverlabel":{"align":"left"},"hovermode":"closest","mapbox":{"style":"dark"},"paper_bgcolor":"rgb(17,17,17)","plot_bgcolor":"rgb(17,17,17)","polar":{"angularaxis":{"gridcolor":"#506784","linecolor":"#506784","ticks":""},"bgcolor":"rgb(17,17,17)","radialaxis":{"gridcolor":"#506784","linecolor":"#506784","ticks":""}},"scene":{"xaxis":{"backgroundcolor":"rgb(17,17,17)","gridcolor":"#506784","gridwidth":2,"linecolor":"#506784","showbackground":true,"ticks":"","zerolinecolor":"#C8D4E3"},"yaxis":{"backgroundcolor":"rgb(17,17,17)","gridcolor":"#506784","gridwidth":2,"linecolor":"#506784","showbackground":true,"ticks":"","zerolinecolor":"#C8D4E3"},"zaxis":{"backgroundcolor":"rgb(17,17,17)","gridcolor":"#506784","gridwidth":2,"linecolor":"#506784","showbackground":true,"ticks":"","zerolinecolor":"#C8D4E3"}},"shapedefaults":{"line":{"color":"#f2f5fa"}},"sliderdefaults":{"bgcolor":"#C8D4E3","bordercolor":"rgb(17,17,17)","borderwidth":1,"tickwidth":0},"ternary":{"aaxis":{"gridcolor":"#506784","linecolor":"#506784","ticks":""},"baxis":{"gridcolor":"#506784","linecolor":"#506784","ticks":""},"bgcolor":"rgb(17,17,17)","caxis":{"gridcolor":"#506784","linecolor":"#506784","ticks":""}},"title":{"x":0.05},"updatemenudefaults":{"bgcolor":"#506784","borderwidth":0},"xaxis":{"automargin":true,"gridcolor":"#283442","linecolor":"#506784","ticks":"","zerolinecolor":"#283442","zerolinewidth":2},"yaxis":{"automargin":true,"gridcolor":"#283442","linecolor":"#506784","ticks":"","zerolinecolor":"#283442","zerolinewidth":2}}},"yaxis":{"domain":[0,1],"automargin":true,"title":{"text":"Quantidade de registros"}},"xaxis":{"domain":[0,1],"automargin":true,"title":{"text":"Raios detectados a cada 12 minutos"}},"title":{"text":"Frequência do número de raios detectados a cada 12 minutos"},"hovermode":"closest","showlegend":true},"attrs":[],"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.2,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script><!--/html_preserve-->


Do ponto de vista físico, os sistemas precipitantes são classificados em 
estratiformes ou convectivos \cite{damian2011duas}. Essa classificação é baseada 
no trabalho de [@steiner1995climatological], que faz uso principalmente dos 
índices de refletividade obtidos por meio de radar. Enquanto nos sistemas 
estratiformes as chuvas acontecem de forma moderada e com distribuição uniforme, 
nos sistemas convectivos, elas acontecem de forma mais intensa e concentrada, 
caracterizando o tempo severo. As descargas atmosféricas são fenômenos que 
acontecem principalmente nos sistemas convectivos. 

Os dados utilizados neste trabalho são referentes ao segundo Período de Operação 
Intensiva, que como supracitado, corresponde ainda ao período de seca na região.
Sendo assim, as chuvas acontecem com pouca frequência e são oriundas 
principalmente de sistemas convectivos. Esse comportamento pode ser observado no 
gráfico da Figura \ref{fig:lightnings-histogram}, onde durante todo o período de 
observação, somente em alguns dias houveram ocorrência de raios, e na maioria 
dos dias em que aconteceram, a atividade elétrica se manifestou de forma intensa
.






