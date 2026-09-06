---
id: MKT-06
nome: Calendário de conteúdo a partir de um tema central
categoria: marketing
nivel: recomendado
modo: execucao
origem: novo
gatilhos:
  - nunca sei sobre o que hei de publicar
  - preciso de um plano de conteúdos
  - quero publicar com regularidade
  - fico sem ideias ao fim de duas semanas
  - o que é que publico este mês
nao_usar_quando:
  - o que se quer é uma peça concreta e não um plano
  - ainda não há tema nem público definidos, usar MKT-01
  - já existe calendário e o que falta é escrever o conteúdo
variaveis:
  - nome: tema
    descricao: o assunto central sobre o qual se quer ser conhecido
    obrigatoria: true
    omissao: perguntar
  - nome: canais
    descricao: onde se publica
    obrigatoria: false
    omissao: perguntar, porque o formato muda tudo
  - nome: periodo
    descricao: quanto tempo o calendário cobre
    obrigatoria: false
    omissao: um mês, que é o horizonte que se consegue cumprir
  - nome: capacidade
    descricao: quanto tempo por semana existe mesmo para isto
    obrigatoria: false
    omissao: assumir poucas horas por semana e declarar a assunção
encadeia_com: [MKT-01, MKT-02, MKT-04]
---

## Prompt

Constrói um calendário de conteúdo sobre {{tema}} para {{canais}}, cobrindo
{{periodo}}, dimensionado para {{capacidade}}. Diz-me antes o ritmo que vais
propor e onde vais guardar o calendário.

Começa pelo ritmo, não pelas ideias. Ideias há sempre; o que falha é a cadência.
Propõe a frequência que {{capacidade}} aguenta numa semana má, e não numa semana
boa. Um calendário que só se cumpre quando corre tudo bem é abandonado ao
terceiro tropeção.

Depois estrutura assim:

1. **Três a cinco subtemas** dentro de {{tema}}. São as coisas sobre as quais se
   vai falar sempre. Se forem mais do que cinco, o tema é largo demais para ser
   reconhecível.
2. **Uma peça central por semana ou quinzena**, conforme o ritmo. É a que dá
   trabalho a sério.
3. **Peças derivadas** de cada central, uma por canal, adaptadas ao formato e
   não copiadas. A mesma ideia rende várias peças; ideias novas todos os dias
   não rendem nada.
4. **O calendário**, com data, canal, formato, subtema, e o gancho em uma linha.

Para cada peça diz também a que pergunta do público responde. Uma peça que não
responde a nenhuma pergunta é enchimento e sai.

Reserva pelo menos um espaço por período sem tema atribuído, para o que
aparecer: uma pergunta que alguém fez, uma novidade, uma reação. Um calendário
totalmente preenchido não sobrevive ao contacto com a realidade.

No fim, diz-me quanto tempo isto consome por semana, somado. Se ultrapassar
{{capacidade}}, corta e mostra a versão cortada.

## Porque importa

Publicar de vez em quando não constrói reconhecimento; publicar sempre sobre a
mesma coisa constrói. A dificuldade nunca é ter ideias, é ter um ritmo que se
aguente durante meses, e por isso o calendário desenha-se a partir do tempo
disponível e não a partir da ambição.

## Como saber se correu bem

- O ritmo foi definido a partir da capacidade real, e para uma semana má
- Os subtemas são cinco ou menos
- Cada peça derivada nasce de uma peça central e está adaptada ao canal
- Cada peça responde a uma pergunta concreta do público
- Há espaço deixado por preencher, e o tempo total foi somado e comparado com a capacidade
