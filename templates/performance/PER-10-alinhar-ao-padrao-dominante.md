---
id: PER-10
nome: Alinhar ao padrão que o projeto já usa
categoria: performance
nivel: situacional
modo: diagnostico
origem: ccp-71
gatilhos:
  - cada parte do código faz as coisas à sua maneira
  - isto está inconsistente
  - construí isto ao longo de várias sessões e ficou tudo diferente
  - qual é a forma certa de fazer isto neste projeto
  - quero uniformizar a maneira de fazer as coisas
nao_usar_quando:
  - o projeto é novo e ainda não tem padrão nenhum estabelecido
  - a inconsistência é visual e não de código, usar EXP-09
  - o padrão dominante está reconhecidamente errado e a decisão é mudá-lo
variaveis:
  - nome: aspetos
    descricao: que aspetos analisar
    obrigatoria: false
    omissao: ir buscar dados, tratar erros, nomear ficheiros e validar formulários
encadeia_com: [PER-08, DOC-04, DOC-02]
---

## Prompt

Só diagnóstico. Analisa como este projeto costuma fazer {{aspetos}}.

Para cada um:

1. Identifica o padrão mais usado, com a contagem: em quantos sítios aparece
   assim, em quantos aparece de outra maneira.
2. Mostra-me os sítios que fogem a esse padrão, com ficheiro e linha.
3. Diz se a fuga tem razão de ser. Nem toda a inconsistência é acidente: às vezes
   um caso é mesmo diferente.

Não inventes um padrão novo melhor do que o que lá está. O objetivo aqui é
coerência com o existente, não elevar a qualidade. Se achares que o padrão
dominante é mau, diz numa nota à parte, mas continua a medir as fugas em relação
a ele.

Dá-me a lista das fugas ordenada da mais fácil de alinhar para a mais complicada,
com o esforço de cada uma.

No fim, escreve o padrão dominante de cada aspeto em duas ou três linhas, numa
forma que eu possa colar no ficheiro de regras do projeto para as próximas
sessões o seguirem sem perguntar.

Não alteres código.

## Porque importa

Cada sessão de trabalho com uma IA tende a introduzir um estilo novo, porque ela
não se lembra do que foi decidido antes. Ao fim de algumas sessões o projeto tem
quatro maneiras de fazer a mesma coisa, e passa a ser preciso perceber as quatro
para mudar qualquer coisa.

## Como saber se correu bem

- Cada padrão dominante vem com a contagem que o sustenta
- As fugas aparecem com ficheiro e linha
- As fugas justificadas estão separadas das acidentais
- Não foi proposto nenhum padrão novo
- Existe um resumo pronto a colar no ficheiro de regras
