---
id: DAD-02
nome: Análise exploratória guiada por perguntas de negócio
categoria: dados
nivel: recomendado
modo: diagnostico
origem: novo
gatilhos:
  - o que é que estes dados me dizem
  - tenho isto tudo e não sei o que fazer com os dados
  - quero perceber o que se está a passar nas vendas
  - analisa-me este ficheiro
  - que conclusões se tiram daqui
nao_usar_quando:
  - o ficheiro ainda não foi verificado quanto a qualidade, usar DAD-01 primeiro
  - o que se quer é transformar os dados e não interpretá-los, usar DAD-03
  - o que se quer é escolher a forma de os mostrar, usar DAD-05
variaveis:
  - nome: ficheiro
    descricao: os dados a analisar
    obrigatoria: true
    omissao: perguntar
  - nome: perguntas
    descricao: as perguntas de negócio a que se quer responder
    obrigatoria: false
    omissao: propor três a cinco a partir das colunas e pedir confirmação antes de analisar
  - nome: ferramenta
    descricao: com que se analisa
    obrigatoria: false
    omissao: usar o que já está no projeto, e na dúvida ler com Python sem instalar nada
  - nome: periodo
    descricao: o intervalo de tempo que interessa
    obrigatoria: false
    omissao: usar todo o intervalo presente nos dados e dizer qual é
encadeia_com: [DAD-01, DAD-05, DAD-04]
---

## Prompt

Só diagnóstico. Analisa {{ficheiro}} com {{ferramenta}}, no período {{periodo}},
para responder a {{perguntas}}.

Começa pelas perguntas e não pelos dados. Uma análise que parte das colunas
produz gráficos bonitos que não decidem nada.

Para cada pergunta, antes de responder, diz uma de três coisas:

- **Estes dados respondem.** Explica com que colunas.
- **Respondem em parte.** Diz o que fica de fora e o que seria preciso ter.
- **Não respondem.** Diz porquê, e não improvises uma resposta aproximada.

Depois responde às que dá para responder, com estas regras:

1. Dá o número e a base sobre que ele foi calculado. Uma subida de trinta por
   cento sobre quatro casos não é uma subida, é ruído.
2. Compara sempre com alguma coisa: o período anterior, a média, o resto do
   conjunto. Um número isolado não significa nada.
3. Separa o que se observa do que se conclui. Duas coisas subirem ao mesmo tempo
   não faz uma causar a outra, e se não houver forma de distinguir, diz isso.
4. Aponta o que te surpreendeu nos dados, mesmo que não estivesse nas perguntas.
   É frequente estar aí o que interessa.
5. Diz onde a qualidade dos dados limita a confiança na resposta, ligando ao que
   o diagnóstico do ficheiro tiver encontrado.

Termina com as três perguntas seguintes que os dados sugerem, e o que seria
preciso recolher para lhes responder.

Não alteres o ficheiro nem crias versões limpas dele.

## Porque importa

O erro caro nesta tarefa não é calcular mal, é responder com confiança a uma
pergunta que os dados não conseguem responder. Dizer que não dá é um resultado
útil; um número inventado a partir de dados insuficientes leva a decisões que
custam dinheiro.

## Como saber se correu bem

- As perguntas foram confirmadas antes da análise
- Cada pergunta foi classificada quanto a poder ou não ser respondida
- Todos os números vêm com a base sobre que foram calculados
- Observação e conclusão estão separadas, sem causalidade assumida
- Nada foi alterado no ficheiro
