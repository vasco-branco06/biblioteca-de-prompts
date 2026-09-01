---
id: PER-06
nome: Consultas repetidas dentro de ciclos
categoria: performance
nivel: situacional
modo: diagnostico
origem: ccp-66
gatilhos:
  - a página com a lista está lenta
  - com poucos dados era rápido e agora arrasta
  - quanto mais registos mais lento fica
  - a listagem demora imenso a abrir
  - isto faz muitos pedidos à base de dados
nao_usar_quando:
  - o projeto não tem base de dados nem chamadas a serviços externos
  - a lentidão está no que se descarrega e não no servidor, usar PER-07
  - ainda não se sabe onde está a lentidão, usar PER-03 primeiro
variaveis:
  - nome: alvo
    descricao: o ecrã ou a operação lenta
    obrigatoria: false
    omissao: examinar as listagens e os ecrãs com mais dados
encadeia_com: [PER-03, TES-06]
---

## Prompt

Só diagnóstico. Procura em {{alvo}} sítios onde o código vai buscar uma lista e
depois, para cada item dessa lista, faz mais um pedido separado.

É o problema que multiplica pedidos: com dez itens são onze pedidos, com mil são
mil e um. Não se nota enquanto há poucos dados e estrangula a aplicação quando
ela começa a ter uso a sério.

Procura em quatro sítios, não só no óbvio:

1. Ciclos com consultas à base de dados lá dentro.
2. Ciclos com chamadas a serviços externos lá dentro.
3. Relações carregadas item a item em vez de todas de uma vez.
4. O mesmo padrão escondido dentro de componentes que se repetem numa lista, onde
   cada um vai buscar os seus próprios dados.

Para cada caso encontrado devolve: ficheiro e linha | quantos pedidos faz com dez
itens e com mil | como buscar tudo de uma vez.

Ordena do mais grave para o menos, sendo grave o que cresce mais depressa com o
número de itens.

Não alteres nada. Mostra-me a lista primeiro.

## Porque importa

É o defeito de desempenho mais comum e o mais traiçoeiro, porque durante o
desenvolvimento tudo parece rápido. O momento em que aparece é exatamente o
momento em que o projeto começa a correr bem e a ter dados a sério.

## Como saber se correu bem

- Nada foi alterado
- Cada caso tem ficheiro e linha
- Está estimado o número de pedidos com poucos e com muitos itens
- Foram procurados também os casos escondidos dentro de componentes repetidos
- A ordem segue a rapidez com que o problema cresce
