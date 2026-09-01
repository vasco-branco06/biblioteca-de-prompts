---
id: SEG-07
nome: Olhar para o projeto como quem o quer atacar
categoria: seguranca
nivel: recomendado
modo: diagnostico
origem: ccp-30
gatilhos:
  - isto é seguro
  - por onde é que me podem atacar
  - quero uma verificação geral de segurança
  - nunca pensei nisto do ponto de vista da segurança
  - o que é que pode correr mal em termos de segurança
nao_usar_quando:
  - já se sabe qual é a área de risco e o que falta é a auditoria detalhada dessa área
  - o projeto ainda não tem nada construído
variaveis:
  - nome: alvo
    descricao: o projeto ou a parte a examinar
    obrigatoria: false
    omissao: examinar o projeto inteiro
  - nome: dados_valiosos
    descricao: o que existe aqui que valha a pena roubar ou estragar
    obrigatoria: false
    omissao: inferir do projeto e declarar o que foi assumido como valioso
encadeia_com: [SEG-02, SEG-04, SEG-08, SEG-14]
---

## Prompt

Só diagnóstico, não mexas em nada.

Olha para {{alvo}} como alguém que o quer atacar, e não como quem o construiu.
Assume que essa pessoa tem tempo, sabe programar, e consegue ver todo o código
que é enviado ao navegador.

Começa por dizer o que aqui vale a pena atacar: {{dados_valiosos}}, dinheiro,
capacidade de enviar mensagens em nome de outro, ou simplesmente derrubar o
serviço. Sem saber o que se quer roubar, a lista de ataques não tem ordem.

Depois dá-me as cinco formas mais prováveis de conseguir alguma dessas coisas.
Para cada uma:

- por onde entra
- que passos daria, em concreto, neste projeto e não em abstrato
- o que conseguia no fim
- o que existe hoje que o trava, se existir
- qual das auditorias detalhadas confirma esta suspeita

Ordena por probabilidade vezes estrago, e não por gravidade teórica. Uma falha
fácil que dá acesso a pouco pode ser pior do que uma difícil que dá acesso a
tudo.

Se o projeto estiver genuinamente bem protegido nalguma frente, diz. Uma lista em
que tudo é crítico não ajuda a decidir por onde começar.

## Porque importa

Quem constrói olha para o caminho que quer que as pessoas façam. Quem ataca olha
para todos os outros. Trocar de lado durante meia hora encontra mais problemas do
que reler o código com os mesmos olhos com que foi escrito.

## Como saber se correu bem

- Nada foi alterado
- Ficou dito primeiro o que aqui vale a pena atacar
- Os cinco caminhos são concretos e apontam para sítios deste projeto
- A ordem segue probabilidade e estrago, não gravidade teórica
- O que está bem protegido também foi dito
