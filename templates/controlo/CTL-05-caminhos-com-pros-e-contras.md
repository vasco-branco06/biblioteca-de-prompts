---
id: CTL-05
nome: Dois ou três caminhos, com vantagens e desvantagens
categoria: controlo
nivel: recomendado
modo: diagnostico
origem: ccp-15
gatilhos:
  - há outra maneira de fazer isto
  - não escolhas logo o primeiro caminho
  - quais são as opções
  - quero decidir eu como é que isto se faz
  - dá-me alternativas antes de avançares
nao_usar_quando:
  - existe uma forma óbvia e as alternativas seriam inventadas para encher
  - a decisão é fácil de mudar depois e a discussão custa mais do que a mudança
  - o que se quer é a lista de decisões de uma funcionalidade inteira, usar PLA-09
variaveis:
  - nome: problema
    descricao: o que precisa de ser decidido
    obrigatoria: false
    omissao: usar o assunto em discussão e dizer qual é
  - nome: criterio
    descricao: o que pesa mais na escolha
    obrigatoria: false
    omissao: assumir simplicidade e rapidez de execução, e declarar a assunção
encadeia_com: [PLA-09, CTL-06, DOC-06]
---

## Prompt

Não escolhas logo o primeiro caminho para {{problema}}. Apresenta-me duas ou três
abordagens diferentes e espera que eu escolha.

Diferentes quer dizer com filosofias distintas, e não a mesma solução com nomes
trocados. Se só houver mesmo um caminho razoável, diz isso em vez de inventares
alternativas para encher a resposta.

Para cada uma:

- como funciona, em duas ou três linhas de linguagem simples
- o que ganho
- o que perco
- quanto trabalho dá, em ordem de grandeza
- o que fica difícil se mais tarde quiser mudar de ideias

Depois diz qual recomendas e porquê, tendo em conta {{criterio}}. Uma
recomendação clara, e não um encolher de ombros: escolher é o teu trabalho aqui,
decidir é o meu.

Se uma das opções for claramente pior mas for a que muita gente escolhe, inclui-a
na mesma e explica porquê. É útil saber o que se está a rejeitar.

Não implementes nada até eu escolher.

## Porque importa

A primeira solução que ocorre nem sempre é a melhor, e quando é apresentada
sozinha parece a única possível. Ver o mapa das opções permite decidir com
conhecimento, sobretudo em escolhas que ficam caras de mudar depois.

## Como saber se correu bem

- As opções são genuinamente diferentes entre si
- Cada uma tem vantagens, desvantagens e esforço
- Está dito o que fica difícil de mudar em cada caso
- Existe uma recomendação clara e justificada
- Nada foi implementado antes da escolha
