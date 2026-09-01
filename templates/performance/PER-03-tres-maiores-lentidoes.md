---
id: PER-03
nome: As três maiores lentidões
categoria: performance
nivel: recomendado
modo: diagnostico
origem: ccp-39
gatilhos:
  - o site está lento
  - isto demora imenso a abrir
  - porque é que isto é tão lento
  - as pessoas queixam-se da lentidão
  - preciso de acelerar isto
nao_usar_quando:
  - já se sabe qual é a causa e o que falta é corrigi-la
  - o problema é a sensação e não o tempo real, usar EXP-10
  - a lentidão só aparece com muitos dados e ainda não foi medida, usar TES-06
variaveis:
  - nome: alvo
    descricao: a página, ecrã ou operação lenta
    obrigatoria: false
    omissao: usar o percurso principal e dizer qual foi medido
encadeia_com: [PER-06, PER-07, PER-02, EXP-10]
---

## Prompt

Só diagnóstico. {{alvo}} está lento. Encontra os três pontos que mais o atrasam.

Mede antes de opinar. Se não conseguires medir, diz que estás a estimar e com que
base, em vez de apresentares um palpite com ar de facto.

Separa o tempo em três sítios, porque as correções são diferentes:

1. O que acontece no servidor antes de responder: consultas à base de dados,
   chamadas a outros serviços, cálculos.
2. O que é preciso descarregar: tamanho total, quantos pedidos, o que bloqueia a
   página até chegar.
3. O que acontece no navegador depois de chegar: trabalho pesado, listas grandes
   desenhadas de uma vez, animações.

Para cada um dos três maiores atrasos:

- explica em linguagem simples o que se está a passar
- diz quanto tempo custa, ou a ordem de grandeza
- propõe a correção mais fácil, e diz quanto tempo poupa
- diz se existe uma correção mais completa e mais cara, para eu escolher

Ordena por tempo poupado a dividir pelo esforço, e não pelo tempo poupado
sozinho.

Não corrijas nada. Se a causa for uma das que tem template próprio, consultas
repetidas ou peso do arranque, diz qual e para em vez de a resolveres aqui.

## Porque importa

Sem medir, mexe-se no sítio errado e o site continua lento, agora com mais código
lá dentro. Saber onde está o tempo transforma uma queixa vaga numa lista curta de
correções com ganho conhecido.

## Como saber se correu bem

- Ficou claro o que foi medido e o que foi estimado
- O tempo está separado entre servidor, transferência e navegador
- Cada correção vem com ganho estimado
- A ordem segue ganho a dividir por esforço
- Nada foi corrigido
