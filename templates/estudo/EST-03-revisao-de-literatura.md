---
id: EST-03
nome: Revisão de literatura com fontes verificadas
categoria: estudo
nivel: situacional
modo: execucao
origem: novo
gatilhos:
  - preciso de fazer o estado da arte
  - o que é que já se escreveu sobre isto
  - preciso de fontes para este trabalho
  - faz-me uma revisão de literatura
  - preciso de referências académicas sobre este tema
nao_usar_quando:
  - o que se quer é resumir um documento que já se tem, usar EST-01
  - o trabalho já tem fontes e falta a estrutura, usar EST-04
  - não há acesso às fontes nem forma de as verificar
variaveis:
  - nome: tema
    descricao: a pergunta a que a revisão responde
    obrigatoria: true
    omissao: perguntar, e insistir até ser uma pergunta e não um assunto
  - nome: ambito
    descricao: limites de anos, idiomas, tipo de publicação
    obrigatoria: false
    omissao: propor limites e pedir confirmação antes de procurar
  - nome: norma_citacao
    descricao: o estilo de citação exigido
    obrigatoria: false
    omissao: perguntar, porque refazer citações no fim dá mais trabalho do que fazê-las bem
encadeia_com: [EST-01, EST-04, MKT-04]
---

## Prompt

Faz uma revisão de literatura sobre {{tema}}, dentro de {{ambito}}, com citações
em {{norma_citacao}}.

Antes de tudo, a regra que não se negoceia nesta tarefa: **não cites nada que não
tenhas aberto.** Não inventes títulos, autores, anos, revistas nem identificadores.
Uma referência inventada é o erro mais grave possível num trabalho académico,
porque quem avalia verifica, e uma referência que não existe põe em causa tudo o
resto.

Para cada fonte, indica o que leste de facto:

- **Texto completo.** Abriste e leste.
- **Só o resumo.** Leste o resumo e mais nada. Diz-o.
- **Referida por outros.** Sabes dela através de outra fonte. Diz qual, e trata
  a afirmação como sendo dessa outra fonte.

Estrutura a entrega:

1. **A pergunta** e os limites de procura usados, com os termos que procuraste.
2. **O que está estabelecido**, onde há acordo entre fontes, com pelo menos duas
   independentes por afirmação.
3. **O que está em disputa**, com as posições e quem as defende.
4. **As lacunas**, o que ninguém respondeu ainda. É esta secção que dá valor à
   revisão e que costuma justificar o trabalho seguinte.
5. **O que procuraste e não encontraste.** Obrigatória. Distingue não existe de
   não consegui aceder.
6. **A lista de referências**, no formato pedido.

Se não conseguires aceder a fontes suficientes para sustentar alguma secção,
escreve isso na secção em vez de a preencheres com generalidades. Uma revisão
curta e verdadeira vale mais do que uma longa e frágil.

## Porque importa

O ponto de falha destas tarefas não é a escrita, é a verificabilidade. Um texto
bem construído com três referências que não existem é inutilizável e prejudica
quem o entrega. Por isso a rastreabilidade vem antes da cobertura.

## Como saber se correu bem

- Nenhuma referência foi escrita sem ter sido aberta
- Cada fonte diz se foi lida por inteiro, pelo resumo, ou conhecida por terceiros
- As afirmações de consenso têm pelo menos duas fontes independentes
- Existem as secções de lacunas e do que não foi encontrado
- Onde faltou material, isso está escrito em vez de disfarçado
