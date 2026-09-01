---
id: DIA-05
nome: Provar a causa com registos, em vez de adivinhar
categoria: diagnostico
nivel: situacional
modo: execucao
origem: ccp-47
gatilhos:
  - já tentámos três correções e continua igual
  - não sabemos porque é que isto acontece
  - estás a adivinhar
  - preciso de perceber o que se passa lá dentro
  - o erro não faz sentido nenhum
nao_usar_quando:
  - a causa já está identificada e falta corrigir
  - o problema só acontece às vezes e não se consegue repetir, usar DIA-06
  - basta olhar para o histórico de alterações, usar DIA-02
variaveis:
  - nome: problema
    descricao: o comportamento errado, e como o reproduzir
    obrigatoria: true
    omissao: perguntar, incluindo os passos exatos para o fazer acontecer
  - nome: onde_leio
    descricao: onde é que eu vejo as mensagens, consola do navegador, terminal ou registos do serviço
    obrigatoria: false
    omissao: escolher o sítio mais provável e explicar como lá chegar
encadeia_com: [DIA-01, DIA-06, TES-05]
---

## Prompt

Não sabemos porque {{problema}} acontece, e não quero que adivinhes. Vamos provar
a causa.

**Passo 1.** Dá-me as três causas mais prováveis, ordenadas, e o que esperarias
ver em {{onde_leio}} se cada uma fosse a verdadeira. Sê concreto: que valor, em
que ponto.

**Passo 2.** Acrescenta registos temporários nos pontos que separam as hipóteses:
onde os dados entram, onde são transformados, onde saem. Marca cada um de forma
a ser fácil de encontrar e de remover depois. Diz-me exatamente que ação eu tenho
de fazer para os registos aparecerem, e onde os vou ler.

**Passo 3.** Eu colo-te aqui o que apareceu. Só com essa prova é que dizes qual
das causas é a verdadeira. Se o que aparecer não bater com nenhuma das três,
propõe hipóteses novas em vez de forçar uma das antigas.

Não corrijas nada enquanto a causa não estiver provada pelos registos. Quando
estiver, propõe a correção e espera.

No fim, depois de corrigido e confirmado, remove todos os registos temporários e
mostra-me a lista do que removeste.

## Porque importa

Corrigir sem saber a causa tapa o sintoma e deixa o problema à espera. Pior:
cada tentativa acrescenta código que ninguém percebe porque lá está. Ver os
valores reais a passar pelo programa transforma a discussão numa observação.

## Como saber se correu bem

- Vieram três hipóteses antes de qualquer alteração
- Cada uma dizia o que se esperaria observar
- Os registos foram colocados nos pontos que separam as hipóteses
- Nenhuma correção foi feita antes de eu colar o resultado
- Os registos temporários foram removidos no fim, com a lista do que saiu
