---
id: DAD-03
nome: Transformação de dados passo a passo e reproduzível
categoria: dados
nivel: recomendado
modo: execucao
origem: novo
gatilhos:
  - tenho de limpar isto antes de usar
  - preciso de juntar estes dois ficheiros
  - todos os meses faço isto à mão
  - preciso de mudar o formato destas colunas
  - quero automatizar esta preparação de dados
nao_usar_quando:
  - ainda não se sabe o que está mal no ficheiro, usar DAD-01 primeiro
  - é uma correção pontual num ficheiro que nunca mais se vai repetir
  - o que se quer é analisar e não transformar, usar DAD-02
variaveis:
  - nome: ficheiro
    descricao: os dados de partida
    obrigatoria: true
    omissao: perguntar
  - nome: resultado
    descricao: como devem ficar os dados no fim, e para que vão servir
    obrigatoria: true
    omissao: perguntar, porque sem destino não há transformação certa
  - nome: ferramenta
    descricao: onde se faz a transformação
    obrigatoria: false
    omissao: Power Query, por ser o que existe no Excel sem instalar nada, e dizer que foi essa a escolha
  - nome: periodicidade
    descricao: com que frequência isto se repete
    obrigatoria: false
    omissao: assumir que se repete e construir para ser reutilizável
encadeia_com: [DAD-01, DAD-02, DAD-04]
---

## Prompt

Transforma {{ficheiro}} até {{resultado}}, usando {{ferramenta}}, sabendo que
isto se repete {{periodicidade}}.

Diz-me primeiro os passos que tencionas dar e espera. Só depois executas.

Regras que valem para qualquer ferramenta:

1. **Nunca alteres o ficheiro de origem.** A transformação lê e escreve noutro
   lado. Se a origem for tocada, a próxima vez começa de um sítio diferente e
   nada bate certo.
2. **Um passo, uma coisa.** Cada passo com nome que diga o que faz, e não passo
   um, passo dois. Daqui a três meses é o nome que permite perceber onde corrigir.
3. **Sem edições manuais pelo meio.** Se um valor for corrigido à mão, a
   transformação deixa de ser repetível e a próxima execução perde a correção.
   Se houver mesmo casos manuais, ficam numa tabela de exceções à parte, também
   ela lida como dados.
4. **Prevê o que muda da próxima vez:** linhas novas, colunas que mudam de nome,
   valores que ainda não apareceram, ficheiro com mais uma folha. Diz o que
   acontece em cada um destes casos, e o que rebenta em silêncio.
5. **Verifica no fim.** Compara contagem de linhas antes e depois, e explica
   qualquer diferença. Linhas que desaparecem sem explicação são o erro mais
   comum e o mais difícil de detetar.

Entrega três coisas: os dados transformados, os passos escritos por palavras
minhas para eu conseguir repetir sozinho, e a lista do que pode correr mal na
próxima vez.

Se {{ferramenta}} não conseguir fazer algum passo, diz e propõe alternativa, em
vez de contornares com uma solução manual escondida.

## Porque importa

A transformação feita à mão resolve hoje e volta a dar trabalho no mês seguinte,
com o agravante de ninguém se lembrar exatamente do que fez. Uma transformação
com passos nomeados repete-se com um clique e corrige-se num sítio só.

## Como saber se correu bem

- O ficheiro de origem ficou intacto
- Os passos foram apresentados antes de serem executados
- Cada passo tem nome que diz o que faz
- Não há correções manuais fora de uma tabela de exceções
- As contagens antes e depois foram comparadas e as diferenças explicadas
