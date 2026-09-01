---
id: PLA-06
nome: Especificação com critérios que eu consigo testar
categoria: planeamento
nivel: recomendado
modo: execucao
origem: ccp-22
gatilhos:
  - quero garantir que fica bem feito
  - como é que eu confirmo que ficou como pedi
  - escreve o que isto tem de fazer antes de programares
  - preciso de uma lista do que tem de funcionar
  - quero uma especificação
nao_usar_quando:
  - o trabalho é uma correção pequena e a especificação demora mais do que a correção
  - ainda não se sabe o que se quer construir, usar PLA-02
  - o que falta é ordenar fases e não descrever comportamento, usar PLA-04
variaveis:
  - nome: ambito
    descricao: o projeto ou as funcionalidades a especificar
    obrigatoria: true
    omissao: perguntar
  - nome: ficheiro_spec
    descricao: onde fica a especificação
    obrigatoria: false
    omissao: SPEC.md na raiz do projeto
encadeia_com: [PLA-02, PLA-07, TES-02, TES-04]
---

## Prompt

Antes de programares, escreve a especificação de {{ambito}} em {{ficheiro_spec}}.
Diz-me antes o que vais criar e onde.

Para cada funcionalidade descreve o comportamento que se vê, e não a forma como
está feita por dentro:

- O que entra.
- O que sai.
- O que acontece quando corre bem.
- O que acontece quando corre mal: erro do servidor, campo vazio, valor
  inválido, sem internet, sessão expirada, carregar duas vezes no botão.

No fim de cada funcionalidade escreve os critérios de aceitação, em lista de
verificação. Cada critério é uma frase que eu consiga testar clicando, na forma
quando faço isto, vejo aquilo. Se um critério não se puder verificar sem ler
código, está mal escrito, reescreve-o.

Não escrevas código nenhum enquanto eu não aprovar isto.

Se alguma parte for ambígua, escreve-a numa secção de ambiguidades no fim, com a
decisão que falta tomar. Não resolvas nenhuma por tua conta, mesmo que a resposta
te pareça óbvia.

Escreve em linguagem simples. Quem lê isto sou eu, não um programador.

## Porque importa

Sem critérios escritos, aprovar trabalho é uma questão de confiança e de olhar
para o ecrã à espera de reparar em alguma coisa. Com uma lista de frases
testáveis, qualquer pessoa confirma se ficou feito, sem perceber de código.

## Como saber se correu bem

- Cada funcionalidade descreve comportamento visível e não implementação
- Os casos de erro estão escritos, e não só o caminho em que corre tudo bem
- Todos os critérios se verificam clicando, sem abrir código
- As ambiguidades foram listadas em vez de resolvidas
- Nenhum código foi escrito
