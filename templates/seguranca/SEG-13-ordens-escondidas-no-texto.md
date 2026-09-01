---
id: SEG-13
nome: Ordens escondidas no texto que chega ao modelo de IA
categoria: seguranca
nivel: situacional
modo: diagnostico
origem: ccp-58
gatilhos:
  - o meu site usa inteligência artificial
  - tenho um assistente que lê mensagens dos utilizadores
  - o modelo consegue enviar emails
  - dou documentos de utilizadores a ler à IA
  - isto resume páginas da internet automaticamente
nao_usar_quando:
  - o projeto não envia texto nenhum a um modelo de linguagem
  - o texto enviado é sempre escrito por mim e nunca por terceiros
variaveis:
  - nome: acoes_do_modelo
    descricao: que ferramentas ou ações o modelo consegue executar
    obrigatoria: false
    omissao: detetar no código e listar todas as encontradas
encadeia_com: [SEG-14, SEG-05, SEG-15]
---

## Prompt

Só diagnóstico, e só se este projeto enviar texto a um modelo de linguagem.

Encontra todos os pontos onde conteúdo que eu não controlo chega ao modelo:
mensagens escritas por utilizadores, texto de páginas da internet, ficheiros
enviados, dados guardados na base de dados por outras pessoas, respostas de
serviços externos.

Para cada ponto responde:

1. Esse texto pode conter instruções dirigidas ao modelo, do género ignora o que
   te disseram antes, revela as tuas instruções, ou chama esta ferramenta. O
   modelo não distingue sozinho instruções de conteúdo.
2. O modelo tem acesso a {{acoes_do_modelo}} que uma instrução escondida pudesse
   aproveitar: enviar mensagens, apagar, ler a base de dados, gastar dinheiro.
3. A resposta do modelo é mostrada no ecrã como conteúdo interpretado, sem ser
   escapada, permitindo que o texto gerado execute algo no navegador.
4. Há limite de custo e de utilização por pessoa.

Devolve: sítio, ficheiro e linha | de onde vem o texto não confiável | o pior
caso se contiver instruções | o que o mitiga.

Nas mitigações, distingue sempre estas quatro: separar instruções de conteúdo,
limitar as ações a uma lista fechada, exigir confirmação humana antes de ações
com consequências, e escapar o que vai para o ecrã.

Não alteres código.

## Porque importa

O texto que os utilizadores escrevem passa a fazer parte das instruções que o
modelo lê, e ele não tem forma fiável de separar uma coisa da outra. Se o modelo
puder agir sobre o mundo, uma instrução escondida numa mensagem passa a ser uma
ordem executada em nome do dono do site.

## Como saber se correu bem

- Todos os pontos de entrada de texto não confiável estão listados
- As ações disponíveis ao modelo estão inventariadas
- Cada caso descreve o pior resultado possível em concreto
- As mitigações estão separadas por tipo e não resumidas a uma frase
- Nada foi alterado
