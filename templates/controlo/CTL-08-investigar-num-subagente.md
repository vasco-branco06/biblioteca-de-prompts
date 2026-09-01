---
id: CTL-08
nome: Investigar num subagente e receber só o resumo
categoria: controlo
nivel: situacional
modo: diagnostico
origem: ccp-50
gatilhos:
  - antes de mexeres investiga como isto funciona
  - não me encham a conversa com ficheiros todos
  - preciso que percebas o projeto antes de avançar
  - lê isto tudo mas dá-me só o resumo
  - vê como está feita esta parte
nao_usar_quando:
  - a investigação é pequena e cabe em dois ou três ficheiros
  - a conversa está a começar e ainda há espaço de sobra
  - o resultado precisa do detalhe todo e não de um resumo
variaveis:
  - nome: assunto
    descricao: o que investigar
    obrigatoria: true
    omissao: perguntar
  - nome: perguntas
    descricao: as perguntas concretas a que a investigação tem de responder
    obrigatoria: false
    omissao: derivar do assunto e mostrar as perguntas antes de investigar
encadeia_com: [CTL-09, DOC-04, PLA-01]
---

## Prompt

Antes de mexeres em código, lança um subagente para investigar {{assunto}} neste
projeto.

Dá-lhe {{perguntas}} como missão. Mostra-me as perguntas antes de o lançares: se
forem vagas, o resumo vem vago.

O que quero de volta, e só isto:

1. A resposta a cada pergunta, em poucas linhas.
2. Os ficheiros que interessam, com o nome e uma linha a dizer o papel de cada
   um. Não mais de dez.
3. O que o subagente não conseguiu determinar.

Não tragas para aqui o conteúdo dos ficheiros. Não colas trechos de código a não
ser que sejam indispensáveis para eu decidir, e nesse caso poucas linhas.

Se o resumo que voltar não responder às perguntas, diz isso e pergunta outra vez
com perguntas melhores, em vez de me entregares um resumo que não serve.

Depois de teres o resumo, diz-me o que propões fazer e espera.

## Porque importa

Ler muitos ficheiros enche a conversa principal, o que a torna mais lenta, mais
cara, e faz perder de vista o que se estava a fazer. Mandar a leitura pesada para
outro lado e trazer só as conclusões mantém a conversa útil durante muito mais
tempo.

## Como saber se correu bem

- As perguntas foram mostradas antes da investigação
- O resumo responde a cada pergunta em poucas linhas
- A lista de ficheiros é curta e cada um tem o seu papel explicado
- O conteúdo dos ficheiros não foi despejado na conversa
- O que ficou por determinar está dito
