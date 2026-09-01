---
id: PER-02
nome: Imagens, prioridade e o salto do conteúdo
categoria: performance
nivel: recomendado
modo: diagnostico
origem: ccp-38
gatilhos:
  - o conteúdo salta enquanto carrega
  - a imagem grande do topo demora imenso
  - as imagens são muito pesadas
  - cliquei e ele mudou de sítio
  - o Google diz que a minha página é instável
nao_usar_quando:
  - o site praticamente não tem imagens
  - a lentidão vem do servidor e não do que se descarrega, usar PER-06
variaveis:
  - nome: paginas
    descricao: que páginas auditar
    obrigatoria: false
    omissao: auditar todas as páginas públicas
encadeia_com: [PER-07, EXP-10, PER-03]
---

## Prompt

Só diagnóstico. Audita as imagens de {{paginas}} para os três problemas que mais
estragam a experiência.

1. **A imagem grande do topo.** Em cada página, a imagem principal deve carregar
   com prioridade e nunca em carregamento adiado. Adiar a imagem que se vê
   primeiro faz dela a última a aparecer, que é exatamente o contrário do que se
   quer. Diz-me em que páginas isto está trocado.
2. **Dimensões declaradas.** Todas as outras imagens devem ter largura e altura
   definidas, para o navegador reservar o espaço e o conteúdo não saltar quando
   elas chegam. Lista as que não têm, e diz quanto salta a página em cada caso.
3. **Peso.** Imagens muito maiores do que o espaço onde aparecem, e imagens em
   formatos pesados que podiam ser mais leves. Diz o tamanho atual, o tamanho
   necessário, e quanto se pouparia.

Devolve os casos por página, com a correção de cada um e o ganho estimado.

Confirma comigo antes de alterar qualquer ficheiro. Se as correções envolverem
converter ou redimensionar ficheiros originais, avisa que os originais devem ser
guardados.

## Porque importa

O conteúdo a saltar enquanto a página carrega faz clicar no sítio errado, o que
é irritante e às vezes caro. E a imagem do topo é a primeira coisa que a pessoa
espera ver: se for a última a chegar, a página parece lenta mesmo carregando
depressa.

## Como saber se correu bem

- Ficou identificada a imagem principal de cada página e a sua prioridade
- As imagens sem dimensões declaradas estão listadas
- Cada caso de peso excessivo tem tamanho atual, necessário e poupança
- Nada foi alterado sem confirmação
- Ficou dito o que fazer aos ficheiros originais
