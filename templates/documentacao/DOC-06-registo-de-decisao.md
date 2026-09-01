---
id: DOC-06
nome: Registar a decisão e as alternativas rejeitadas
categoria: documentacao
nivel: situacional
modo: execucao
origem: ccp-78
gatilhos:
  - acabámos de decidir uma coisa importante
  - regista esta decisão
  - não quero voltar a discutir isto daqui a um mês
  - porque é que escolhemos isto mesmo
  - guarda o porquê desta escolha
nao_usar_quando:
  - a decisão é pequena e reversível numa linha
  - a decisão é uma regra de comportamento permanente, e aí vai para o ficheiro de regras, usar CTL-07
  - a decisão ainda não foi tomada, usar PLA-09
variaveis:
  - nome: decisao
    descricao: o que ficou decidido
    obrigatoria: true
    omissao: perguntar
  - nome: pasta_decisoes
    descricao: onde ficam guardados estes registos
    obrigatoria: false
    omissao: docs/decisoes na raiz do projeto, com o ficheiro numerado e datado
encadeia_com: [PLA-09, DOC-02, DOC-03]
---

## Prompt

Escreve o registo de {{decisao}} num ficheiro dentro de {{pasta_decisoes}}, com
número e data no nome.

Estrutura:

1. **Contexto.** Que problema obrigou a decidir. Sem isto, o registo não se
   percebe daqui a seis meses.
2. **Decisão.** O que ficou escolhido, em uma frase, sem rodeios.
3. **Alternativas rejeitadas.** Pelo menos duas, cada uma com o motivo real de
   ter sido posta de lado. Motivo real quer dizer o que pesou mesmo, incluindo se
   foi falta de tempo ou de conhecimento. Um registo que finge que a decisão foi
   puramente técnica não serve para nada mais tarde.
4. **Consequências.** O que fica mais fácil e o que fica mais difícil por causa
   desta escolha. As duas listas, não só a primeira.
5. **Quando reconsiderar.** O sinal concreto que dirá que esta decisão deixou de
   servir. Um número, um acontecimento, um limite.

Escreve em linguagem simples, assumindo que quem lê nunca programou.

Não escrevas nada que não tenha sido discutido. Se alguma das cinco secções não
tiver conteúdo real, pergunta-me em vez de a preencheres com plausibilidades.
Sobretudo a terceira: se não foram consideradas alternativas, o registo devia
dizer isso.

## Porque importa

Daqui a três semanas ninguém se lembra porque é que se escolheu aquilo, e a
discussão recomeça do zero, muitas vezes chegando à decisão contrária pelas mesmas
razões. O que dá valor a este registo não é a decisão, é a lista do que se
rejeitou e porquê.

## Como saber se correu bem

- As cinco secções existem e nenhuma foi preenchida por plausibilidade
- Há pelo menos duas alternativas rejeitadas com motivo real
- As consequências incluem o que fica mais difícil
- O sinal para reconsiderar é concreto e verificável
- Está escrito em linguagem que se percebe sem saber programar
