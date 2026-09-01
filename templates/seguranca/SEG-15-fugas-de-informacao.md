---
id: SEG-15
nome: O que a aplicação deixa escapar sem dar por isso
categoria: seguranca
nivel: situacional
modo: diagnostico
origem: ccp-60
gatilhos:
  - o erro mostra coisas técnicas ao utilizador
  - outro site consegue chamar a minha API
  - o que é que os meus registos guardam
  - apareceu-me um erro com o nome das tabelas
  - isto revela se um email já existe
nao_usar_quando:
  - o projeto não tem servidor nem endereços próprios
  - a preocupação é com chaves no código, usar SEG-01
variaveis:
  - nome: dominios_permitidos
    descricao: que sites devem mesmo poder chamar esta aplicação
    obrigatoria: false
    omissao: assumir que só o próprio site e assinalar qualquer permissão mais larga
encadeia_com: [SEG-09, SEG-16, SEG-13]
---

## Prompt

Só diagnóstico, tema fugas de informação. Quatro frentes.

**Quem pode chamar.** Alguma resposta permite que qualquer site faça pedidos, e
ainda por cima com as credenciais do visitante. Verifica se a permissão é aberta
a todos ou reflete automaticamente quem pergunta, em vez de estar limitada a
{{dominios_permitidos}}. Aberta com credenciais deixa outro site agir em nome dos
meus utilizadores.

**Cabeçalhos de proteção.** Falta alguma das proteções que o navegador aplica se
lhe disserem: política de conteúdos, recusa de adivinhar tipos de ficheiro,
obrigação de ligação segura, proibição de a página ser embebida noutro site.

**Erros.** Em produção, o utilizador vê detalhes internos: caminhos de ficheiros,
nomes de tabelas, versões, rastreio da falha. As mensagens de login e de registo
revelam se um endereço de email já está registado.

**Registos.** O que fica gravado nos registos: dados pessoais, credenciais,
conteúdos inteiros de pedidos. Verifica também quem tem acesso a esses registos.

Devolve por item: ficheiro e linha | o que escapa | quem aproveita e como | o que
corrige.

Não alteres nada.

## Porque importa

Nenhuma destas falhas dá acesso direto a nada, e é por isso que ficam anos sem
ser reparadas. O que fazem é entregar a quem procura o mapa do sistema, e reduzir
o trabalho de um ataque a sério. Fugas somam-se.

## Como saber se correu bem

- As quatro frentes foram cobertas
- A permissão de quem pode chamar foi avaliada em conjunto com as credenciais
- Ficou claro o que o utilizador vê quando há erro em produção
- Os registos foram inspecionados quanto a dados pessoais
- Nada foi alterado
