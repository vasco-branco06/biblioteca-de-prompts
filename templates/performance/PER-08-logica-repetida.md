---
id: PER-08
nome: A mesma lógica repetida em vários sítios
categoria: performance
nivel: situacional
modo: diagnostico
origem: ccp-68
gatilhos:
  - ando sempre a corrigir a mesma coisa em vários sítios
  - isto está copiado em três sítios
  - mudei num sítio e esqueci-me do outro
  - há muito código repetido aqui
  - dá para juntar isto tudo
nao_usar_quando:
  - o projeto é pequeno e a repetição ainda não custou nada
  - os blocos parecidos servem regras de negócio diferentes
  - o objetivo é dividir um ficheiro grande, usar PER-09
variaveis:
  - nome: alvo
    descricao: onde procurar
    obrigatoria: false
    omissao: procurar no projeto inteiro
  - nome: limite
    descricao: a partir de quantas repetições vale a pena juntar
    obrigatoria: false
    omissao: três ocorrências, abaixo disso a duplicação sai mais barata
encadeia_com: [PER-10, PER-01, PER-09]
---

## Prompt

Só diagnóstico. Procura em {{alvo}} blocos que fazem essencialmente a mesma coisa
em {{limite}} ou mais sítios: validações repetidas, formatação de datas ou de
dinheiro, chamadas parecidas a serviços, tratamento de erros, transformações de
dados.

Para cada caso, lista os sítios e propõe onde ficaria a versão única.

A regra que manda aqui, e que é mais importante do que encontrar repetições: só
propõe juntar se o comportamento for genuinamente idêntico. Se dois blocos são
parecidos mas servem regras diferentes, deixa-os separados e explica-me porquê.

Aplica este teste a cada candidato: se amanhã um dos sítios tiver de mudar e o
outro não, juntá-los teria criado um problema. Se a resposta for sim, não juntes.

Separa a lista em duas partes:

- **Juntar.** Comportamento idêntico, muda sempre ao mesmo tempo, mesma razão de
  existir.
- **Deixar como está.** Parecido à superfície, com razões diferentes por baixo,
  com a explicação da diferença.

Não alteres nada. Mostra-me as duas listas para eu escolher.

## Porque importa

Quando a mesma lógica está copiada, uma correção obriga a mudar em todos os
sítios, e esquece-se sempre um. Mas juntar coisas que só parecem iguais é pior:
cria um sítio único que tem de servir dois donos com necessidades diferentes, e
esse sítio vai encher-se de exceções.

## Como saber se correu bem

- Nada foi alterado
- Cada repetição aparece com todos os sítios onde ocorre
- Existe a lista do que não se deve juntar, com a razão
- Foi aplicado o teste de mudarem em alturas diferentes
- A decisão final ficou para mim
