---
title: "Introdução"
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

# Introdução
As descargas elétricas atmosféricas têm sido estudadas desde os tempos de 
Benjamin Franklin (1706-1790), quando o próprio cientista, em 1752, realizou um 
dos primeiros experimentos com este fenômeno da natureza. O experimento 
consistiu em soltar, durante uma tempestade, uma pipa manipulada por um fio de 
seda, o instrumento recebia cargas elétricas advindas de raios e descia até uma 
chave de metal onde o fio estava preso. Com isso, Franklin acabará de descobrir 
de forma concisa a natureza elétrica das descargas elétricas, dando origem ao 
primeiro para-raios [@krider2006benjamin]. 

## Características das descargas atmosféricas

As descargas atmosféricas são eventos de natureza aleatória que advém de fortes 
interações entre os centros de cargas em sistemas convectivos. Essas interações 
acabam desenvolvendo forte atividade elétrica, que podendo chegar na ordem de 
milhares de ampères, e que normalmente são acompanhados por intensos efeitos 
sonoros e luminosos [@souza2017analise]. Os raios podem ser dos 
seguintes tipos: intranuvem, quando as descargas acontecem dentro de uma única
nuvem, nuvem-para-nuvem, quando cargas com polaridades opostas são conectadas 
de um raio em nuvens separadas, nuvens-para-ar, quando as descargas 
intra-nuvem extapolam os limites de uma nuvem, e por fim, as descargas 
nuvem-solo, que são quando os raios que atingem o solo [@rakov2007lightning]. 
A Figura \@ref(fig:type-lightning) mostra alguns exemplos dos tipos de 
descargas elétricas mencionados.

<div class="figure">
<img src="images/types-lightning.png" alt="Principais tipos de descargas atmosféricas. Adptado de [NOAA](https://www.nssl.noaa.gov/education/svrwx101/lightning/types/)."  />
<p class="caption">(\#fig:type-lightning)Principais tipos de descargas atmosféricas. Adptado de [NOAA](https://www.nssl.noaa.gov/education/svrwx101/lightning/types/).</p>
</div>


## Consequências provocadas pelos raios

Além de afetarem diretamente na composição química da atmosfera e a qualidade do 
ar na alta troposfera [@weber2005improving], as descargas 
atmosféricas são responsáveis por uma série de impactos socieconômicos. Os raios 
são os principais responsáveis por iniciarem incêndios florestais, causar 
interrupções de serviços de transmissão de energia e comunicação, e também por 
baixas em rebanhos de gado na zona em zona rural [@cardoso2017determinaccao]. 
As descargas atmosféricas estão relacionadas ao alto índice de fatalidades 
contra seres humanos, conforme mostrado no trabalho de [@cardoso2014lightning].

Por ser um país de grande extensão territorial, e está predominantemente 
localizado em zona tropical, o Brasil ocupa uma posição de destaque mundial no 
que diz respeito a grande incidência de raios, chegando a serem registrados 
aproximadamente 77.8 milhões por ano, de acordo com estimativa feita pelo Grupo 
de Eletricidade Atmosférica 
([ELAT](http://www.inpe.br/webelat/homepage/menu/el.atm/perguntas.e.respostas.php)) 
do Instituto Nacional de Pesquisas Espaciais (INPE). Sendo assim, as redes de 
detecção desempenham um papel fundamental no monitoramento de descargas 
elétricas no Brasil, representando grande avanço nas pesquisas correlatas, 
principalmente na prevenção de fatalidades e auxílios em tomadas de decisões 
[@chinchay2018uso]. Além disso, dados de outras fontes também são muito 
utilizados em pesquisas relacionadas às descargas atmosféricas, como dados de 
radares meteorológicos e de satélites [@chinchay2018uso].


## Pesquisas relacionadas à previsão raios

Dentre as pesquisas a respeito das descargas atmosféricas, talvez as que possuam 
maior valor agregado, sejam as pesquisas relacionadas ao desenvolvimento de 
mecanismos de previsão. No trabalho de [@zepka2005estudo], é feito um 
estudo aprofundado com a finalidade de avaliar a viabilidade do desenvolvimento 
de sistemas previsores de descargas elétricas atmosféricas, o autor também 
ressalta também a importância desse tipo de mecanismo para o acompanhamento e 
evolução de tempestades.

Embora tenha sido constatada a real necessidade mecanismos de previsão de 
descargas elétricas, as soluções propostas ainda estão muito escassas 
[@zepka2005estudo]. Sendo assim, este trabalho tem como objetivo realizar a 
análise de atributos de dados meteorológicos, e então propor um sistema de 
previsão de descargas elétricas atmosféricas baseado em abordagens de 
aprendizado de máquina supervisionado. Os dados são referentes aos experimentos 
do CHUVA-Manaus [@machado2014chuva] e GoAmazon [@martin2016introduction], 
realizados na região central da Bacia Amazônica. Além disso, os dados foram 
processados em uma adaptação do algoritmo ForTraCC (*Forecast and Tracking of* 
*Active Convective Cells*) por Pereira [@rebeca2019propriedades].
