---
id: PLA-09
nome: As decisões que faltam, com recomendação para cada uma
categoria: planeamento
nivel: situacional
modo: diagnostico
origem: ccp-51
gatilhos:
  - o que é que temos de decidir antes de começar
  - não quero que decidas sozinho
  - que escolhas é que isto implica
  - antes de construires esta funcionalidade
  - quais são as decisões importantes aqui
nao_usar_quando:
  - as decisões já estão tomadas e registadas
  - a escolha é só de ferramentas, usar PLA-05
  - o trabalho é mecânico e não tem decisões de desenho
variaveis:
  - nome: funcionalidade
    descricao: o que vai ser construído
    obrigatoria: true
    omissao: perguntar
  - nome: criterio
    descricao: o que importa mais nesta decisão, rapidez, custo, simplicidade ou durar muito tempo
    obrigatoria: false
    omissao: assumir simplicidade acima de tudo e declará-lo
encadeia_com: [PLA-01, CTL-05, DOC-06]
---

## Prompt

Antes de construir {{funcionalidade}}, lista as decisões que vão ter de ser
tomadas. Não construas nada.

Uma decisão entra na lista se mudar o que fica escrito no código de forma difícil
de desfazer depois. Escolhas que se mudam numa linha não são decisões, são
detalhes, e não me devem ocupar tempo.

Para cada uma escreve:

- A pergunta, em linguagem simples, sem termos técnicos por explicar.
- As opções reais, no máximo três.
- A tua recomendação e a razão dela, tendo em conta {{criterio}}.
- O que fica difícil se mais tarde eu quiser mudar de ideias.

Ordena por quanto custa mudar depois de decidido. As irreversíveis primeiro.

No fim, separa as decisões que precisam mesmo de mim das que podes tomar sozinho
seguindo a tua recomendação. Se a lista tiver mais de seis pontos, provavelmente
estás a trazer-me detalhes. Corta-a.

Espera pela minha resposta antes de avançares.

## Porque importa

Quando ninguém as põe em cima da mesa, estas escolhas são feitas na mesma, só que
em silêncio e sem ninguém dar por elas. Vê-las escritas com uma recomendação
deixa decidir sem perceber dos detalhes, e deixa a decisão registada.

## Como saber se correu bem

- Nada foi construído
- Cada pergunta está em linguagem que se percebe sem saber programar
- Cada uma vem com recomendação e não só com opções
- A ordem segue o custo de mudar mais tarde
- Está separado o que precisa mesmo de mim do que não precisa
