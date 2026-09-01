---
id: DIA-04
nome: Voltar atrás na última alteração
categoria: diagnostico
nivel: recomendado
modo: execucao
origem: ccp-13
gatilhos:
  - desfaz o que fizeste
  - volta atrás
  - isso piorou, anula
  - quero como estava antes
  - esquece essa alteração
nao_usar_quando:
  - as alterações a desfazer já foram guardadas há muito e outras coisas foram construídas por cima
  - o objetivo é recuperar um ficheiro apagado, usar DIA-07
  - ainda não se sabe se a alteração é a culpada, usar DIA-02 primeiro
variaveis:
  - nome: alvo
    descricao: o que se quer desfazer
    obrigatoria: false
    omissao: assumir as alterações feitas desde o último ponto guardado e dizer quais são
encadeia_com: [DIA-02, CTL-03]
---

## Prompt

Quero desfazer {{alvo}} e deixar o projeto como estava antes.

Antes de executares seja o que for:

1. Mostra-me tudo o que está alterado neste momento, ficheiro a ficheiro.
2. Diz em palavras simples o que vais desfazer e o que vai desaparecer com isso.
3. Diz-me claramente o que fica perdido para sempre e o que continua recuperável
   depois desta operação.
4. Se houver alterações misturadas, umas que quero manter e outras não, separa-as
   e pergunta quais mantenho, em vez de desfazeres tudo em bloco.

Espera pelo meu OK. Só depois executas.

Se o que eu pedir for irrecuperável, diz-me isso e propõe primeiro a alternativa
que guarda uma cópia do estado atual antes de desfazer. Prefiro um passo a mais
do que perder trabalho.

## Porque importa

Desfazer é a operação que mais vezes destrói trabalho por engano, porque se
executa depressa e no meio da frustração. Ver a lista do que vai desaparecer,
antes de desaparecer, é o que separa um recuo controlado de uma perda.

## Como saber se correu bem

- A lista do que está alterado foi mostrada antes de qualquer ação
- Ficou claro o que se perde e o que continua recuperável
- As alterações a manter foram separadas das que se desfazem
- Esperou pela autorização em vez de executar logo
- Existe cópia do estado anterior se o que se desfez era irrecuperável
