---
id: EST-01
nome: Resumo estruturado de um documento longo
categoria: estudo
nivel: essencial
modo: execucao
origem: novo
gatilhos:
  - tenho um pdf de oitenta páginas para estudar
  - preciso de perceber isto até quinta
  - resume-me este documento
  - tenho um documento enorme para ler
  - não tenho tempo para ler isto tudo
  - o que é que interessa mesmo neste relatório
nao_usar_quando:
  - o objetivo é decorar para um teste, usar EST-02
  - o documento é curto e lê-se em dez minutos
  - o que se quer é comparar várias fontes, usar EST-03
  - o pedido é perceber um conceito e não um documento, usar EST-05
variaveis:
  - nome: documento
    descricao: caminho, ficheiro ou conjunto de páginas a resumir
    obrigatoria: true
    omissao: perguntar qual é
  - nome: objetivo
    descricao: para que serve a leitura, exame, decisão, reunião, escrita
    obrigatoria: false
    omissao: assumir compreensão para exame e declarar a assunção
  - nome: profundidade
    descricao: quanto detalhe se quer, panorama, trabalho ou exaustivo
    obrigatoria: false
    omissao: nível de trabalho, suficiente para discutir o assunto sem reler
  - nome: formato_saida
    descricao: onde fica o resumo, resposta no chat ou ficheiro markdown
    obrigatoria: false
    omissao: ficheiro markdown ao lado do documento, com o mesmo nome
encadeia_com: [EST-02, EST-05]
---

## Prompt

Vais resumir {{documento}} para {{objetivo}}, ao nível {{profundidade}}, e entregar
em {{formato_saida}}. Antes de escrever, diz-me em uma linha o que vais produzir e
onde o guardas.

Lê o documento inteiro antes de resumir a primeira secção. Um resumo escrito à
medida que se lê fica com o peso todo no início.

Estrutura a entrega assim:

1. A tese. O que este documento defende, em três frases. Se defender mais do que
   uma coisa, diz quantas e quais.
2. O mapa. A estrutura real do documento, secção a secção, com uma linha por
   secção a dizer qual é a função dela no argumento, e não o título que já lá está.
3. O que interessa para {{objetivo}}. Aqui vai o detalhe. Definições que é preciso
   saber, números que sustentam o argumento, exemplos que o autor usa para provar
   cada ponto. Indica sempre a página ou secção de onde vem cada coisa.
4. O que se pode saltar e porquê. Partes que repetem, contextualizam ou existem
   por convenção do formato.
5. O que ficou por responder. Perguntas que o documento levanta e não fecha,
   afirmações sem prova apresentada, saltos no raciocínio, termos usados sem
   definição. Esta secção é obrigatória e nunca vem vazia. Se estiver vazia, é
   porque a leitura foi superficial.
6. Cinco perguntas de verificação. Perguntas cuja resposta certa prova que se
   percebeu o documento, com a resposta a seguir a cada uma.

Não escrevas nada que não esteja no documento. Onde acrescentares contexto teu,
marca-o como acrescento e separa-o do resumo.

## Porque importa

O resumo típico devolve o índice por outras palavras e deixa a pessoa com a
sensação de que percebeu. A parte que faz diferença é a que fica de fora: onde é
que o argumento não fecha e o que é preciso perguntar a seguir. É isso que
distingue estudar de folhear.

## Como saber se correu bem

- A tese está em três frases e não é um parágrafo de generalidades
- Cada facto do resumo aponta para a página ou secção de onde saiu
- A secção do que ficou por responder tem conteúdo real
- Os acrescentos externos estão marcados como tal
- As cinco perguntas não se respondem só com o resumo lido por cima
