---
id: SEG-09
nome: A proteção tem de estar no servidor, não no ecrã
categoria: seguranca
nivel: situacional
modo: diagnostico
origem: ccp-54
gatilhos:
  - escondi o botão de administrador, chega
  - a verificação está toda num sítio só
  - o que acontece se alguém chamar isto diretamente
  - só os administradores é que veem esta opção
  - tenho a proteção na camada de entrada
nao_usar_quando:
  - o projeto não tem contas nem papéis de utilizador
  - a pergunta é sobre dados por dono, usar SEG-08
  - não existem chamadas ao servidor, é um site só de conteúdo
variaveis:
  - nome: camada_intermedia
    descricao: o mecanismo que filtra pedidos antes de chegarem ao código, se existir
    obrigatoria: false
    omissao: detetar no projeto e dizer o que foi encontrado
  - nome: alvo
    descricao: funções de servidor e rotas a examinar
    obrigatoria: false
    omissao: examinar todas as que leem ou alteram dados sensíveis
encadeia_com: [SEG-08, SEG-04, SEG-10]
---

## Prompt

Só diagnóstico.

Parte do princípio de que quem ataca chama {{alvo}} diretamente: sem passar pelo
ecrã, sem os botões que foram escondidos, sem passar por {{camada_intermedia}}.
Isto faz-se com uma ferramenta de linha de comandos e não exige nada de especial.

Para cada função de servidor e cada rota que lê ou altera dados sensíveis,
verifica se a primeira coisa que faz é:

a) confirmar que existe sessão autenticada, e
b) confirmar que essa sessão tem a permissão necessária,

dentro da própria função, e não noutro sítio qualquer.

Marca à parte todas as que dependem apenas de {{camada_intermedia}} para
autorizar. Essa camada é uma conveniência e não uma garantia: já houve falhas
públicas em que foi contornada, e basta uma configuração errada para deixar de
correr.

Marca também todas as que dependem de o botão estar escondido no ecrã. Esconder
não é proteger.

Devolve: ficheiro e linha | verifica sessão | verifica permissão | o que acontece
se for chamada diretamente sem login e sem ser administrador.

Ordena por gravidade. Não corrijas nada.

## Porque importa

O ecrã é sugestão, o servidor é lei. Tudo o que está escondido na interface
continua a existir e continua a responder a quem souber pedir. A única barreira
que aguenta é a que está dentro da função que faz o trabalho.

## Como saber se correu bem

- Nada foi alterado
- Cada função aparece com ficheiro e linha
- Sessão e permissão foram avaliadas como coisas separadas
- As que dependem só da camada intermédia estão marcadas
- Cada caso diz o que acontece se for chamada diretamente
