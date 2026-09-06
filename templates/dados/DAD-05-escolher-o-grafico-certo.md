---
id: DAD-05
nome: Escolher o gráfico certo para a mensagem
categoria: dados
nivel: recomendado
modo: diagnostico
origem: novo
gatilhos:
  - que gráfico é que uso para isto
  - este gráfico não se percebe
  - quero mostrar isto numa apresentação
  - faço um gráfico de barras ou de linhas
  - como é que mostro esta evolução
nao_usar_quando:
  - os dados ainda não foram verificados nem analisados, usar DAD-01 ou DAD-02
  - a mensagem ainda não está decidida, e aí a escolha é impossível
  - o que se quer é um painel com muitos indicadores e não um gráfico
variaveis:
  - nome: mensagem
    descricao: a frase que quem vir o gráfico tem de ficar a saber
    obrigatoria: true
    omissao: perguntar, e insistir até ser uma frase com sujeito e verbo
  - nome: dados
    descricao: o que existe, com as colunas e o número de categorias
    obrigatoria: false
    omissao: perguntar quais são as colunas em causa
  - nome: publico
    descricao: quem vê e em que contexto
    obrigatoria: false
    omissao: assumir apresentação a quem não conhece os dados, e declarar a assunção
  - nome: meio
    descricao: onde aparece, slide, relatório impresso, ecrã, telemóvel
    obrigatoria: false
    omissao: assumir slide projetado, que é o mais restritivo
encadeia_com: [DAD-02, DAD-04, EXP-09]
---

## Prompt

Só diagnóstico e recomendação, não construas o gráfico ainda.

A mensagem é {{mensagem}}, para {{publico}}, em {{meio}}, com {{dados}}.

Começa por confirmar a mensagem. Se ela for do género mostrar as vendas, ainda
não é mensagem, é assunto. Uma mensagem é uma frase que se pode contestar: as
vendas caíram no norte desde março. É a partir dela que a escolha se faz, e não
a partir do formato dos dados.

Classifica o que a mensagem pede, porque cada tipo tem uma resposta diferente:

- **Comparar** grandezas entre categorias
- **Compor**, mostrar partes de um todo
- **Distribuir**, mostrar como os valores se espalham
- **Evoluir** ao longo do tempo
- **Relacionar** duas variáveis

Recomenda um gráfico, com a razão, e diz que segunda opção existe e quando é que
ela seria melhor. Um só, não uma galeria.

Diz também o que fazer com o gráfico para a mensagem chegar:

1. O título é a mensagem escrita, não a descrição do eixo.
2. O que destacar e o que empurrar para segundo plano. Se tudo tiver a mesma
   cor, não há mensagem; se tudo tiver cores diferentes, também não.
3. Que eixo começa em zero e porquê. Cortar o eixo das quantidades exagera
   diferenças e é a forma mais comum de enganar sem mentir.
4. Quantas categorias mostrar antes de agrupar o resto.
5. Quanto texto sobrevive em {{meio}}. O que se lê num relatório não se lê num
   slide a cinco metros.

Avisa-me se algum destes aparecer: sectores com mais de cinco fatias, dois eixos
verticais diferentes no mesmo gráfico, três dimensões, ou distinções feitas só
por cor sem outro sinal. Todos parecem bem e todos dificultam a leitura.

Se os dados não sustentarem a mensagem, diz isso antes de escolher o gráfico.
Nenhuma escolha de formato salva uma conclusão que os dados não suportam.

## Porque importa

Escolhe-se quase sempre o gráfico pelo formato dos dados, e o resultado é uma
imagem tecnicamente correta que não diz nada. Partir da frase que se quer passar
inverte a ordem e faz o gráfico decidir-se sozinho.

## Como saber se correu bem

- A mensagem foi confirmada como frase contestável antes de qualquer escolha
- Foi identificado o que a mensagem pede, comparar, compor, distribuir, evoluir ou relacionar
- Há uma recomendação, com segunda opção e a condição em que ela ganha
- Está dito o que destacar e como tratar os eixos
- Se os dados não sustentam a mensagem, isso foi dito primeiro
