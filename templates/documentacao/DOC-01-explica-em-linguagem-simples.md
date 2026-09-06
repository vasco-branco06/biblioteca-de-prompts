---
id: DOC-01
nome: Explica em linguagem simples
categoria: documentacao
nivel: essencial
modo: diagnostico
origem: ccp-3
gatilhos:
  - explica-me lá o que fizeste aí
  - não percebi nada do que disseste
  - não percebi o que mudaste
  - o que é isso que acabaste de dizer
  - fala como se eu não soubesse programar
  - explica isso por palavras simples
nao_usar_quando:
  - o pedido é uma lição do que mudou no projeto para aprender com ela, usar DOC-03
  - o que se quer é um documento escrito e não uma explicação, usar DOC-04 ou DOC-05
  - a explicação pedida é sobre uma decisão a registar, usar DOC-06
variaveis:
  - nome: assunto
    descricao: o que precisa de ser explicado
    obrigatoria: false
    omissao: usar a última coisa que foi dita e confirmar numa linha qual foi
encadeia_com: [DOC-03, CTL-04]
---

## Prompt

Explica-me {{assunto}} como se eu nunca tivesse programado. Não alteres nada do
projeto, só explica.

Regras:

- Nenhum termo técnico sem o explicares na primeira vez que o usas, e explica-o
  com uma comparação do mundo real, não com outro termo técnico.
- Diz primeiro o que isto significa para mim na prática, e só depois como
  funciona. Se eu não precisar da segunda parte, ficamos pela primeira.
- Nada de siglas nuas.
- Se houve uma decisão pelo meio, diz qual foi a alternativa que não seguiste e
  porquê, numa frase.

No fim, diz-me em uma linha o que muda para mim por causa disto: se tenho de
fazer alguma coisa, se há algum risco, ou se posso simplesmente continuar.

Não simplifiques ao ponto de ficar errado. Se alguma coisa for mesmo complicada,
diz que é complicada e explica só a parte que me interessa decidir, em vez de
inventares uma analogia que engana.

## Porque importa

Não é preciso perceber o código, mas é preciso perceber o que se passa no projeto
para se poder decidir. Sem isso, aprovar trabalho é assinar por baixo às cegas, e
qualquer erro só aparece quando já é caro.

## Como saber se correu bem

- Nenhum termo técnico ficou por explicar
- As comparações são com coisas do mundo real
- O que significa para mim veio antes de como funciona
- Está dito em uma linha se tenho de fazer alguma coisa
- Nada foi simplificado ao ponto de ficar errado
