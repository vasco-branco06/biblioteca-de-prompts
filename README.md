# Biblioteca de prompts

Catálogo de métodos de trabalho que o Claude consulta sozinho. Descreve-se a
tarefa em linguagem normal, ele escolhe o template que serve, preenche-o com o
contexto da conversa e executa-o. Não há copiar nem colar.

São 92 templates e 3 regras permanentes, arrumados em onze categorias.

## Como se usa

Não se faz nada de especial. Escreve-se o pedido como se escreveria a uma pessoa:

> o site está lento

O Claude lê o índice, escolhe, e avisa numa linha antes de trabalhar:

> Uso o PER-03 (as três maiores lentidões) porque disseste que o site está lento.

Se nenhum template servir, diz isso e trabalha à mesma, sem forçar uma
correspondência que não existe. Escolher a martelo é pior do que não escolher.

Para forçar a consulta, basta pedir: `usa o melhor prompt` ou `usa a biblioteca`.

## O que está aqui dentro

| Pasta | O que é |
|---|---|
| `SKILL.md` | as regras de escolha e o índice completo, gerado |
| `templates/` | um ficheiro por template, em onze categorias |
| `regras/` | comportamento permanente, para colar no `CLAUDE.md` de um projeto |
| `fonte/` | a coleção original, intacta, tal como veio |
| `ferramentas/` | o gerador do índice e o registo de utilizações |
| `registo/` | que templates se usam e quais nunca se tocaram |
| `INSTRUCOES.md` | a especificação a partir da qual isto foi construído |

## Anatomia de um template

Cada ficheiro tem o texto do prompt com variáveis em `{{chave}}`, a explicação
do porquê em linguagem simples, e a lista de sinais de que correu bem. No
cabeçalho estão os gatilhos, que são as frases que o disparam, e as condições em
que não se deve usar.

Há três modos. Um template de `diagnostico` nunca altera ficheiros, mesmo que o
pedido pareça pedir a correção. Um de `execucao` altera, e anuncia o que vai
mudar antes de mudar. Um de `regra` nunca se executa: descreve postura e vive no
`CLAUDE.md` do projeto.

## Acrescentar um template

Copia um ficheiro parecido, muda o cabeçalho e o texto, e corre:

    python ferramentas/gerar_indice.py

O índice do `SKILL.md` nunca se escreve à mão. O gerador recusa-se a correr se
um template ficar sem identificador ou sem gatilhos.

Os gatilhos são o que faz isto acertar ou falhar. Escreve-os como se fala. "o
site está lento" é um bom gatilho. "otimização de performance" não é.

## Instalação

A pasta é a biblioteca. Existe uma cópia e mais nenhuma. Para o Claude Code a
encontrar em qualquer projeto, cria-se uma junção do Windows, que não precisa de
privilégios de administrador:

    mklink /J "%USERPROFILE%\.claude\skills\biblioteca-de-prompts" "C:\Users\Admin\Desktop\prompt maneger"

No Cowork basta ligar a pasta como contexto. Fica uma limitação conhecida: aí a
skill não aparece na lista da conta, e o disparo automático é menos fiável do
que no Claude Code.

## De onde veio

A base são 78 prompts de um curso de programação assistida por IA. Estão em
`fonte/colecao-original.md` tal como vieram, sem uma vírgula alterada, e o campo
`origem` de cada template aponta para o número correspondente.

Os 92 templates não são cópia dessa coleção. Cada entrada foi reescrita para
servir qualquer projeto em vez de um caso concreto: as tecnologias passaram a
variáveis, os gatilhos foram escritos de raiz, e acrescentaram-se as secções de
quando não usar e de como saber que correu bem. Dezassete são de raiz, para
marketing, estudo e dados, áreas que a coleção original não cobria.

## Registo

No fim de cada utilização acrescenta-se uma linha:

    python ferramentas/registar_uso.py PER-03 --resumo "site lento na listagem" --resultado bom

Serve para, daqui a uns meses, ver o que se usa mesmo e o que nunca se tocou. O
script recusa identificadores que não existam, para o registo não encher de
lixo.

## Estado

As 78 entradas da coleção estão convertidas ou classificadas como regra, os 17
novos estão escritos, e a bateria de aceitação passa sem falsos disparos.
