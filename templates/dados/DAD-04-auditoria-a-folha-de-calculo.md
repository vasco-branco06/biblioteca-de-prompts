---
id: DAD-04
nome: Auditoria a um cálculo ou modelo de folha de cálculo
categoria: dados
nivel: situacional
modo: diagnostico
origem: novo
gatilhos:
  - as contas não batem certo
  - este total está errado e não sei porquê
  - herdei esta folha de outra pessoa
  - vou apresentar isto e quero ter a certeza
  - confias neste ficheiro de orçamento
nao_usar_quando:
  - o problema são os dados de entrada e não as fórmulas, usar DAD-01
  - a folha é uma lista simples sem cálculos
  - o que se quer é transformar dados, usar DAD-03
variaveis:
  - nome: ficheiro
    descricao: a folha a auditar, e a folha ou área dentro dela
    obrigatoria: true
    omissao: perguntar
  - nome: resultado_critico
    descricao: as células cujo valor é o que interessa no fim
    obrigatoria: false
    omissao: identificar os totais e resultados finais e confirmar comigo quais são os críticos
  - nome: uso
    descricao: para que serve este número, porque define a gravidade de um erro
    obrigatoria: false
    omissao: assumir uso em decisão e declarar a assunção
encadeia_com: [DAD-01, DAD-03, DAD-05]
---

## Prompt

Só diagnóstico. Não corrijas fórmulas nem alteres o ficheiro. Audita {{ficheiro}},
com atenção especial a {{resultado_critico}}, que serve para {{uso}}.

Percorre estes pontos, que são onde estes erros se escondem:

1. **Números escritos dentro de fórmulas.** Um valor cravado numa fórmula é
   invisível e ninguém o atualiza. Lista todos, com a célula.
2. **Intervalos que não chegam ao fim.** Somas e procuras que param antes da
   última linha, tipicamente porque foram acrescentadas linhas depois. É a causa
   número um de totais errados.
3. **Fórmulas inconsistentes numa coluna.** Uma coluna em que quase todas as
   células têm a mesma fórmula e duas ou três têm outra coisa, ou um valor
   escrito à mão.
4. **Linhas ocultas ou filtradas dentro de somas.** O total inclui o que não se
   vê, ou exclui o que se vê, conforme a função usada.
5. **Percentagens e bases.** Percentagem calculada sobre a base errada,
   percentagens somadas quando não se somam, variações calculadas ao contrário.
6. **Arredondamentos.** Onde se arredonda, e se o arredondamento acontece antes
   ou depois de somar. Faz diferença e costuma explicar cêntimos que não batem.
7. **Referências circulares e a outros ficheiros**, sobretudo ficheiros que
   podem já não estar onde estavam.
8. **Datas e texto disfarçado de número**, que fazem somas ignorar linhas em
   silêncio.

Depois faz a verificação que apanha o que a leitura não apanha: escolhe uma
linha e recalcula o resultado à mão, passo a passo, e compara com o que a folha
diz. Se não bater, encontraste o problema. Faz isto para pelo menos duas linhas,
uma normal e uma que pareça atípica.

Devolve uma tabela: célula ou intervalo | problema | efeito no resultado crítico,
com número se conseguires quantificar | gravidade para o uso previsto.

Ordena por efeito no resultado final e não pela ordem das células.

## Porque importa

Uma folha de cálculo errada não avisa. Devolve um número plausível que ninguém
questiona, e decide-se com base nele. Os erros clássicos, o intervalo que ficou
para trás e o número cravado numa fórmula, são invisíveis a olho e mantêm-se
durante anos.

## Como saber se correu bem

- Nada foi corrigido nem alterado no ficheiro
- Os números dentro de fórmulas estão listados com a célula
- Os intervalos foram verificados até à última linha com dados
- Pelo menos duas linhas foram recalculadas à mão e comparadas
- Cada problema traz o efeito no resultado que interessa
