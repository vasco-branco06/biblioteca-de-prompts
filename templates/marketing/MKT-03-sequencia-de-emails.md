---
id: MKT-03
nome: Sequência de emails com objetivo definido
categoria: marketing
nivel: recomendado
modo: execucao
origem: novo
gatilhos:
  - preciso de uma sequência de emails
  - as pessoas inscrevem-se e depois não acontece nada
  - quero fazer um seguimento automático
  - tenho uma lista e não faço nada com ela
  - quero uma série de emails para quem descarrega isto
nao_usar_quando:
  - o que se quer é um email único e avulso
  - ainda não existe campanha nem objetivo definido, usar MKT-01
  - não existe lista nem forma legal de contactar as pessoas
variaveis:
  - nome: objetivo
    descricao: o que a sequência tem de conseguir, em uma ação concreta
    obrigatoria: true
    omissao: perguntar
  - nome: momento_de_entrada
    descricao: o que faz uma pessoa entrar nesta sequência
    obrigatoria: false
    omissao: assumir inscrição voluntária e declarar a assunção
  - nome: numero_de_emails
    descricao: quantos emails
    obrigatoria: false
    omissao: propor o número que o objetivo pede e justificar
  - nome: ferramenta_envio
    descricao: por onde são enviados
    obrigatoria: false
    omissao: escrever de forma independente da ferramenta e assinalar o que cada uma terá de suportar
encadeia_com: [MKT-01, MKT-02, MKT-07]
---

## Prompt

Escreve uma sequência de {{numero_de_emails}} emails para conseguir
{{objetivo}}, que começa quando {{momento_de_entrada}}. Diz-me antes quantos vais
escrever e porquê.

Regras da sequência:

- Cada email faz um só trabalho. Se um email tenta educar e vender ao mesmo
  tempo, não faz nenhuma das duas.
- Cada email tem uma só ação. Dois botões diferentes é o mesmo que nenhum.
- O primeiro email entrega o que foi prometido no momento da inscrição, antes de
  pedir seja o que for. Se a pessoa se inscreveu para receber algo, é isso que
  vem primeiro.
- Cada email tem de fazer sentido isolado. Muita gente só abre o terceiro.

Para cada email escreve: o trabalho que faz, o assunto com duas alternativas, a
pré-visualização, o corpo, e a ação. No assunto, nada de truques que prometem o
que o corpo não cumpre.

Define também:

1. **Espaçamento** entre emails, com a razão. Mais depressa quando o interesse
   está quente, mais devagar depois.
2. **Saída.** O que faz uma pessoa deixar de receber o resto, tipicamente ter
   feito o que se queria. Continuar a insistir com quem já comprou é a forma mais
   rápida de perder alguém.
3. **O que fazer com quem chega ao fim sem agir.** Sai da sequência, entra
   noutra, ou fica em silêncio.

Deixa espaço no fim de cada email para o cancelamento da subscrição e para a
identificação de quem envia. É obrigação legal e não é opcional.

Considera {{ferramenta_envio}}. Se algum passo exigir uma funcionalidade que
nem todas as ferramentas têm, assinala isso.

## Porque importa

Uma lista sem sequência é uma lista a arrefecer. O momento em que alguém se
inscreve é o de maior interesse que vai haver, e quase toda a gente o desperdiça
com silêncio seguido de um pedido de compra semanas depois.

## Como saber se correu bem

- Cada email faz um só trabalho e pede uma só ação
- O primeiro entrega o que foi prometido antes de pedir alguma coisa
- Cada email lê-se sozinho
- Estão definidos o espaçamento, a saída e o destino de quem não age
- O cancelamento e a identificação de quem envia estão previstos
