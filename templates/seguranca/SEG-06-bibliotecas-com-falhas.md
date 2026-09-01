---
id: SEG-06
nome: Bibliotecas com falhas de segurança conhecidas
categoria: seguranca
nivel: recomendado
modo: diagnostico
origem: ccp-29
gatilhos:
  - as bibliotecas que uso são seguras
  - apareceu-me um aviso de vulnerabilidade
  - isto está desatualizado
  - devia atualizar as dependências
  - vi uma notícia sobre uma falha numa biblioteca
nao_usar_quando:
  - o projeto não usa bibliotecas externas
  - o que se procura são bibliotecas instaladas e não usadas, usar PER-11
variaveis:
  - nome: gestor
    descricao: o gestor de pacotes do projeto e o comando de auditoria correspondente
    obrigatoria: false
    omissao: detetar pelos ficheiros de dependências e dizer qual foi encontrado
encadeia_com: [PER-11, SEG-07]
---

## Prompt

Só diagnóstico. Não atualizes nada.

Corre a auditoria de segurança de {{gestor}} e lê o resultado. Depois traduz-mo,
porque o resultado bruto destas ferramentas é ilegível para quem não é técnico.

Para cada falha encontrada devolve:

- que biblioteca é e para que serve neste projeto
- gravidade
- se a falha é alcançável a partir do meu código, ou se está numa parte da
  biblioteca que o projeto nunca chama
- se é uma dependência que eu instalei ou uma que veio arrastada por outra
- o que a atualização parte, se partir alguma coisa

Separa em três grupos: atualizar agora, atualizar quando der, e ignorar com
razão explicada.

A distinção que mais interessa é a terceira do primeiro grupo. Uma falha grave
numa parte que o projeto nunca usa é menos urgente do que uma falha média num
caminho que corre a cada visita. Se não conseguires determinar se é alcançável,
diz que não conseguiste em vez de assumir.

Não escrevas nem apliques atualizações. Deixa os comandos escritos para eu
correr depois de aprovar.

## Porque importa

O projeto é feito de peças de outras pessoas, e algumas têm falhas já
descobertas, publicadas e conhecidas por quem procura alvos fáceis. A lista bruta
das ferramentas assusta e não ajuda a decidir; o que decide é saber quais é que
tocam mesmo no projeto.

## Como saber se correu bem

- Nenhuma biblioteca foi atualizada
- Cada falha vem traduzida para linguagem simples
- Está dito se a falha é alcançável a partir deste projeto
- As três listas existem e a terceira tem razões escritas
- Os comandos ficaram escritos por correr
