---
id: DOC-02
nome: A memória do projeto para as próximas sessões
categoria: documentacao
nivel: recomendado
modo: execucao
origem: ccp-45
gatilhos:
  - estou farto de repetir as mesmas coisas
  - de cada vez que abro isto começamos do zero
  - já respondi a essa pergunta três vezes
  - quero que te lembres das decisões do projeto
  - cria o ficheiro de regras do projeto
nao_usar_quando:
  - o que se quer explicar é a estrutura do código, usar DOC-04
  - o documento é para pessoas e não para a IA, usar DOC-05
  - é uma regra isolada a acrescentar a um ficheiro que já existe, usar CTL-07
variaveis:
  - nome: ficheiro_memoria
    descricao: o ficheiro que a ferramenta lê no início de cada sessão
    obrigatoria: false
    omissao: CLAUDE.md na raiz do projeto
encadeia_com: [DOC-04, CTL-07, PER-10]
---

## Prompt

Analisa este projeto e escreve {{ficheiro_memoria}} para servires-te dele como
memória nas próximas sessões, quando não te lembrares de nada do que decidimos.

Diz-me primeiro o que vais escrever, em tópicos, e espera. Um ficheiro destes mal
feito estraga tudo o que vier a seguir.

Inclui, curto e direto:

1. O que é o projeto, em uma frase.
2. As ferramentas usadas e a razão de cada uma.
3. Os comandos para correr, testar e publicar, exatamente como se escrevem.
4. As convenções a respeitar sempre: nomes, organização de pastas, onde vão as
   validações, como se tratam os erros.
5. O que nunca se deve fazer neste projeto.
6. As decisões já tomadas que não se rediscutem.

Escreve em pontos curtos. Nada de parágrafos, nada de explicações longas: isto é
para ser lido de relance no início de cada sessão.

No topo, põe um aviso a lembrar que este ficheiro deve ser lido antes de se mexer
no código.

Regras do que não entra: nada que se possa descobrir olhando para o código em
dois minutos, nada que mude todas as semanas, e nada que seja preferência sem
consequência. Este ficheiro só serve enquanto for curto.

Não inventes convenções que o projeto não segue. Escreve o que lá está, mesmo que
aches que devia ser outra coisa. Se achares, diz numa nota à parte.

## Porque importa

Cada sessão começa sem memória do que ficou decidido, e por isso repetem-se as
mesmas perguntas e reinventam-se as mesmas soluções de maneiras diferentes. Este
ficheiro é o que transforma decisões tomadas uma vez em decisões respeitadas
sempre.

## Como saber se correu bem

- O conteúdo foi apresentado em tópicos e aprovado antes de ser escrito
- Está em pontos curtos e cabe numa leitura rápida
- As convenções escritas são as que o projeto segue de facto
- Existe a lista do que nunca fazer
- As sugestões de melhoria ficaram numa nota à parte
