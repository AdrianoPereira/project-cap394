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

Do ponto de vista físico, os sistemas precipitantes são classificados em 
estratiformes ou convectivos \cite{damian2011duas}. Essa classificação é baseada 
no trabalho de [@steiner1995climatological], que faz uso principalmente dos 
índices de refletividade obtidos por meio de radar. Enquanto nos sistemas 
estratiformes as chuvas acontecem de forma moderada e com distribuição uniforme, 
nos sistemas convectivos, elas acontecem de forma mais intensa e concentrada, 
caracterizando o tempo severo. As descargas atmosféricas são fenômenos que 
acontecem principalmente nos sistemas convectivos. 


```python
import plotly
import plotly.graph_objs as go
fig = {'data':[go.Scatter(x=[1,2,3,4],y=[1,4,9,16])],
       'layout':go.Layout(title='Plot generated in python')}
```

---


```python
plotly.offline.iplot(fig)
```

# Json export

As an alternative, we export the python figure to json


```python
import json
fig_as_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
```

---

Display plot as a plotly widget from R

and display the figure in R


```r
plotly::as_widget(
  jsonlite::fromJSON(
    reticulate::py$fig_as_json, simplifyVector=FALSE))
```

<!--html_preserve--><div id="htmlwidget-0e6a1d90064a1294e0c8" style="width:672px;height:480px;" class="plotly html-widget"></div>
<script type="application/json" data-for="htmlwidget-0e6a1d90064a1294e0c8">{"x":{"data":[{"x":[1,2,3,4],"y":[1,4,9,16],"type":"scatter","xaxis":"x","yaxis":"y","frame":null}],"layout":{"title":{"text":"Plot generated in python"},"xaxis":{"domain":[0,1],"automargin":true},"yaxis":{"domain":[0,1],"automargin":true},"hovermode":"closest","showlegend":false},"attrs":[],"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.2,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script><!--/html_preserve-->
