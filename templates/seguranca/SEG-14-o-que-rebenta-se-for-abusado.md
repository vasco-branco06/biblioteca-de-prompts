---
id: SEG-14
nome: O que me rebenta a conta ou o servidor se for abusado
categoria: seguranca
nivel: situacional
modo: diagnostico
origem: ccp-59
gatilhos:
  - e se alguém puser um programa a chamar isto sem parar
  - tenho medo de receber uma fatura enorme
  - isto pode ser usado para enviar spam em meu nome
  - quanto é que alguém me pode fazer gastar
  - o servidor aguenta se alguém quiser abusar
nao_usar_quando:
  - o site não tem funcionalidades que custem dinheiro nem enviem mensagens
  - a preocupação é só com o login, usar SEG-16
variaveis:
  - nome: operacoes_caras
    descricao: o que aqui custa dinheiro ou consome muitos recursos por utilização
    obrigatoria: false
    omissao: detetar no projeto e listar tudo o que for pago por uso
encadeia_com: [SEG-16, SEG-11, SEG-13, PLA-08]
---

## Prompt

Só diagnóstico.

Identifica os pontos caros ou abusáveis que não têm limite de ritmo. Além do
login, procura em especial:

- recuperação e reenvio de palavra-passe
- criação de contas
- envio de mensagens, convites ou notificações
- chamadas a {{operacoes_caras}}, sobretudo as que são pagas por utilização
- geração de documentos, exportações e relatórios
- consultas pesadas sem limite de resultados nem paginação

Para cada um, responde com um programa a chamar mil vezes por minuto em mente:

1. Consegue fazer-me gastar dinheiro, e quanto por hora.
2. Consegue encher-me a base de dados.
3. Consegue enviar mensagens em meu nome, queimando a reputação do meu domínio.
4. Consegue deixar o serviço indisponível para toda a gente.

Verifica se existe limite por pessoa autenticada e também por origem do pedido.
Um limite só por conta não trava quem cria contas novas.

Devolve: ponto, ficheiro e linha | custo ou impacto do abuso | tem limite | limite
que sugeres, com o número.

Ordena pelo estrago por hora e não pela facilidade. Não implementes nada.

## Porque importa

Estas funcionalidades funcionam bem com pessoas e mal com programas. Sem travão,
uma noite chega para transformar uma funcionalidade normal numa fatura de
centenas de euros, ou para pôr o domínio numa lista negra de spam.

## Como saber se correu bem

- A lista inclui tudo o que é pago por utilização
- Cada ponto tem o estrago estimado por hora de abuso
- Foi verificado o limite por conta e por origem
- Os limites sugeridos vêm com números concretos
- Nada foi implementado
