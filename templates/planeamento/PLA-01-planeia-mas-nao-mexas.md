---
id: PLA-01
nome: Planeia primeiro, mexe depois
categoria: planeamento
nivel: essencial
modo: diagnostico
origem: ccp-2
gatilhos:
  - antes de mexeres diz-me o que vais fazer
  - quero ver o plano primeiro
  - não mexas ainda
  - isto parece grande, como é que vais fazer
  - explica-me o que vais alterar antes de alterares
nao_usar_quando:
  - a alteração é de uma linha e planear demora mais do que fazer
  - o projeto ainda não existe e falta decidir o que construir, usar PLA-02
  - já existe um plano aprovado e o que se pede é executá-lo
variaveis:
  - nome: tarefa
    descricao: o trabalho a planear
    obrigatoria: false
    omissao: usar o último pedido da conversa e dizer numa linha qual foi
  - nome: restricoes
    descricao: o que não pode ser tocado, prazos, dependências de terceiros
    obrigatoria: false
    omissao: perguntar apenas se alguma parte do plano depender disso
encadeia_com: [PLA-09, CTL-05, PLA-07]
---

## Prompt

Antes de mexeres em código, faz-me o plano de {{tarefa}}. Não escrevas código,
não corras comandos, não crias nem alteres ficheiros até eu aprovar o plano.

O plano leva:

1. Os passos, pela ordem em que os vais fazer, e o que fica pronto no fim de cada
   um.
2. Os ficheiros que vais tocar, com o nome de cada um e o que muda lá dentro.
   Não escrevas "os ficheiros relevantes"; escreve os nomes.
3. O que pode correr mal em cada passo e o que fica partido se correr.
4. O que fica deliberadamente de fora deste trabalho.
5. Como eu confirmo no fim que ficou bem, em passos que eu consiga fazer sozinho
   sem ler código.

Respeita {{restricoes}}.

Se durante o plano descobrires que o pedido é ambíguo, escreve a ambiguidade na
lista em vez de a resolveres por tua conta.

Para no fim do plano e espera pela minha resposta.

## Porque importa

Corrigir um plano custa uma frase. Corrigir código já escrito custa desfazer
alterações espalhadas por ficheiros que já nem sabes quais são. Este pedido põe a
decisão no momento em que ainda é barata.

## Como saber se correu bem

- Nenhum ficheiro foi criado ou alterado
- Os ficheiros a tocar aparecem pelo nome, não por categoria
- Há riscos identificados e não só uma lista de passos otimista
- O que fica de fora está escrito
- Parou no fim e esperou, em vez de começar a trabalhar a seguir ao plano
