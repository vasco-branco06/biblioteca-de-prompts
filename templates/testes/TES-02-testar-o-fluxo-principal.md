---
id: TES-02
nome: Testar o percurso que não pode falhar
categoria: testes
nivel: recomendado
modo: execucao
origem: ccp-42
gatilhos:
  - quero ser avisado se isto partir
  - o registo não pode falhar nunca
  - preciso de testes para o que é importante
  - já parti isto duas vezes sem dar por isso
  - quero garantir que o principal continua a funcionar
nao_usar_quando:
  - o percurso ainda está a ser desenhado e muda todos os dias
  - o que se quer é uma verificação rápida antes de publicar, usar TES-01
  - o objetivo é reproduzir um defeito concreto, usar TES-05
variaveis:
  - nome: fluxo
    descricao: o percurso a proteger, do primeiro passo ao último
    obrigatoria: true
    omissao: perguntar, e pedir que seja descrito como uma pessoa o faria
  - nome: ferramenta_testes
    descricao: com que ferramenta se escrevem e correm os testes
    obrigatoria: false
    omissao: usar a que o projeto já tem, e se não houver nenhuma propor a mais simples e esperar aprovação
encadeia_com: [TES-01, TES-04, TES-06]
---

## Prompt

Escreve testes que verifiquem que {{fluxo}} funciona de início ao fim, com
{{ferramenta_testes}}.

Antes de escreveres, descreve-me o percurso passo a passo como uma pessoa o faz,
e confirma comigo. O teste tem de seguir esse percurso e não um atalho por
dentro do código: se o teste chamar diretamente as funções, deixa de proteger
contra os problemas que acontecem entre elas.

Cada teste deve:

- partir de um estado limpo e conhecido, sem depender do que ficou de outro teste
- fazer os mesmos passos que uma pessoa faria
- verificar o resultado que a pessoa vê, e não o estado interno
- não depender de dados reais nem escrever nos meus dados reais
- falhar com uma mensagem que diga em que passo parou e o que esperava

Cobre também o que acontece quando o percurso é interrompido a meio, porque na
vida real é o que acontece.

No fim, corre os testes e mostra-me o resultado. Depois estraga uma coisa de
propósito, mostra-me que o teste apanha, e volta a pôr como estava. Um teste que
nunca se viu falhar não prova nada.

Diz-me onde ficaram guardados e como se correm.

## Porque importa

Este é o teste que decide se és tu ou um cliente a descobrir que a inscrição
deixou de funcionar. Cobrir o percurso mais importante vale mais do que cobrir
muitas funções pequenas, porque é onde o estrago é real.

## Como saber se correu bem

- O percurso foi descrito e confirmado antes de o teste ser escrito
- O teste segue os passos de uma pessoa e não atalhos internos
- Não toca nos dados reais
- Foi demonstrado a falhar quando algo é estragado de propósito
- Ficou dito onde está e como se corre
