---
id: MKT-04
nome: Análise de um concorrente a partir do rasto público
categoria: marketing
nivel: recomendado
modo: diagnostico
origem: novo
gatilhos:
  - o que é que a concorrência anda a fazer
  - analisa-me este concorrente
  - porque é que eles vendem mais do que eu
  - como é que eles se posicionam
  - quero perceber contra quem estou a competir
nao_usar_quando:
  - o que se quer é auditar a minha própria página, usar MKT-05 ou EXP-01
  - não há acesso à internet nem a material público sobre o concorrente
  - o pedido implica obter informação que não é pública
variaveis:
  - nome: concorrente
    descricao: quem analisar, com o endereço do site
    obrigatoria: true
    omissao: perguntar
  - nome: aspetos
    descricao: o que interessa saber, preço, posicionamento, canais, conteúdo, público
    obrigatoria: false
    omissao: cobrir posicionamento, oferta, preço e canais, e dizer que foi essa a escolha
  - nome: eu
    descricao: com que produto ou serviço se está a comparar
    obrigatoria: false
    omissao: perguntar, porque sem termo de comparação a análise não conclui nada
encadeia_com: [MKT-01, MKT-05, MKT-06]
---

## Prompt

Só diagnóstico. Analisa {{concorrente}} em {{aspetos}}, usando apenas o que está
publicamente disponível, e compara com {{eu}}.

A regra que manda em tudo: cada afirmação tem de vir com o sítio onde a
encontraste. Se não encontrares, escreve que não encontraste. Não estimes preços,
não infiras número de clientes, não inventes datas de fundação nem tamanho de
equipa. Um concorrente descrito com números inventados é pior do que concorrente
nenhum, porque leva a decisões erradas com ar de fundamentadas.

Separa sempre três coisas, e etiqueta cada linha:

- **Observado.** Está escrito algures e tens a fonte.
- **Inferido.** Conclusão tua a partir do observado, com o raciocínio à vista.
- **Desconhecido.** Procuraste e não encontraste.

Percorre o rasto público: site e páginas de produto, tabela de preços, blogue,
redes sociais, ofertas de emprego, que ferramentas o site usa, avaliações de
clientes, notas de imprensa.

Devolve:

1. **Como se posicionam**, na frase deles e não na tua interpretação.
2. **O que vendem e por quanto**, ou a nota de que o preço não é público.
3. **A quem falam**, visível na linguagem que usam.
4. **Onde estão presentes** e com que frequência publicam.
5. **O que fazem melhor do que eu**, sem contemplações.
6. **O que não cobrem**, e se isso é descuido ou escolha deliberada.
7. **Três coisas acionáveis para mim**, ligadas ao que encontraste.

Não copies a estratégia deles. Diz o que aprendeste com ela.

## Porque importa

Olhar para um concorrente sem método produz uma lista de admirações e invejas
que não muda nada. O que muda alguma coisa é ver o que eles decidiram não fazer,
porque é aí que costuma estar o espaço livre.

## Como saber se correu bem

- Cada afirmação tem fonte, ou está marcada como desconhecida
- Observado, inferido e desconhecido estão etiquetados e separados
- Nenhum número foi estimado sem o dizer
- O posicionamento aparece nas palavras deles
- Há três ações concretas para mim, ligadas ao que foi encontrado
