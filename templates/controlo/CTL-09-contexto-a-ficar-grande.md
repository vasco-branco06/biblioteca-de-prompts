---
id: CTL-09
nome: A conversa está a ficar grande
categoria: controlo
nivel: situacional
modo: diagnostico
origem: ccp-76
gatilhos:
  - esta conversa já vai longa
  - andas a repetir-te
  - já não te lembras do que combinámos ao princípio
  - isto está a ficar caro
  - acho que já te perdeste
nao_usar_quando:
  - a conversa está no início
  - o que se quer é registar decisões de forma permanente, usar DOC-06 ou CTL-07
  - o problema é a leitura de muitos ficheiros e não o histórico, usar CTL-08
variaveis:
  - nome: proximo_passo
    descricao: o que vem a seguir, para se saber o que é preciso manter
    obrigatoria: false
    omissao: perguntar, porque sem isto não se sabe o que se pode descartar
encadeia_com: [CTL-08, DOC-06, CTL-07]
---

## Prompt

Esta conversa já está longa. Resume o que é preciso manter para continuarmos com
{{proximo_passo}}, para podermos descartar o resto.

O resumo tem de conter, e nada mais:

1. **O objetivo.** O que estamos a tentar conseguir, em uma frase.
2. **Decisões tomadas.** Cada uma em uma linha, com a razão em meia linha. Isto
   é o mais importante: sem as razões, as decisões voltam a ser discutidas.
3. **Estado atual.** O que já está feito e a funcionar, o que está feito mas por
   verificar, o que falta.
4. **Restrições e preferências** que eu disse durante a conversa e que continuam
   a valer.
5. **O que estava a acontecer neste momento**, com detalhe suficiente para se
   retomar sem perguntas.

Deixa de fora as tentativas que não resultaram, as explicações já dadas, o
conteúdo de ficheiros e os caminhos abandonados. Se algum caminho foi abandonado
por uma razão importante, essa razão é uma decisão e vai para o ponto dois.

Antes de descartarmos, diz-me se alguma coisa deste resumo merece ser escrita num
ficheiro do projeto, porque vai voltar a fazer falta noutra sessão. As decisões
costumam merecer.

## Porque importa

Quanto mais longa a conversa, mais lenta e cara fica cada resposta, e mais fácil
é perder-se o que ficou combinado no início. Um resumo do essencial permite
continuar leve sem perder o fio.

## Como saber se correu bem

- As decisões vêm com a razão de cada uma
- O estado distingue o que está verificado do que não está
- As tentativas falhadas e as explicações já dadas ficaram de fora
- O ponto de retoma tem detalhe suficiente para continuar sem perguntas
- Foi assinalado o que merece ser guardado em ficheiro
