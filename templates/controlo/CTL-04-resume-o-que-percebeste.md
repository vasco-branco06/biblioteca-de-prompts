---
id: CTL-04
nome: Resume o que percebeste antes de avançar
categoria: controlo
nivel: recomendado
modo: diagnostico
origem: ccp-14
gatilhos:
  - antes de avançares diz-me o que percebeste
  - quero confirmar que estamos a falar do mesmo
  - repete-me o que te pedi
  - não tenho a certeza de que me percebeste
  - explica-me o que vais fazer em três frases
nao_usar_quando:
  - o pedido é trivial e o resumo demora mais do que fazê-lo
  - o que se quer é um plano completo, usar PLA-01
  - o trabalho já começou e o que falta é explicar o que foi feito, usar DOC-03
variaveis:
  - nome: pedido
    descricao: o que foi pedido
    obrigatoria: false
    omissao: usar a última coisa pedida na conversa
encadeia_com: [PLA-01, CTL-05, DOC-01]
---

## Prompt

Antes de avançares com {{pedido}}, resume em três frases simples o que percebeste
que eu quero. Não comeces a trabalhar.

As três frases são:

1. O que queres que aconteça no fim.
2. O que não vou tocar.
3. O que estou a assumir que não me disseste.

A terceira é a que interessa mesmo. Se estiver vazia é porque não olhaste com
atenção: há sempre alguma coisa assumida.

Escreve em linguagem simples, sem termos técnicos, para eu poder corrigir sem
precisar de perceber de código.

Se depois do resumo continuares com dúvidas que mudem o resultado, faz as
perguntas em vez de escolheres. Se as dúvidas não mudarem o resultado, decide e
diz o que decidiste.

Espera pela minha confirmação.

## Porque importa

Um mal-entendido apanhado aqui custa uma frase. Apanhado depois do trabalho feito
custa o trabalho todo. É a verificação mais barata que existe e a que mais vezes
se salta por parecer desnecessária.

## Como saber se correu bem

- São três frases e não um parágrafo
- Está dito o que não vai ser tocado
- As assunções estão explícitas e a lista não está vazia
- Está em linguagem que eu percebo sem saber programar
- Parou e esperou pela confirmação
