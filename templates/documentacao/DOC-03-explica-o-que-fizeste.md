---
id: DOC-03
nome: Explica o que fizeste e porquê, para eu aprender
categoria: documentacao
nivel: recomendado
modo: diagnostico
origem: ccp-46
gatilhos:
  - quero perceber o que mudou no projeto
  - explica-me para eu aprender
  - o que é que isto muda daqui para a frente
  - resume o que fizeste nesta tarefa
  - quero aprender e não só receber código
nao_usar_quando:
  - o pedido é esclarecer uma frase que acabou de ser dita, usar DOC-01
  - a tarefa ainda não terminou
  - o que se quer é registar uma decisão em documento, usar DOC-06
variaveis:
  - nome: tarefa
    descricao: o trabalho que acabou de ser feito
    obrigatoria: false
    omissao: usar a última tarefa concluída e dizer qual foi
encadeia_com: [DOC-01, DOC-06, CTL-07]
---

## Prompt

Acabaste {{tarefa}}. Explica-me, em linguagem simples e sem alterares mais nada:

1. **O que mudou.** Que ficheiros e o que passou a acontecer de diferente do
   ponto de vista de quem usa a aplicação. Não me dês a lista das linhas.
2. **Porque assim.** A razão da abordagem escolhida, e que alternativa
   consideraste e puseste de lado, com o motivo real.
3. **O que isto implica daqui para a frente.** O que fica mais fácil, o que fica
   mais difícil, e o que passa a ser preciso lembrar quando se mexer nesta parte.
4. **O que aprender com isto.** Uma ideia geral que se aplique a outros casos
   parecidos, e não apenas a este.
5. **O que ficou por fazer.** Atalhos que tomaste, casos que não estão cobertos,
   coisas que deixaste para depois. Esta parte é obrigatória e não pode vir
   vazia. Se estiver vazia, é porque não estás a olhar com atenção.

Se alguma coisa que fizeste for uma solução provisória, diz isso com todas as
letras e diz o que a torna definitiva.

Não me vendas o trabalho. Quero saber o que ficou bem e o que ficou apenas a
funcionar.

## Porque importa

Sem esta explicação fica-se com uma caixa preta que funciona por razões que
ninguém sabe, e ao fim de umas semanas já não se consegue decidir nada sobre o
projeto sem perguntar tudo outra vez. É também a forma mais rápida de aprender,
porque se aprende sobre código que interessa.

## Como saber se correu bem

- A explicação fala do que muda para quem usa, não de linhas alteradas
- A alternativa posta de lado está dita com o motivo
- Existe uma ideia geral aplicável a outros casos
- A lista do que ficou por fazer tem conteúdo real
- As soluções provisórias estão identificadas como tal
