---
id: SEG-10
nome: Campos que o utilizador não devia poder controlar
categoria: seguranca
nivel: situacional
modo: diagnostico
origem: ccp-55
gatilhos:
  - o formulário guarda os dados direto na base de dados
  - alguém pode promover-se a administrador
  - tenho um formulário de perfil que grava tudo
  - o registo aceita o que vier
  - será que dá para alguém mudar o próprio plano
nao_usar_quando:
  - o projeto não tem base de dados
  - o projeto não tem contas de utilizador
  - nenhum formulário escreve dados, tudo é só leitura
variaveis:
  - nome: alvo
    descricao: ficheiros, rotas ou funcionalidade a auditar
    obrigatoria: false
    omissao: auditar o projeto inteiro
  - nome: campos_sensiveis
    descricao: campos que nunca devem vir do cliente
    obrigatoria: false
    omissao: usar a lista por defeito do template
  - nome: validador
    descricao: a biblioteca de validação usada no projeto
    obrigatoria: false
    omissao: detetar no projeto, e propor a correção em pseudocódigo se não houver nenhuma
encadeia_com: [SEG-05, SEG-09, SEG-08]
---

## Prompt

Só diagnóstico, não alteres código.

Em {{alvo}}, encontra todos os sítios onde dados vindos do utilizador são
guardados diretamente na base de dados: inserções e atualizações feitas a partir
do corpo do pedido, de dados de formulário ou de conteúdo enviado, em perfis,
definições, registo e afins.

Para cada um, verifica se o utilizador podia enviar {{campos_sensiveis}}. Na
falta de lista, usa esta: papel, administrador, plano, escalão, dono, referência
a outro utilizador, saldo, créditos, estado de verificação, estado de pagamento,
datas de criação e identificadores internos.

Assume que quem ataca edita o pedido à mão antes de o enviar e acrescenta esses
campos. Não precisa do formulário para isso.

Procura em especial o padrão que causa quase todos estes casos: código que aceita
o objeto inteiro que veio no pedido e o entrega à base de dados, em vez de
escolher explicitamente os campos permitidos.

Devolve: ficheiro e linha | campos que passam sem filtro | o que a pessoa
conseguia em concreto, por exemplo tornar-se administrador, mudar o dono de um
registo, ficar com saldo grátis.

Propõe para cada caso uma lista explícita de campos permitidos, escrita com
{{validador}}, mas não a apliques.

## Porque importa

Um formulário envia mais coisas do que as que se veem no ecrã, e nada impede
alguém de acrescentar campos ao pedido antes de o enviar. Se o código aceitar
tudo o que recebe, a pessoa promove-se a administrador sozinha, sem sair da
página de perfil.

## Como saber se correu bem

- Devolveu uma tabela com ficheiro e linha
- Não alterou ficheiro nenhum
- Para cada caso, disse o que um atacante conseguiria
- Encontrou os sítios que aceitam o objeto inteiro em vez de campos escolhidos
- A lista de campos permitidos ficou proposta e por aplicar
