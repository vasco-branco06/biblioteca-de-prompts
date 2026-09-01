---
id: DIA-01
nome: Parar e diagnosticar, sem mexer em mais nada
categoria: diagnostico
nivel: recomendado
modo: diagnostico
origem: ccp-10
gatilhos:
  - para
  - isto está a piorar
  - não mexas mais
  - estás a fazer coisas que eu não pedi
  - já não percebo o que se está a passar aqui
nao_usar_quando:
  - ainda nada foi alterado nesta sessão e não há nada para explicar
  - a causa já é conhecida e o que falta é corrigir
  - o que se quer é desfazer o que foi feito, usar DIA-04
variaveis:
  - nome: sintoma
    descricao: o que está mal, tal como se vê
    obrigatoria: false
    omissao: usar o que foi dito na conversa e dizer o que se percebeu
encadeia_com: [DIA-02, DIA-04, DIA-05]
---

## Prompt

Para tudo. Não escrevas mais código, não corras comandos, não alteres ficheiros.
Só quero perceber o que se passa antes de decidir o próximo passo.

Responde por esta ordem:

1. O que fizeste nos últimos passos, em três a cinco frases simples. Sem
   justificações, só o que aconteceu.
2. Que ficheiros alteraste, pelo nome, e o que mudou em cada um.
3. Três hipóteses para {{sintoma}}, da mais provável para a menos, e o que
   esperarias observar se cada uma fosse a verdadeira.
4. O que eu posso verificar sozinho, agora, para separar as hipóteses.

Não corrijas nada. Não proponhas a correção da hipótese que achas mais provável.
Espera pela minha decisão.

Se alguma das últimas alterações foi feita por tua iniciativa e não por eu ter
pedido, diz isso de forma explícita. É a primeira coisa que quero saber.

## Porque importa

Quando alguma coisa parte, o instinto é continuar a mexer, e às vezes cada
tentativa afasta mais do estado que funcionava. Parar e pôr em cima da mesa o que
foi feito devolve o controlo a quem decide, e transforma a confusão numa lista de
hipóteses.

## Como saber se correu bem

- Nenhum ficheiro foi tocado depois do pedido
- Os ficheiros alterados aparecem pelo nome
- Há três hipóteses ordenadas por probabilidade, e não uma conclusão
- Cada hipótese diz o que se observaria se fosse a verdadeira
- As alterações feitas por iniciativa própria estão assinaladas
