---
id: CTL-01
nome: Fechar o ciclo: escrever, experimentar, corrigir até passar
categoria: controlo
nivel: essencial
modo: execucao
origem: ccp-4
gatilhos:
  - disseste que estava feito e não está
  - experimenta antes de me dizeres que acabaste
  - quero ver a prova de que funciona
  - não me digas feito sem confirmares
  - corre isso e mostra o resultado
nao_usar_quando:
  - não existe forma de correr nem de verificar o resultado
  - o trabalho é um documento e não código a funcionar
  - a verificação depende de acesso que a ferramenta não tem, e aí diz-se isso
variaveis:
  - nome: forma_de_verificar
    descricao: como se confirma que funciona, correr a aplicação, correr testes, abrir a página
    obrigatoria: false
    omissao: escolher a forma disponível no projeto e dizer qual foi usada
encadeia_com: [CTL-02, TES-01, TES-02]
---

## Prompt

Depois de implementares, não pares aí.

1. Corre {{forma_de_verificar}} e lê o resultado com atenção. Ler é a parte que
   se salta: um comando que termina sem erro não prova que a funcionalidade
   funciona.
2. Se alguma coisa falhar, corrige e repete. Continua o ciclo até funcionar
   mesmo, sem me devolveres o trabalho a meio para eu reportar o erro.
3. Mostra-me a prova: o resultado do comando, os testes a passar, o que aparece
   no ecrã.
4. Só me dizes que está feito depois de teres verificado com os teus próprios
   meios.

Duas exceções em que deves parar e falar comigo em vez de continuares o ciclo:

- A mesma correção falhou duas vezes seguidas. Ao terceiro palpite estás a
  adivinhar, e é altura de diagnosticar em vez de tentar.
- A correção que falta fazer sai do âmbito do que pedi, ou obriga a alterar
  coisas que não estavam em causa.

Se não conseguires verificar por não teres acesso a alguma coisa, diz isso com
todas as letras e diz o que eu tenho de fazer para verificar. Não digas que está
feito quando o que queres dizer é que está escrito.

## Porque importa

Dizer que está feito sem confirmar é o que gera aquelas sessões inteiras a
reportar erros para trás e para a frente. Quando a verificação faz parte do
trabalho, o que chega já passou por ela.

## Como saber se correu bem

- A verificação foi corrida e o resultado foi lido
- A prova está na resposta e não apenas afirmada
- O ciclo repetiu-se até passar, sem me devolver o erro a meio
- Se falhou duas vezes seguidas, parou e passou a diagnóstico
- Se não foi possível verificar, isso foi dito em vez de assumido
