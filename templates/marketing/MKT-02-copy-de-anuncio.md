---
id: MKT-02
nome: Copy de anúncio com vários ângulos e variantes
categoria: marketing
nivel: essencial
modo: execucao
origem: novo
gatilhos:
  - preciso de um anúncio
  - escreve-me um anúncio para o Instagram
  - faz-me um texto para promover isto
  - preciso de texto para uma campanha paga
  - não sei o que hei de escrever no anúncio
  - quero testar várias versões do mesmo anúncio
nao_usar_quando:
  - o pedido é para uma página inteira e não para um anúncio, usar MKT-05
  - ainda não está decidido o que se vende nem a quem, usar MKT-01 primeiro
  - o texto pedido é editorial ou informativo e não tem intenção comercial
variaveis:
  - nome: produto
    descricao: o que se vende, com a promessa central em uma frase
    obrigatoria: true
    omissao: perguntar, sem isto nada do resto se sustenta
  - nome: publico
    descricao: quem vê o anúncio, com a dor ou desejo concreto que traz
    obrigatoria: false
    omissao: inferir do produto e declarar a assunção numa linha
  - nome: plataforma
    descricao: onde corre o anúncio, porque fixa formato e limites
    obrigatoria: false
    omissao: assumir Meta em formato feed e dizê-lo
  - nome: objetivo
    descricao: a ação que se quer, comprar, marcar, subscrever, instalar
    obrigatoria: false
    omissao: assumir clique para a página de destino
  - nome: provas
    descricao: números, resultados, testemunhos ou garantias disponíveis
    obrigatoria: false
    omissao: não inventar nenhuma e assinalar onde faria falta uma
  - nome: restricoes
    descricao: limites de caracteres, termos proibidos, obrigações legais
    obrigatoria: false
    omissao: aplicar os limites correntes da plataforma assumida
encadeia_com: [MKT-01, MKT-05, MKT-07]
---

## Prompt

Escreve copy de anúncio para {{produto}}, dirigido a {{publico}}, para correr em
{{plataforma}}, com o objetivo de {{objetivo}}.

Trabalha por ângulos, não por variações de palavras. Um ângulo é uma razão
diferente para a mesma pessoa comprar. Dá-me quatro:

1. Dor. O que custa hoje não resolver isto.
2. Desejo. Como fica a vida quando estiver resolvido.
3. Objeção. A razão pela qual esta pessoa ainda não comprou, respondida de frente.
4. Prova. O resultado concreto que já aconteceu a alguém.

Para cada ângulo entrega três peças separadas e etiquetadas: gancho, corpo e
chamada à ação. O gancho tem de funcionar sozinho, porque é o que aparece antes
do "ver mais". A chamada à ação diz o que acontece a seguir ao clique, não repete
o nome do produto.

Depois dos quatro ângulos, escolhe o que apostarias e explica em duas linhas
porquê, em função de {{publico}} e de {{objetivo}}.

Usa {{provas}} apenas onde houver material real. Onde uma afirmação precisar de
prova que não tenho, escreve-a entre parênteses retos como pendente, em vez de
inventar um número.

Respeita {{restricoes}}. Não uses emojis salvo pedido explícito, não uses
superlativos vazios, não abras com uma pergunta retórica, e não escrevas frases
do tipo "não é apenas X, é Y".

## Porque importa

Quase toda a gente escreve o mesmo anúncio cinco vezes e chama-lhe teste. Testar
sinónimos não ensina nada. Testar razões diferentes ensina qual é o motivo que
move aquela pessoa, e esse motivo serve depois para a página, para os emails e
para a proposta.

## Como saber se correu bem

- Vieram quatro ângulos genuinamente diferentes, não a mesma ideia repetida
- Cada gancho lê-se sozinho e faz sentido sem o resto do texto
- As afirmações sem prova estão marcadas como pendentes, sem números inventados
- Há uma recomendação com justificação ligada ao público e ao objetivo
- Os limites da plataforma foram respeitados
