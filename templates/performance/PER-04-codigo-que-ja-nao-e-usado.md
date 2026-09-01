---
id: PER-04
nome: Código que já não é usado por ninguém
categoria: performance
nivel: recomendado
modo: diagnostico
origem: ccp-40
gatilhos:
  - deve haver aqui muita coisa a mais
  - isto ainda é usado
  - tenho ficheiros que já não sei para que servem
  - quero limpar o projeto
  - sobrou código de coisas que já tirámos
nao_usar_quando:
  - o projeto é recente e ainda está a crescer depressa
  - o que se procura são bibliotecas instaladas e não usadas, usar PER-11
  - o que se procura são mensagens de depuração esquecidas, usar PER-05
variaveis:
  - nome: alvo
    descricao: pasta ou área a examinar
    obrigatoria: false
    omissao: examinar o projeto inteiro
encadeia_com: [PER-11, PER-05, PER-08]
---

## Prompt

Só diagnóstico. Procura em {{alvo}} código que já não está a ser usado em lado
nenhum: funções, ficheiros, componentes, variáveis, rotas, tabelas, estilos.

Para cada item, diz:

- onde está
- quando deixou de ser usado, se o histórico o disser
- que confiança tens de que está mesmo morto, e porquê

Essa última é a parte importante. Marca como incerto tudo o que possa ser
chamado de formas que a procura por nome não apanha: chamadas construídas por
texto, carregamento dinâmico, referências em ficheiros de configuração, código
usado apenas em produção, pontos de entrada externos, funcionalidades atrás de
interruptores desligados.

Separa em três listas: morto com certeza, provavelmente morto, e não consigo
determinar.

Não apagues nada. Nem sequer o que estiver na primeira lista. Mostra-me primeiro
e espera.

Para a primeira lista, propõe a ordem de remoção, do mais isolado para o mais
entrelaçado, e diz o que se ganha em cada passo.

## Porque importa

Código morto ocupa espaço na cabeça de quem lê, incluindo a de uma IA que
continue o trabalho e o tome por vivo. Ao mesmo tempo, apagar código que afinal
ainda era chamado parte a aplicação em produção, e por isso a certeza importa
mais do que a limpeza.

## Como saber se correu bem

- Nada foi apagado
- Cada item tem o grau de confiança explicado
- As formas de chamada que a procura por nome não apanha foram consideradas
- Existem três listas separadas por certeza
- A ordem de remoção proposta vai do mais isolado ao mais entrelaçado
