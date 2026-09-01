---
id: DAD-01
nome: Diagnóstico de um ficheiro de dados
categoria: dados
nivel: essencial
modo: diagnostico
origem: novo
gatilhos:
  - este excel tem valores esquisitos
  - as contas não batem certo
  - recebi um ficheiro e não sei se posso confiar nele
  - há linhas repetidas nesta folha
  - antes de analisar isto quero saber se está bom
nao_usar_quando:
  - já se sabe qual é o problema e o que se quer é corrigi-lo, usar DAD-03
  - o pedido é responder a uma pergunta de negócio e não avaliar o ficheiro, usar DAD-02
  - o ficheiro tem menos de vinte linhas e vê-se a olho
variaveis:
  - nome: ficheiro
    descricao: caminho ou nome do ficheiro e a folha ou tabela a examinar
    obrigatoria: true
    omissao: perguntar qual é, não adivinhar entre vários
  - nome: ferramenta
    descricao: com que se examina, folha de cálculo, Python, Power Query, SQL
    obrigatoria: false
    omissao: usar o que já estiver no projeto, e na dúvida ler com Python sem instalar nada
  - nome: chave
    descricao: coluna ou conjunto de colunas que deveria identificar cada linha
    obrigatoria: false
    omissao: procurar candidatas a chave e propor a mais provável
  - nome: uso_previsto
    descricao: para que vai servir o ficheiro, porque define o que é grave
    obrigatoria: false
    omissao: assumir análise exploratória e declarar a assunção
encadeia_com: [DAD-02, DAD-03, DAD-04]
---

## Prompt

Só diagnóstico. Não corrijas nada, não reescrevas o ficheiro, não crias uma versão
limpa. Examina {{ficheiro}} com {{ferramenta}} e diz-me em que estado está.

Percorre por esta ordem e devolve uma secção por ponto:

1. Forma. Número de linhas e colunas, onde começa mesmo a tabela, se há
   cabeçalhos a mais, linhas de total no meio dos dados, células unidas ou folhas
   escondidas.
2. Tipos. Coluna a coluna, o que devia ser e o que está lá. Números guardados como
   texto, datas em formatos misturados, decimais com vírgula e ponto na mesma
   coluna, espaços à frente e atrás.
3. Buracos. Percentagem de vazios por coluna. Distingue vazio de zero, de "N/A"
   escrito à mão e de espaço em branco, porque não são a mesma coisa.
4. Duplicados. Quantas linhas se repetem por inteiro e quantas se repetem em
   {{chave}}. Se {{chave}} não for única, mostra três exemplos.
5. Categorias sujas. Em colunas de texto com poucos valores distintos, agrupa os
   que são o mesmo escrito de maneira diferente, com maiúsculas, acentos ou
   abreviaturas.
6. Valores impossíveis. Datas no futuro, quantidades negativas onde não faz
   sentido, extremos que destoam do resto por uma ordem de grandeza.

Devolve no fim uma tabela com: problema, colunas afetadas, quantas linhas,
gravidade para {{uso_previsto}}, e o que seria preciso decidir para o resolver.

Ordena por gravidade, não pela ordem das colunas. Onde não conseguires distinguir
um erro de um caso legítimo, diz isso em vez de decidir por mim.

## Porque importa

Um ficheiro sujo não dá erro. Dá um resultado com ar de correto que ninguém
verifica. Meia hora a olhar para o estado dos dados evita reconstruir uma análise
inteira depois de alguém reparar que metade das datas estava trocada.

## Como saber se correu bem

- Nenhum ficheiro foi alterado nem criado
- Cada problema veio com contagem de linhas, não com uma impressão vaga
- Vazio, zero e texto "N/A" foram tratados como coisas diferentes
- A lista está ordenada por gravidade e ligada ao uso previsto
- Os casos ambíguos ficaram marcados como decisão minha
