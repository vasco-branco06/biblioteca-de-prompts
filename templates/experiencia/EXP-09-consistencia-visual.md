---
id: EXP-09
nome: Consistência visual e conjunto mínimo de decisões
categoria: experiencia
nivel: situacional
modo: diagnostico
origem: ccp-64
gatilhos:
  - tenho cinco vermelhos quase iguais
  - os botões estão todos ligeiramente diferentes
  - isto parece amador mas não sei porquê
  - cada página tem espaçamentos diferentes
  - quero organizar as cores e os tamanhos
nao_usar_quando:
  - o projeto tem uma página só
  - o problema é a falta de carácter e não a incoerência, usar EXP-05
  - o projeto já usa um conjunto de decisões visuais definido e cumprido
variaveis:
  - nome: escala_espacos
    descricao: a escala de espaçamentos a adotar
    obrigatoria: false
    omissao: usar 4, 8, 12, 16, 24, 32 e justificar desvios
encadeia_com: [EXP-05, EXP-07, PER-10]
---

## Prompt

Só diagnóstico. Audita a coerência visual do projeto e mostra cada incoerência
com ficheiro e linha.

1. **Cores.** Lista todos os valores de cor usados e agrupa os que são quase
   iguais, por exemplo dois vermelhos com um dígito de diferença. Para cada grupo,
   diz qual devia sobreviver e onde os outros aparecem.
2. **Espaçamentos.** Identifica margens e espaços avulsos que fogem a
   {{escala_espacos}}. Não me dês a lista toda; agrupa por valor e diz quantas
   ocorrências tem cada um.
3. **Tipografia.** Quantos tamanhos e pesos de letra existem, e quais são
   redundantes. Mais de seis tamanhos num projeto pequeno é quase sempre acidente
   e não decisão.
4. **Componentes repetidos.** Botões, cartões e campos com estilos ligeiramente
   diferentes que deviam ser o mesmo.
5. **Cantos e sombras.** Os mesmos valores repetidos com pequenas variações.

Propõe o conjunto mínimo de decisões nomeadas, cor, espaço, tipografia, cantos e
sombra, e diz onde substituir cada valor solto pelo nome correspondente.

Ordena pelo que se nota mais: as cores e os botões notam-se, uma sombra com dois
pontos de diferença não.

Não alteres ficheiros. Se alguma variação for intencional e justificada, marca-a
como tal em vez de a uniformizares.

## Porque importa

A incoerência visual não se nota como erro, nota-se como desleixo. Ninguém repara
que há cinco vermelhos, mas o conjunto passa a sensação de coisa montada aos
bocados. Reduzir ao conjunto mínimo também torna qualquer alteração futura
trivial.

## Como saber se correu bem

- Os valores quase iguais estão agrupados com a contagem de ocorrências
- Cada grupo tem um vencedor proposto
- O conjunto mínimo está nomeado e é mesmo mínimo
- As variações intencionais ficaram marcadas e não uniformizadas
- Nada foi alterado
