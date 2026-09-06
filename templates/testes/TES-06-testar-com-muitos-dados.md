---
id: TES-06
nome: Testar com muitos dados, não com três exemplos
categoria: testes
nivel: situacional
modo: execucao
origem: ccp-75
gatilhos:
  - quantos utilizadores é que isto aguenta
  - com poucos dados funciona bem
  - e se tiver mil registos
  - aguenta muitas pessoas ao mesmo tempo
  - isto aguenta o lançamento
  - não sei se isto escala
nao_usar_quando:
  - já se sabe que está lento e onde, usar PER-03 ou PER-06
  - o projeto nunca vai ter mais do que alguns registos
  - não existe forma de gerar dados sem tocar nos reais
variaveis:
  - nome: alvo
    descricao: o ecrã ou funcionalidade a testar
    obrigatoria: true
    omissao: perguntar
  - nome: volume
    descricao: quantos registos gerar
    obrigatoria: false
    omissao: cinco mil registos, e subir em degraus se aguentar
encadeia_com: [PER-06, PER-03, TES-04]
---

## Prompt

Isto funciona com os poucos exemplos que tenho. Quero saber se aguenta a
realidade. Não mudes o desenho ainda: primeiro mede.

**Passo 1.** Cria dados de teste realistas em quantidade, {{volume}}, sem tocar
nos meus dados reais. Diz-me antes onde os vais criar e como os removo depois.
Realistas quer dizer com a variedade que os reais têm: nomes de comprimentos
diferentes, campos opcionais por preencher, acentos, datas espalhadas no tempo.

**Passo 2.** Abre {{alvo}} com esses dados e mede. Responde com números, não com
impressões:

- quanto demora a abrir
- fica lento, trava, ou deixa de responder
- alguma coisa deixa de caber ou de aparecer
- a que volume começa a doer

Mede em degraus, por exemplo cem, mil, cinco mil, e mostra a curva. O que
interessa não é o valor num ponto, é a forma como cresce: se duplicar os dados
quadruplicar o tempo, o problema aparece muito antes do que se pensa.

**Passo 3.** Só depois propõe o que melhorar, do mais simples para o mais
complexo, com o ganho esperado de cada um.

No fim, remove os dados de teste e confirma que ficaram removidos.

## Porque importa

Tudo parece rápido com três exemplos. O momento em que o problema aparece é o
momento em que o projeto começa a ter uso a sério, que é o pior momento possível
para descobrir que não aguenta.

## Como saber se correu bem

- Os dados de teste foram criados sem tocar nos dados reais
- Os dados gerados têm a variedade dos reais
- As respostas vêm com números medidos e não com impressões
- A medição foi feita em degraus e mostra como o tempo cresce
- Os dados de teste foram removidos no fim
