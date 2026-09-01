---
id: PLA-02
nome: Entrevista antes de escrever seja o que for
categoria: planeamento
nivel: recomendado
modo: execucao
origem: ccp-18
gatilhos:
  - quero começar um projeto novo
  - tenho uma ideia para uma app
  - quero fazer um site para
  - por onde é que começo
  - ajuda-me a montar isto do zero
nao_usar_quando:
  - já existe um plano ou uma especificação escrita, e o que falta é fatiar ou cortar, usar PLA-04 ou PLA-07
  - o pedido é uma alteração a um projeto que já existe
  - já está decidido o que se vai construir e só faltam as ferramentas, usar PLA-05
  - a pessoa quer uma resposta rápida a uma dúvida e não montar um projeto
variaveis:
  - nome: ideia
    descricao: o que a pessoa quer construir, mesmo que ainda esteja vago
    obrigatoria: true
    omissao: começar a entrevista pela pergunta que a descobre, sem inventar uma
  - nome: ficheiro_plano
    descricao: onde fica o plano no fim
    obrigatoria: false
    omissao: PLAN.md na raiz do projeto
  - nome: limites
    descricao: prazo, orçamento, plataforma obrigatória ou outra restrição já conhecida
    obrigatoria: false
    omissao: perguntar durante a entrevista, nunca assumir em silêncio
encadeia_com: [PLA-03, PLA-04, PLA-06, PLA-07]
---

## Prompt

Vais ajudar-me a especificar {{ideia}}. Ainda não escrevas código nem documento
nenhum. Primeiro entrevista-me.

Regras da entrevista:

- Uma pergunta de cada vez. Espera pela minha resposta antes da seguinte.
- Começa pelas perguntas que mais mudam o desenho do produto e só depois desce
  aos detalhes. Quem usa isto e para resolver o quê vem antes de que cor tem o
  botão.
- Se eu responder de forma vaga, insiste. Uma resposta vaga agora vira retrabalho
  daqui a duas semanas.
- Não assumas nada importante em silêncio. Quando precisares de assumir alguma
  coisa, diz em voz alta o que estás a assumir e pergunta se está certo.
- Cobre {{limites}} antes de fechar: prazo, dinheiro, plataforma, quem mais mexe
  nisto, o que já existe e não pode partir.

Quando achares que já tens o essencial, avisa-me que estás pronto e espera. Só
depois de eu confirmar é que escreves {{ficheiro_plano}} com:

1. O objetivo em uma frase.
2. O âmbito, em duas listas separadas: o que entra na primeira versão e o que
   fica de fora. A segunda lista é tão importante como a primeira.
3. Quem usa e o que cada um faz.
4. Os dados que a aplicação vai guardar.
5. As fases de construção, pequenas, ordenadas, cada uma com o que fica a
   funcionar no fim dela.
6. O que ficou por decidir, com a decisão que falta em cada ponto.

Não encham o plano de secções que não usámos na conversa. O que não foi
perguntado não entra.

Começa agora com a primeira pergunta.

## Porque importa

Quando o trabalho arranca sem esta conversa, constrói-se depressa a coisa errada,
e o erro só aparece quando já custa desfazer. Meia hora de perguntas antes de
escrever a primeira linha é o momento mais barato de todo o projeto para mudar de
ideias.

## Como saber se correu bem

- As perguntas vieram uma de cada vez, e não uma lista de quinze de uma vez só
- As primeiras perguntas foram sobre o produto, não sobre tecnologia
- Cada assunção foi dita em voz alta e confirmada
- O plano só apareceu depois de a entrevista ter sido dada por terminada
- A lista do que fica de fora existe e não está vazia
- O que ficou por decidir está registado em vez de resolvido por conta própria
