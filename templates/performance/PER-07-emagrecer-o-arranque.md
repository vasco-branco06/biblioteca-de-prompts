---
id: PER-07
nome: Emagrecer o que carrega no arranque
categoria: performance
nivel: situacional
modo: diagnostico
origem: ccp-67
gatilhos:
  - a primeira visita demora imenso
  - no telemóvel com dados móveis é insuportável
  - o site é pesado a abrir
  - descarrega muita coisa antes de aparecer
  - quero reduzir o tamanho do site
nao_usar_quando:
  - o site é pequeno e usa poucas bibliotecas
  - a lentidão está no servidor, usar PER-06
  - o problema são as imagens, usar PER-02
variaveis:
  - nome: pagina
    descricao: a página a analisar
    obrigatoria: false
    omissao: analisar a página de entrada, que é a que apanha as primeiras visitas
encadeia_com: [PER-02, PER-11, PER-03]
---

## Prompt

Só diagnóstico. Diz-me o que mais pesa naquilo que o visitante descarrega ao
abrir {{pagina}}.

Dá-me primeiro o total e o número de pedidos, para eu ter noção da escala. Se não
conseguires medir, diz que estás a estimar.

Depois lista as bibliotecas por peso, das mais pesadas para as mais leves. Para
as três maiores, responde:

1. Para que servem neste projeto, em concreto, e onde são usadas.
2. Se há alternativa mais leve, ou se o navegador já faz isso sem biblioteca
   nenhuma. Muita coisa que se instala hoje já existe de origem.
3. Se podem ser carregadas só quando são precisas, em vez de logo no início.

Concentra-te no que a maioria das pessoas nunca chega a abrir: editores, gráficos,
mapas, animações, painéis de administração. Isso é peso que quase toda a gente
descarrega e quase ninguém usa.

Diz também o que bloqueia a página até estar carregado, porque isso pesa mais do
que o tamanho sugere.

Dá-me a lista com o ganho estimado em cada caso. Não mudes nada.

## Porque importa

Tudo o que a página precisa de enviar tem de chegar ao telemóvel de quem entra,
muitas vezes com ligação fraca. O primeiro carregamento é o único que não tem
ajuda de nada guardado antes, e é precisamente o momento em que a pessoa decide
se fica.

## Como saber se correu bem

- Há um total e um número de pedidos, medidos ou assumidos como estimativa
- As três maiores estão explicadas quanto ao seu uso real
- Foi verificado se o navegador já faz aquilo de origem
- Está identificado o que bloqueia a página
- Nada foi alterado
