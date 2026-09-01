---
id: SEG-04
nome: Que páginas exigem login e quais estão abertas
categoria: seguranca
nivel: recomendado
modo: diagnostico
origem: ccp-27
gatilhos:
  - qualquer pessoa consegue entrar na área de administração
  - que páginas é que estão protegidas
  - isto precisa de login
  - esqueci-me de trancar alguma página
  - quem é que consegue ver o quê
nao_usar_quando:
  - o site não tem contas de utilizador nem área privada
  - a pergunta é sobre a base de dados e não sobre páginas, usar SEG-02
  - a pergunta é sobre chamadas ao servidor e não sobre páginas, usar SEG-09
variaveis:
  - nome: papeis
    descricao: os tipos de utilizador que existem
    obrigatoria: false
    omissao: detetar no código e listar os que forem encontrados
encadeia_com: [SEG-09, SEG-08, SEG-02]
---

## Prompt

Só diagnóstico. Faz o levantamento de acessos do projeto.

Lista todas as páginas e funcionalidades e, para cada uma, diz:

- exige login, ou está aberta a qualquer visitante
- se exige, que papel de {{papeis}} é preciso
- onde está escrita essa verificação, com ficheiro e linha
- o que se vê se lá chegar quem não devia

Depois faz três coisas que a lista sozinha não faz:

1. Aponta as que deviam estar protegidas e não estão. Considera suspeita qualquer
   página de administração, de gestão, de listagem de utilizadores, de
   configuração ou de dados de outras pessoas.
2. Aponta as que estão protegidas por estarem escondidas, ou seja, aquelas cuja
   única proteção é ninguém saber o endereço. Isso não é proteção.
3. Aponta as que verificam se há sessão iniciada mas não verificam qual é o papel,
   deixando um utilizador normal entrar numa área de administração.

Ordena por gravidade e diz, em cada caso, o que uma pessoa mal-intencionada
conseguiria ver ou fazer.

Não corrijas nada.

## Porque importa

Esta é a verificação mais básica de todas e a que mais vezes falha, porque as
páginas de administração são construídas depressa e a proteção fica para depois.
Basta uma página esquecida para os dados de toda a gente ficarem à vista.

## Como saber se correu bem

- Nenhum ficheiro foi alterado
- A lista cobre todas as páginas, incluindo as antigas e as de teste
- Cada proteção aparece com ficheiro e linha
- As páginas protegidas apenas por endereço secreto estão assinaladas
- Está separado quem tem sessão de quem tem permissão
