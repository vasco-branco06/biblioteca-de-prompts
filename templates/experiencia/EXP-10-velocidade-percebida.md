---
id: EXP-10
nome: Velocidade sentida, e não apenas a medida
categoria: experiencia
nivel: situacional
modo: diagnostico
origem: ccp-65
gatilhos:
  - parece lento mas os testes dizem que está rápido
  - fica um bocado em branco antes de aparecer
  - as coisas saltam de sítio enquanto carrega
  - clico e parece que não aconteceu nada
  - dá a sensação de que está sempre à espera
nao_usar_quando:
  - o problema é lentidão real medida no servidor, usar PER-03 ou PER-06
  - o site ainda não tem conteúdo real
variaveis:
  - nome: pagina
    descricao: a página ou percurso a avaliar
    obrigatoria: false
    omissao: avaliar a página de entrada e o percurso principal
encadeia_com: [PER-03, PER-02, EXP-03]
---

## Prompt

Só diagnóstico. Avalia a velocidade sentida de {{pagina}}, que é diferente da
medida.

1. **Primeiro segundo.** O que a pessoa vê: conteúdo útil, um esqueleto do que
   vai aparecer, ou um ecrã em branco. O ecrã em branco é o pior dos três, mesmo
   que o total demore o mesmo.
2. **Estabilidade.** Há elementos a saltar de sítio quando as imagens e os tipos
   de letra acabam de carregar. Identifica os culpados, um a um. Isto não só
   parece mau como faz clicar no sítio errado.
3. **Imagens.** Estão dimensionadas para o espaço onde aparecem, carregam só
   quando se aproximam do ecrã, e usam formato moderno.
4. **Resposta ao toque.** Um clique dá sinal imediato, abaixo de um décimo de
   segundo, ou parece congelado enquanto o pedido decorre. Se a operação for
   longa, há indicação de progresso.
5. **Ordem de carregamento.** O que aparece primeiro é o que interessa, ou o
   cabeçalho e os avisos de cookies chegam antes do conteúdo.

Lista os problemas por impacto na sensação de rapidez, com a correção concreta de
cada um.

Não alteres nada.

## Porque importa

A pessoa não mede milissegundos, mede a espera. Um site que mostra logo alguma
coisa e responde na hora ao toque parece rápido mesmo que ainda esteja a
carregar; um que fica em branco e depois salta parece lento mesmo com boas notas
nos testes.

## Como saber se correu bem

- Ficou dito o que se vê no primeiro segundo
- Os elementos que provocam saltos estão identificados um a um
- A resposta ao toque foi avaliada separadamente do tempo total
- A ordem de carregamento foi avaliada
- Nada foi alterado
