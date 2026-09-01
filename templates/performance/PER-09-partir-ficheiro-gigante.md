---
id: PER-09
nome: Partir o ficheiro ou a função que ficou gigante
categoria: performance
nivel: situacional
modo: execucao
origem: ccp-69
gatilhos:
  - este ficheiro tem duas mil linhas
  - já ninguém percebe o que está aqui
  - esta função faz coisas de mais
  - tenho um ficheiro que faz tudo
  - isto precisa de ser dividido
nao_usar_quando:
  - o ficheiro é grande mas simples, como uma lista de dados
  - não existem testes nem forma de verificar que nada partiu, correr PER-01 primeiro
  - o problema é a lógica estar repetida e não concentrada, usar PER-08
variaveis:
  - nome: alvo
    descricao: o ficheiro ou função a dividir
    obrigatoria: false
    omissao: encontrar os três maiores e mais complicados, e propor o pior
encadeia_com: [PER-01, PER-08, PER-10]
---

## Prompt

Encontra os três ficheiros ou funções mais compridos e mais complicados do
projeto. Compridos e complicados não são a mesma coisa: diz as duas medidas.

Para {{alvo}}, ou para o pior deles, propõe primeiro o plano. Não mexas em nada
ainda.

O plano diz:

- em que partes se divide, e qual é a responsabilidade única de cada uma
- que nome tem cada parte, e porquê
- o que fica onde estava e porquê
- que ficheiros passam a depender de que outros
- o que pode partir durante a divisão

Espera pela minha aprovação.

Se eu aprovar, executa uma divisão de cada vez. A cada passo:

1. Move o que combinámos, sem mudar o comportamento nem aproveitar para melhorar
   nada pelo caminho.
2. Verifica que a aplicação continua a funcionar.
3. Guarda um ponto de retorno com uma mensagem a dizer o que saiu de onde para
   onde.
4. Para e espera que eu confirme antes do passo seguinte.

Se durante a divisão descobrires que uma parte não sai limpa, para e diz. Uma
divisão forçada deixa o código pior do que estava.

## Porque importa

Ficheiros enormes são difíceis de mudar sem partir, tanto para pessoas como para
uma IA que só consegue ler uma parte de cada vez. Um ponto de retorno por passo é
o que permite recuar um bocadinho em vez de recuar tudo.

## Como saber se correu bem

- O plano foi apresentado e aprovado antes de qualquer alteração
- Cada parte tem uma responsabilidade única e um nome que a descreve
- As divisões foram feitas uma de cada vez, com verificação entre elas
- Existe um ponto de retorno por passo, com mensagem descritiva
- O comportamento é igual ao do início
