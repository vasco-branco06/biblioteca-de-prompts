---
id: SEG-11
nome: Avisos de serviços externos e tarefas agendadas
categoria: seguranca
nivel: situacional
modo: diagnostico
origem: ccp-56
gatilhos:
  - recebo avisos do sistema de pagamentos
  - tenho uma tarefa que corre todos os dias
  - como é que sei que o aviso veio mesmo de quem diz
  - alguém pode fingir que me pagou
  - tenho um endereço que recebe notificações automáticas
nao_usar_quando:
  - o projeto não recebe chamadas de serviços externos nem tem tarefas agendadas
  - a preocupação é com dados enviados por utilizadores em formulários, usar SEG-05
variaveis:
  - nome: servicos_externos
    descricao: que serviços enviam avisos automáticos a este projeto
    obrigatoria: false
    omissao: detetar pelas dependências e rotas do projeto
encadeia_com: [SEG-09, SEG-14, SEG-05]
---

## Prompt

Só diagnóstico.

Encontra todos os endereços que recebem chamadas automáticas: avisos de
{{servicos_externos}}, e todas as tarefas agendadas ou rotas internas disparadas
por um relógio.

**Para cada aviso externo, verifica:**

1. A assinatura da mensagem é verificada com o segredo do serviço antes de se
   confiar no conteúdo. Sem isto, qualquer pessoa envia um aviso falso.
2. A verificação usa o corpo original da mensagem e não uma versão já
   interpretada. Interpretar antes de verificar invalida a verificação.
3. Existe proteção contra repetição, por marca de tempo ou por identificador
   único, para o mesmo aviso legítimo não poder ser reenviado mil vezes.
4. O que acontece se a mensagem chegar duas vezes: cria dois registos, cobra duas
   vezes, envia dois emails.

**Para cada tarefa agendada, verifica** se está protegida por um segredo, ou se
qualquer pessoa na internet a consegue disparar quando quiser.

Assume alguém a enviar uma mensagem forjada a dizer que um pagamento foi
concluído. Diz-me, em cada caso, o que essa mensagem conseguiria desbloquear.

Devolve: endereço, ficheiro e linha | verifica assinatura | resiste a repetição |
o que se consegue forjar. Não apliques correções.

## Porque importa

Estes endereços têm de estar abertos à internet para receberem os avisos
legítimos, e por isso recebem também os falsos. Sem verificação de assinatura,
uma mensagem forjada a dizer que alguém pagou vale tanto como o pagamento.

## Como saber se correu bem

- A lista cobre avisos externos e tarefas agendadas
- Cada um diz se verifica a assinatura, e sobre que versão do corpo
- A proteção contra repetição foi avaliada em separado
- As tarefas agendadas sem segredo estão marcadas
- Nada foi corrigido
