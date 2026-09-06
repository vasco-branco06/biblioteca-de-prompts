---
id: EST-04
nome: Estrutura de um trabalho académico com os critérios à vista
categoria: estudo
nivel: situacional
modo: execucao
origem: novo
gatilhos:
  - tenho de entregar um trabalho e não sei como o organizar
  - por onde começo este relatório
  - quantas páginas para cada parte
  - tenho a matéria toda mas não sei estruturar
  - como é que estruturo a tese
nao_usar_quando:
  - o pedido é escrever o trabalho e não estruturá-lo
  - faltam as fontes, usar EST-03 primeiro
  - o documento não é avaliado e não tem critérios nem formato exigido
variaveis:
  - nome: tema
    descricao: sobre o que é o trabalho, e a pergunta a que responde
    obrigatoria: true
    omissao: perguntar
  - nome: criterios
    descricao: a grelha de avaliação ou o enunciado
    obrigatoria: false
    omissao: pedir, porque estruturar sem os critérios é adivinhar onde estão as notas
  - nome: extensao
    descricao: limite de páginas ou palavras
    obrigatoria: false
    omissao: perguntar, porque a estrutura depende do espaço
  - nome: prazo
    descricao: quando é a entrega
    obrigatoria: false
    omissao: perguntar, para dividir o trabalho no tempo disponível
encadeia_com: [EST-03, EST-01, PLA-04]
---

## Prompt

Estrutura o trabalho sobre {{tema}}, com {{extensao}}, a entregar em {{prazo}},
avaliado por {{criterios}}. Não escrevas o trabalho. Diz-me antes o que vais
produzir e onde.

Começa por ler os critérios e dizer-me onde está o peso. Se metade da nota
estiver na discussão dos resultados, a discussão não pode ocupar uma página. É
frequente a estrutura seguir o hábito em vez de seguir a grelha, e perder-se nota
por isso.

Entrega:

1. **A pergunta**, em uma frase, e o que o trabalho defende como resposta. Se o
   trabalho não defender nada, é uma compilação e a nota reflete isso.
2. **A estrutura**, secção a secção, com:
   - a função da secção dentro do argumento, não o título genérico
   - o número de palavras atribuído, somando ao total permitido
   - o critério de avaliação que essa secção serve
   - que material é preciso ter para a escrever
3. **O que já tenho e o que me falta.** Duas listas. A segunda é a que interessa.
4. **A ordem de escrita**, que raramente é a ordem de leitura. A introdução
   escreve-se quase sempre no fim, porque só aí se sabe o que se introduziu.
5. **O calendário** até {{prazo}}, com o que fica pronto em cada dia e uma folga
   antes da entrega para reler.

Se {{criterios}} não estiverem disponíveis, diz que a estrutura é uma aposta e
lista as perguntas a fazer a quem avalia.

Não inventes conteúdo para preencher a estrutura, nem referências. Onde faltar
material, a lista do que falta é a resposta certa.

## Porque importa

Trabalhos bem investigados perdem nota por estarem mal distribuídos: muito
espaço no que era fácil de escrever e pouco no que valia a nota. Distribuir as
palavras pelos critérios antes de escrever resolve isso, e mostra logo onde está
o buraco de material.

## Como saber se correu bem

- O peso dos critérios foi lido e refletido na distribuição de palavras
- Cada secção diz a sua função no argumento e o critério que serve
- As palavras atribuídas somam o limite permitido
- Existem as duas listas, o que há e o que falta
- Existe ordem de escrita e calendário com folga antes da entrega
