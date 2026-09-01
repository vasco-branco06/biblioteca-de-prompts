---
id: PER-01
nome: Arrumar o código por dentro com rede de segurança
categoria: performance
nivel: recomendado
modo: execucao
origem: ccp-37
gatilhos:
  - isto está uma confusão, arruma
  - quero limpar o código sem partir nada
  - dá para organizar isto melhor
  - o código funciona mas está mal feito
  - preciso de refatorar
nao_usar_quando:
  - a arrumação implica mudar o que a aplicação faz, e aí é outra tarefa
  - o ficheiro é enorme e o objetivo é dividi-lo, usar PER-09
  - o projeto está no meio de uma correção urgente
variaveis:
  - nome: alvo
    descricao: que parte do código arrumar
    obrigatoria: true
    omissao: perguntar, porque arrumar tudo de uma vez é o caminho para partir tudo de uma vez
  - nome: comando_testes
    descricao: como se correm os testes neste projeto
    obrigatoria: false
    omissao: detetar no projeto, e se não existirem testes dizer que o primeiro passo é criá-los
encadeia_com: [PER-09, PER-08, TES-02]
---

## Prompt

Vais arrumar {{alvo}} por dentro sem mudar nada do que a aplicação faz. Antes de
tocares em código:

1. Guarda o estado atual num ponto de retorno, para eu poder voltar. Confirma-me
   que ficou guardado.
2. Verifica se existem testes que protegem esta parte. Se não existirem, escreve
   primeiro testes que capturem o que a aplicação faz hoje. Mesmo que aches que
   tem defeitos, captura o comportamento atual e não o ideal. Corrigir defeitos é
   outra tarefa e não se mistura com esta.
3. Corre {{comando_testes}} e mostra-me que passam antes de começares. Se já
   houver testes a falhar, para e diz, porque não dá para distinguir o que
   partiste do que já estava partido.

Só depois arruma, em passos pequenos, correndo os testes a cada passo. Se um
teste passar a falhar, para nesse ponto e mostra-me antes de continuares.

No fim, confirma explicitamente que o comportamento é igual ao do início, e
mostra o resultado dos testes.

Não acrescentes funcionalidades, não corrijas defeitos que encontres pelo
caminho, não mudes nomes de coisas que estão a ser usadas fora daqui. Se
encontrares um defeito, aponta-o numa lista à parte para tratarmos depois.

## Porque importa

Arrumar código é a atividade que mais vezes parte coisas sem ninguém dar por
isso, porque quem arruma tem a certeza de que não mudou nada. Os testes escritos
antes são a única forma de essa certeza ser verificável.

## Como saber se correu bem

- Existe um ponto de retorno guardado antes de qualquer alteração
- Os testes existiam ou foram escritos antes, e passavam antes de começar
- Os testes correram a cada passo, e não só no fim
- O comportamento no fim é igual ao do início
- Os defeitos encontrados ficaram numa lista à parte, por corrigir
