---
id: CTL-07
nome: Gravar a correção como regra do projeto
categoria: controlo
nivel: recomendado
modo: execucao
origem: ccp-17
gatilhos:
  - já te disse isto três vezes
  - isto é uma regra permanente
  - grava isso para não voltares a fazer
  - de agora em diante é sempre assim
  - não quero repetir isto em cada conversa
nao_usar_quando:
  - a correção é específica desta tarefa e não se repete
  - o ficheiro de regras ainda não existe e há muito para escrever, usar DOC-02
  - é uma decisão técnica com contexto a preservar, usar DOC-06
variaveis:
  - nome: regra
    descricao: o comportamento que passa a ser permanente
    obrigatoria: false
    omissao: usar a correção que acabou de ser feita, e confirmá-la comigo antes de escrever
  - nome: ficheiro_regras
    descricao: onde vivem as regras do projeto
    obrigatoria: false
    omissao: CLAUDE.md na raiz do projeto, criando-o se não existir
encadeia_com: [DOC-02, DOC-06]
---

## Prompt

{{regra}} passa a ser permanente. Acrescenta-a a {{ficheiro_regras}}.

Antes de escreveres, mostra-me a frase exata que vais acrescentar e espera.

Regras de como a escrever:

- Por tuas palavras, curta, no imperativo. Uma ou duas linhas.
- Diz o comportamento a seguir, e não a história de como chegámos aqui.
- Se a regra tiver exceções, escreve-as. Uma regra absoluta que tem exceções é
  ignorada logo à primeira vez que a exceção aparece.
- Põe-na na secção certa do ficheiro. Se não houver secção adequada, cria uma com
  um nome claro.

Antes de acrescentar, verifica se já existe uma regra parecida. Se existir,
melhora-a em vez de escreveres uma segunda quase igual. Duas regras próximas mas
diferentes é pior do que nenhuma, porque nunca se sabe qual manda.

Se o ficheiro já estiver longo, diz-me o que se pode remover por já não se
aplicar. Um ficheiro de regras que ninguém consegue ler de uma vez deixa de ser
seguido.

## Porque importa

Cada conversa nova começa sem memória das correções anteriores, e sem isto
repete-se a mesma indicação semana após semana. Escrever uma vez no ficheiro que
é lido no arranque converte uma correção repetida num comportamento por defeito.

## Como saber se correu bem

- A frase foi mostrada e aprovada antes de ser escrita
- Está no imperativo, curta, sem a história por trás
- As exceções, se existirem, ficaram escritas
- Foi verificado se já existia regra parecida
- Se o ficheiro estava longo, foi proposto o que remover
