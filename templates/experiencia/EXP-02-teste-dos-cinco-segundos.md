---
id: EXP-02
nome: O teste dos cinco segundos e a hierarquia visual
categoria: experiencia
nivel: recomendado
modo: diagnostico
origem: ccp-32
gatilhos:
  - percebe-se logo o que isto é
  - a página parece confusa
  - não sei se as pessoas percebem para onde olhar
  - está tudo com o mesmo peso
  - qual é a primeira impressão que isto dá
nao_usar_quando:
  - o objetivo é a análise completa de conversão, usar EXP-01
  - a página ainda não tem conteúdo real, só espaços reservados
  - a preocupação é a coerência visual do projeto todo, usar EXP-09
variaveis:
  - nome: pagina
    descricao: a página a avaliar
    obrigatoria: false
    omissao: usar a página de entrada e dizer qual foi
encadeia_com: [EXP-01, EXP-06, EXP-09]
---

## Prompt

Só diagnóstico.

Comporta-te como alguém que chega a {{pagina}} pela primeira vez e só a vê
durante cinco segundos. Não olhes primeiro para o código, porque isso estraga a
experiência que quero medir.

Descreve, por ordem, o que os teus olhos captam de cima para baixo. Só o que se
capta, não o que se lê com atenção.

Depois responde:

1. Em cinco segundos percebe-se o que isto é, para quem é, e o que devo fazer a
   seguir. Responde às três em separado, porque falham em separado.
2. Qual é o elemento com mais peso visual, e é esse que devia dominar.
3. Onde é que a hierarquia falha: dois elementos a competir pela atenção, o botão
   de ação a perder-se, texto todo do mesmo tamanho, imagens que puxam o olhar
   para longe do que interessa.

Para cada falha, dá a correção concreta: que tamanho, que cor, quanto espaço, que
posição. Não escrevas dar mais destaque; escreve o que muda e para quanto.

Ordena por impacto.

Só depois de responderes a tudo isto é que podes olhar para o código, e só se for
preciso para dizer onde se muda cada coisa.

## Porque importa

Ninguém lê uma página, olha-se para ela. A decisão de ficar ou sair é tomada
antes de qualquer leitura, com base no que salta à vista. Se o que salta à vista
não for o que interessa, o resto do conteúdo não chega a ser lido.

## Como saber se correu bem

- A descrição do que se capta veio antes de qualquer análise de código
- As três perguntas dos cinco segundos foram respondidas em separado
- Foi identificado o elemento dominante e se devia ser esse
- Cada correção tem valores concretos e não conselhos vagos
- Nada foi alterado
