---
id: PLA-07
nome: Cortar o que está complicado a mais
categoria: planeamento
nivel: recomendado
modo: diagnostico
origem: ccp-23
gatilhos:
  - isto parece complicado demais para o que eu quero
  - será que preciso disto tudo
  - o plano ficou enorme
  - revê este plano com olhos críticos
  - simplifica-me isto antes de começarmos
nao_usar_quando:
  - não existe plano nem especificação para rever
  - o projeto já está construído e o que se quer é limpar código, usar PER-08 ou PER-09
  - a complicação vem de um requisito real já verificado, e cortá-la partia o produto
variaveis:
  - nome: documento
    descricao: o plano ou a especificação a rever
    obrigatoria: false
    omissao: usar o último plano ou especificação escrita e dizer qual foi
  - nome: escala_real
    descricao: quantas pessoas vão mesmo usar isto no primeiro mês
    obrigatoria: false
    omissao: assumir escala pequena e declarar a assunção, porque muda tudo
encadeia_com: [PLA-03, PLA-04, PLA-10]
---

## Prompt

Revê {{documento}} como um engenheiro sénior desconfiado, cujo trabalho é
proteger-me de complicar à toa. Só diagnóstico, não reescrevas o ficheiro.

Aponta, com o sítio exato onde aparece:

1. Tudo o que está a ser construído para um futuro que ainda não existe. Assume
   {{escala_real}}, e não a escala que se sonha ter daqui a dois anos.
2. Ferramentas, serviços ou bases de dados que se possam trocar por algo mais
   simples, ou simplesmente eliminar.
3. Funcionalidades que parecem essenciais e que a maioria das pessoas nunca vai
   usar.
4. Problemas que estão a ser resolvidos e que eu ainda não tenho.
5. Camadas criadas para um caso só: uma abstração com uma implementação, uma
   configuração para um valor que nunca muda.

Para cada ponto diz o que ganho e o que perco se simplificar. Se perder alguma
coisa real, diz. Não cortes por cortar.

No fim, mostra-me a versão enxuta em lista, e diz quanto trabalho ela poupa em
relação à original.

Se alguma complicação for mesmo necessária, defende-a em vez de a cortares. Uma
revisão que corta tudo é tão inútil como uma que não corta nada.

## Porque importa

A tendência natural, das pessoas e das ferramentas de IA, é preparar tudo para um
problema muito maior do que aquele que se tem. Isso enche o projeto de peças que
só fazem sentido numa escala que ainda não chegou, e cada peça a mais é mais uma
coisa que parte.

## Como saber se correu bem

- Nenhum ficheiro foi reescrito
- Cada corte aponta para o sítio concreto onde a complicação aparece
- Cada corte diz o que se perde, e não só o que se ganha
- Aquilo que é mesmo preciso ficou defendido e não cortado
- Há uma versão enxuta no fim, em lista
