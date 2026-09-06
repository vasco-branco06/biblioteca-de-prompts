---
id: EST-02
nome: Ficha de estudo com progressão por níveis e flashcards
categoria: estudo
nivel: recomendado
modo: execucao
origem: novo
gatilhos:
  - tenho teste na próxima semana
  - preciso de decorar isto
  - como é que estudo esta matéria
  - quero fazer flashcards disto
  - tenho de saber isto de cor
nao_usar_quando:
  - o objetivo é compreender um documento e não fixá-lo, usar EST-01
  - o que trava é um conceito específico que não se percebe, usar EST-05
  - o trabalho é escrito e não avaliado por memória, usar EST-04
variaveis:
  - nome: materia
    descricao: o que estudar, com o documento ou o programa
    obrigatoria: true
    omissao: perguntar
  - nome: prazo
    descricao: quando é a avaliação
    obrigatoria: false
    omissao: perguntar, porque define o calendário de repetições
  - nome: nivel_atual
    descricao: o que já se sabe da matéria
    obrigatoria: false
    omissao: assumir contacto inicial e declarar a assunção
  - nome: formato_saida
    descricao: onde ficam a ficha e os cartões
    obrigatoria: false
    omissao: ficheiro markdown, com os cartões numa tabela de pergunta e resposta
encadeia_com: [EST-01, EST-05]
---

## Prompt

Constrói uma ficha de estudo de {{materia}} para quem está em {{nivel_atual}},
com avaliação em {{prazo}}. Entrega em {{formato_saida}} e diz-me antes o que vais
criar e onde.

Organiza a matéria em três níveis, e deixa claro que o segundo não se faz sem o
primeiro:

1. **Reconhecer.** Vocabulário e factos. O que é cada coisa, em uma frase.
2. **Explicar.** Como funciona, porque é assim, como se relaciona com o resto.
   Este nível responde a perguntas que começam por porquê.
3. **Aplicar.** Problemas, casos e exceções. Onde a regra deixa de valer.

Para cada nível, diz o que se tem de conseguir fazer para passar ao seguinte.

Depois faz os flashcards, com estas regras:

- Um facto por cartão. Um cartão com três coisas não se aprende, decora-se mal.
- A pergunta obriga a produzir a resposta, não a reconhecê-la. Nada de escolha
  múltipla, nada de perguntas de sim ou não.
- A resposta cabe em duas linhas. Se não couber, o cartão é para dividir.
- Inclui cartões de nível dois e três, e não só de vocabulário. Saber a definição
  e não saber para que serve é o modo típico de chumbar tendo estudado.

No fim, monta o calendário até {{prazo}}: que dias, que níveis, e onde entram as
revisões do que já foi estudado. As repetições espaçadas valem mais do que horas
seguidas, e o calendário tem de as prever mesmo com pouco tempo.

Marca à parte o que a ficha não cobre da matéria, e porquê.

## Porque importa

Reler apunhamentos dá a sensação de saber, porque se reconhece o texto. Só
quando se tenta responder sem ver é que se descobre o que não está lá. A ficha
existe para forçar essa tentativa antes do dia da avaliação.

## Como saber se correu bem

- Os três níveis estão separados e cada um diz o que é preciso para avançar
- Cada cartão tem um só facto e obriga a produzir a resposta
- Há cartões de explicar e de aplicar, e não só de vocabulário
- O calendário chega até ao prazo e inclui revisões
- Está dito o que ficou de fora da matéria
