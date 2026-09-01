---
id: PLA-04
nome: Fatiar o plano em fases que já funcionam
categoria: planeamento
nivel: recomendado
modo: execucao
origem: ccp-20
gatilhos:
  - tenho o plano e não sei por onde começar
  - isto é muito trabalho de uma vez
  - quero ver alguma coisa a funcionar depressa
  - divide-me isto em partes
  - por que fase é que começo
nao_usar_quando:
  - ainda não existe plano nenhum, usar PLA-02
  - o âmbito ainda não foi cortado, usar PLA-03 primeiro
  - o trabalho é pequeno e cabe todo numa sessão
variaveis:
  - nome: plano
    descricao: o documento a reorganizar
    obrigatoria: false
    omissao: usar o PLAN.md do projeto, e se não existir perguntar qual é
  - nome: numero_de_fases
    descricao: em quantas fases fatiar
    obrigatoria: false
    omissao: escolher o número que sair naturalmente do trabalho e explicar porquê
encadeia_com: [PLA-02, PLA-10, PLA-07]
---

## Prompt

Pega em {{plano}} e reorganiza-o em fases. Diz-me antes de escreveres que
ficheiro vais alterar.

A regra que manda em tudo: a fase 1 tem de ser a coisa mais pequena que já
funcione de ponta a ponta. Alguma coisa que eu consiga abrir e usar, mesmo que
faça quase nada.

Não me dês uma fase que seja só a base de dados, nem uma fase que seja só o
aspeto visual. Cada fase atravessa o sistema todo e acrescenta uma capacidade que
eu note ao usar.

Para cada fase escreve:

- O que passo a conseguir fazer no fim dela, dito na primeira pessoa.
- O que ainda vai faltar nesse momento.
- O teste manual que eu faço para confirmar que funciona, passo a passo, sem ler
  código.
- O que pode obrigar a voltar atrás a fases anteriores, se for o caso.

Ordena as fases por quem me dá valor visível mais depressa, e não pela ordem
técnica de construção.

Se {{numero_de_fases}} estiver definido, respeita-o. Se te obrigar a fases que
não funcionam sozinhas, diz-me isso em vez de as forçares.

## Porque importa

O erro clássico é construir durante semanas a parte que ninguém vê e nunca
chegar a ter uma coisa que se possa abrir. Quando cada fase entrega algo
utilizável, percebe-se cedo se o caminho está certo, e o projeto sobrevive a
interrupções.

## Como saber se correu bem

- A fase 1 é utilizável, mesmo que faça pouco
- Nenhuma fase é só uma camada técnica
- Cada fase tem um teste manual escrito que eu consigo seguir
- A ordem segue o valor visível e não a arrumação técnica
- Foi dito que ficheiro seria alterado antes de o ser
