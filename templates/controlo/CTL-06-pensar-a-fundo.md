---
id: CTL-06
nome: Pensar a fundo antes de decidir
categoria: controlo
nivel: recomendado
modo: diagnostico
origem: ccp-16
gatilhos:
  - isto é uma decisão importante
  - pensa bem antes de responder
  - não tenhas pressa nesta
  - isto vai ser difícil de mudar depois
  - preciso que penses a sério nisto
nao_usar_quando:
  - a decisão é pequena e reversível
  - o pedido é mecânico e não tem decisão nenhuma
  - já se está atrasado e a resposta óbvia serve
variaveis:
  - nome: decisao
    descricao: o que tem de ser decidido
    obrigatoria: false
    omissao: usar o assunto em discussão
encadeia_com: [CTL-05, PLA-09, PLA-10]
---

## Prompt

{{decisao}} é uma decisão importante e difícil de reverter. Usa ultrathink e
raciocina a fundo antes de responderes. Não tenhas pressa de chegar ao código.

Antes de recomendares:

1. Considera pelo menos duas alternativas a sério, e não uma alternativa de
   fachada ao lado da que já preferes.
2. Para cada uma, pensa no que corre mal daqui a seis meses, e não apenas em
   como resolve o problema de hoje.
3. Identifica o que estás a assumir sem saber. Se alguma dessas assunções estiver
   errada, qual das alternativas passa a ser a melhor.
4. Pergunta-te o que é preciso ser verdade para a tua recomendação estar errada.

Depois recomenda, com a razão, e diz-me qual é a peça de informação que mais
mudaria a tua recomendação se eu ta desse. Se essa peça for barata de obter,
diz-me como a obtenho antes de decidirmos.

Não me dês uma resposta longa a dizer o mesmo de várias maneiras. Pensar a fundo
não é escrever mais.

## Porque importa

Para decisões difíceis de mudar, o esforço extra de raciocínio compensa,
sobretudo por trazer à superfície aquilo que se estava a assumir sem reparar. Não
vale a pena em decisões pequenas, e usar isto em tudo só torna cada resposta mais
lenta.

## Como saber se correu bem

- Foram consideradas alternativas a sério e não uma de fachada
- Está dito o que pode correr mal a médio prazo em cada opção
- As assunções não verificadas estão explícitas
- Há uma recomendação clara e a informação que mais a mudaria
- A resposta é densa e não apenas comprida
