---
id: PLA-08
nome: Quanto vai custar e até onde é grátis
categoria: planeamento
nivel: recomendado
modo: diagnostico
origem: ccp-24
gatilhos:
  - quanto é que isto me vai custar
  - isto é grátis
  - não quero surpresas na fatura
  - a partir de quantos utilizadores começo a pagar
  - quero saber os custos antes de avançar
nao_usar_quando:
  - o pedido é sobre o custo de usar a IA nesta conversa e não sobre os serviços do projeto, usar CTL-09
  - ainda não há ideia nenhuma do que se vai construir
  - as ferramentas ainda não estão escolhidas, usar PLA-05 primeiro
variaveis:
  - nome: projeto
    descricao: o que se vai construir e com que ferramentas
    obrigatoria: false
    omissao: usar as ferramentas já presentes no projeto ou já decididas na conversa
  - nome: escala_esperada
    descricao: utilizadores, pedidos ou volume de dados previstos no primeiro ano
    obrigatoria: false
    omissao: assumir escala pequena de arranque e declarar os números assumidos
encadeia_com: [PLA-05, PLA-10, SEG-14]
---

## Prompt

Para {{projeto}}, com {{escala_esperada}}, faz-me o mapa dos custos. Só
diagnóstico.

Devolve uma tabela com uma linha por serviço:

serviço | para que serve | tem plano grátis | o que esse plano inclui | o que
dispara a passagem a pago | quanto custa o primeiro escalão pago

Depois responde a estas três, que são as que costumam apanhar as pessoas
desprevenidas:

1. Qual é o serviço que primeiro passa a pago, e com que acontecimento concreto.
2. Que custos crescem com a utilização e não têm teto, ou seja, aqueles em que
   uma noite má gera uma fatura má.
3. O que acontece quando um plano grátis é ultrapassado: cobra, bloqueia, ou
   desliga o serviço. As três consequências são muito diferentes.

Diz também o que posso adiar. Serviços que só passam a fazer falta quando houver
utilizadores a sério não precisam de ser contratados no primeiro dia.

Regra importante: preços mudam. Não escrevas nenhum valor que não tenhas a
certeza de estar atual. Onde não souberes, escreve que é preciso confirmar na
página do serviço, e diz que página. Um número inventado aqui é pior do que uma
lacuna assumida.

## Porque importa

Quase todos os serviços usados neste tipo de projeto são grátis até um limite que
ninguém lê, e depois começam a cobrar sem aviso. Saber onde está esse limite
antes de construir evita escolher a ferramenta que fica cara exatamente quando o
projeto começar a correr bem.

## Como saber se correu bem

- Há uma linha por serviço, incluindo os que já estão no projeto
- Cada limite grátis está dito em unidades concretas
- Está claro o que acontece ao ultrapassar cada limite
- Os custos sem teto estão assinalados à parte
- Onde não houve certeza do preço, está escrito que é preciso confirmar
