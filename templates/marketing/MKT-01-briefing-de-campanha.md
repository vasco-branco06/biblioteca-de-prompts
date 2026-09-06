---
id: MKT-01
nome: Briefing de campanha a partir de um objetivo de negócio
categoria: marketing
nivel: essencial
modo: execucao
origem: novo
gatilhos:
  - quero fazer uma campanha
  - preciso de divulgar isto
  - quero mais vendas no próximo mês
  - vamos lançar isto e não sei por onde começar
  - preciso de trazer gente para aqui
nao_usar_quando:
  - já existe briefing e o que falta é escrever as peças, usar MKT-02 ou MKT-03
  - o pedido é uma peça isolada e não uma campanha
  - ainda não está decidido o que se vende nem a quem
variaveis:
  - nome: objetivo_negocio
    descricao: o que tem de acontecer no negócio, não na campanha
    obrigatoria: true
    omissao: perguntar, e insistir até ser mensurável
  - nome: publico
    descricao: quem tem de agir para o objetivo acontecer
    obrigatoria: false
    omissao: inferir do produto e declarar a assunção numa linha
  - nome: recursos
    descricao: orçamento, tempo e quem trabalha nisto
    obrigatoria: false
    omissao: assumir orçamento pequeno e uma só pessoa, e dizê-lo
  - nome: prazo
    descricao: quando tem de estar feito
    obrigatoria: false
    omissao: perguntar, porque muda tudo o que é possível
encadeia_com: [MKT-02, MKT-03, MKT-06, MKT-05]
---

## Prompt

Vamos transformar {{objetivo_negocio}} num briefing de campanha. Diz-me primeiro
o que vais escrever e onde, e espera.

Antes de tudo, converte o objetivo em número. Mais vendas não é objetivo, é
desejo. Quantas vendas, até quando, a partir de que ponto de partida. Se eu não
souber o ponto de partida, diz que isso é o primeiro problema a resolver.

O briefing leva:

1. **Objetivo**, com número e data.
2. **Uma pessoa**, não um segmento. Parte de {{publico}} e afina: quem é, o que
   anda a tentar resolver, o que já experimentou, o que a faz hesitar. Se a
   campanha servir três públicos diferentes, são três campanhas, e diz isso.
3. **A mensagem única.** Uma frase que essa pessoa tem de acreditar para agir.
   Só uma. Se houver duas, escolhe e explica porquê.
4. **A ação.** O que ela faz a seguir, e onde. Uma ação, não um menu.
5. **Onde a encontramos**, com {{recursos}} em mente. Poucos canais bem feitos
   ganham a muitos mal feitos, e com uma pessoa a trabalhar nisto não há muitos.
6. **Como sabemos que resultou.** O que se mede, onde se lê esse número, e a
   partir de que valor se considera que valeu a pena.
7. **O que não fazemos nesta campanha.** Esta secção é obrigatória e é a que
   protege o resto.

Se {{prazo}} não der para o que o objetivo pede, diz isso em vez de encolheres o
plano em silêncio. Prefiro saber que é irrealista agora.

Não escrevas peças de comunicação aqui. Isto é o mapa, não o conteúdo.

## Porque importa

Quase todas as campanhas que não resultam falham antes de existir, num objetivo
vago e num público que é toda a gente. Com o objetivo em número e uma pessoa
concreta, cada decisão seguinte, o canal, o texto, a oferta, decide-se sozinha.

## Como saber se correu bem

- O objetivo tem número, data e ponto de partida
- Há uma pessoa descrita, não um segmento demográfico
- A mensagem única é mesmo uma
- Existe a lista do que fica de fora
- Se o prazo for irrealista, isso foi dito
