---
id: PLA-10
nome: Estimativa honesta de tempo, risco e a experiência que tira a dúvida
categoria: planeamento
nivel: situacional
modo: diagnostico
origem: ccp-52
gatilhos:
  - quanto tempo é que isto demora
  - vale a pena avançar com isto
  - onde é que me vou atrapalhar
  - isto é muito ambicioso
  - por onde é mais seguro começar
nao_usar_quando:
  - não existe plano para estimar, usar PLA-02 primeiro
  - o trabalho é pequeno e a estimativa demora mais do que fazê-lo
  - o que se procura são custos em dinheiro e não em tempo, usar PLA-08
variaveis:
  - nome: plano
    descricao: o plano ou a lista de fases a estimar
    obrigatoria: false
    omissao: usar o plano do projeto e dizer qual
  - nome: quem_faz
    descricao: quem vai fazer o trabalho e com que experiência
    obrigatoria: false
    omissao: assumir alguém que nunca programou, com ajuda de IA, e declará-lo
  - nome: tempo_disponivel
    descricao: quantas horas por semana existem mesmo para isto
    obrigatoria: false
    omissao: não assumir, e dizer que a estimativa em semanas depende disso
encadeia_com: [PLA-04, PLA-07, PLA-08]
---

## Prompt

Olha para {{plano}} e dá-me uma estimativa honesta, feita para {{quem_faz}}. Sem
otimismo de vendedor. Só diagnóstico.

**Por fase.** Quanto tempo demora, e onde é provável que essa pessoa fique presa.
O sítio onde se fica preso interessa mais do que o número: é o que decide se a
fase demora um dia ou uma semana. Dá o tempo em horas de trabalho e converte para
semanas apenas se {{tempo_disponivel}} for conhecido.

**Os três maiores riscos.** As coisas com mais hipótese de fazer o projeto parar
ou disparar em custo. Para cada uma, uma forma de reduzir o risco já, e não mais
tarde.

**A parte mais incerta de todas.** Aquela em que nem tu sabes se vai funcionar.
Propõe uma experiência pequena, de poucas horas, que resolva essa dúvida antes de
se investir no resto. Diz o que essa experiência tem de mostrar para se poder
avançar, e o que significa se falhar.

Onde não souberes estimar, diz que não sabes e o que seria preciso descobrir
primeiro. Um número inventado com ar de confiança é pior do que uma incerteza
assumida.

## Porque importa

Projetos não morrem por serem difíceis, morrem por serem mais longos do que quem
os começou esperava. Saber onde se vai ficar preso, e provar a parte duvidosa com
uma experiência curta, é a diferença entre desistir a meio e chegar ao fim.

## Como saber se correu bem

- Cada fase tem tempo e, mais importante, o sítio onde se vai ficar preso
- Os três riscos vêm com forma de os reduzir desde já
- A experiência proposta é curta e tem critério de sucesso escrito
- As incertezas foram assumidas em vez de disfarçadas com números
- Nada foi construído
