---
id: EST-05
nome: Explicação progressiva de um conceito difícil
categoria: estudo
nivel: recomendado
modo: diagnostico
origem: novo
gatilhos:
  - não estou a perceber isto de todo
  - explica-me isto do início
  - já li três vezes e não entra
  - o que é isto na prática
  - toda a gente diz que é simples e eu não percebo
nao_usar_quando:
  - o que se quer é fixar matéria já compreendida, usar EST-02
  - o pedido é resumir um documento inteiro, usar EST-01
  - a dúvida é sobre o que a IA acabou de fazer no projeto, usar DOC-01
variaveis:
  - nome: conceito
    descricao: o que não se está a perceber
    obrigatoria: true
    omissao: perguntar
  - nome: base
    descricao: o que a pessoa já sabe e que sirva de apoio
    obrigatoria: false
    omissao: perguntar uma coisa que ela domine e usar isso como ponto de partida
  - nome: para_que
    descricao: para que precisa de perceber isto
    obrigatoria: false
    omissao: perguntar, porque decide onde parar a explicação
encadeia_com: [EST-02, EST-01, DOC-01]
---

## Prompt

Explica-me {{conceito}}, sabendo que preciso disto para {{para_que}} e que já
domino {{base}}. Não alteres nem produzas ficheiros, só explica.

Faz quatro passagens, por esta ordem, e para no fim de cada uma para eu dizer se
já cheguei:

1. **A analogia.** Uma comparação com uma coisa que eu já conheço, ligada a
   {{base}}. Uma só, bem escolhida. Três analogias seguidas confundem em vez de
   ajudarem.
2. **O mecanismo.** O que acontece, por que ordem, e porquê. Ainda sem
   formalismo, mas já com as peças certas e os nomes verdadeiros de cada uma.
3. **A definição formal.** A forma como aparece nos livros e nos testes, agora
   que já sei o que ela quer dizer.
4. **Onde a analogia falha.** Esta passagem é a mais importante e a que quase
   nunca aparece. Toda a analogia mente nalgum ponto, e é exatamente aí que se
   erra depois nos exercícios. Diz-me em que ponto a comparação deixa de valer e
   o que acontece na realidade nesse ponto.

Depois faz-me duas perguntas de verificação. Não perguntas de definição, que se
respondem repetindo o que disseste. Perguntas em que eu tenho de aplicar o
conceito a um caso que não usaste. Espera pelas minhas respostas e diz-me onde
ainda estou ao lado.

Se o conceito depender de outro que eu provavelmente não domino, diz isso antes
de começares e pergunta se quero explicar esse primeiro. Explicar por cima de um
buraco não resulta.

## Porque importa

Um conceito não entra por repetição, entra quando se liga a alguma coisa que já
se sabe. E a parte que quase toda a gente salta, dizer onde a comparação deixa
de servir, é a que evita os erros seguintes, porque é aí que a intuição
emprestada engana.

## Como saber se correu bem

- Houve uma só analogia, ligada a algo que eu já domino
- As quatro passagens vieram por ordem, com paragem entre elas
- A passagem sobre os limites da analogia existe e é concreta
- As perguntas de verificação obrigam a aplicar, não a repetir
- Os pré-requisitos em falta foram assinalados antes de começar
