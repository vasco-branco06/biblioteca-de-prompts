---
id: SEG-05
nome: Validar tudo o que vem do utilizador
categoria: seguranca
nivel: recomendado
modo: diagnostico
origem: ccp-28
gatilhos:
  - os meus formulários são seguros
  - alguém pode escrever coisas estranhas nos campos
  - isto aceita qualquer coisa
  - tenho medo de ataques pelos formulários
  - o que acontece se escreverem código no campo
nao_usar_quando:
  - o projeto não recebe nada escrito por utilizadores
  - a preocupação é com campos que o utilizador não devia poder mudar, usar SEG-10
  - o texto do utilizador vai para um modelo de IA, usar SEG-13
variaveis:
  - nome: validador
    descricao: a biblioteca ou mecanismo de validação usado no projeto
    obrigatoria: false
    omissao: detetar no projeto, e se não existir nenhum dizê-lo como problema
  - nome: alvo
    descricao: formulários, rotas ou área a examinar
    obrigatoria: false
    omissao: examinar tudo o que recebe dados de fora
encadeia_com: [SEG-10, SEG-12, EXP-04]
---

## Prompt

Só diagnóstico. Percorre {{alvo}} e encontra todos os pontos onde entram dados
que vêm de fora: formulários, endereços, parâmetros, ficheiros, cabeçalhos,
respostas de serviços externos.

Para cada um, verifica e reporta:

1. Há validação, e onde está: só no navegador, só no servidor, ou nos dois. A
   validação que só existe no navegador não conta como proteção, porque quem
   ataca não usa o navegador.
2. O que é validado: existe, tem o tipo certo, está dentro dos limites, tem
   formato válido. Diz qual destas falta.
3. O que acontece com o valor a seguir: vai para uma consulta à base de dados,
   vai para o ecrã, vai para um comando, vai para um endereço. Cada destino tem
   um risco diferente e quero saber qual é.
4. Se {{validador}} está a ser usado de forma consistente ou se há sítios que
   escapam.

Devolve: ficheiro e linha | de onde vem o dado | onde é validado | o que falta |
o que se consegue fazer aproveitando a falha, descrito em linguagem simples.

Ordena por gravidade. Não corrijas nada.

## Porque importa

Tudo o que vem de fora tem de ser tratado como se tivesse sido escrito por
alguém a tentar partir o sistema, porque às vezes foi mesmo. A maior parte dos
ataques conhecidos entra por um campo em que ninguém se lembrou de verificar o
que lá vinha.

## Como saber se correu bem

- A lista cobre todas as entradas, e não só os formulários visíveis
- Está distinguido o que é validado no navegador do que é validado no servidor
- Cada caso diz para onde vai o valor depois de entrar
- O risco está descrito em linguagem que se percebe sem saber programar
- Nada foi alterado
