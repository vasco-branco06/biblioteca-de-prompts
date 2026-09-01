---
id: CTL-03
nome: Guardar o trabalho em segurança
categoria: controlo
nivel: essencial
modo: execucao
origem: ccp-7
gatilhos:
  - guarda o que já está feito
  - não quero perder isto
  - antes de continuarmos guarda tudo
  - faz um ponto de retorno
  - vamos parar por hoje
nao_usar_quando:
  - o projeto não tem controlo de versões e criá-lo é outra decisão
  - o que se quer é desfazer e não guardar, usar DIA-04
variaveis:
  - nome: alvo
    descricao: o que guardar
    obrigatoria: false
    omissao: guardar tudo o que está por guardar, agrupado por assunto
encadeia_com: [DIA-04, SEG-01, DIA-07]
---

## Prompt

Antes de continuarmos, garante que não perco nada de {{alvo}}.

1. **Mostra o que está por guardar.** Ficheiro a ficheiro, com uma linha a dizer
   o que mudou em cada um. Se houver muitos, agrupa por assunto.
2. **Procura segredos.** Antes de guardar seja o que for, verifica se algum
   ficheiro tem palavras-passe, chaves ou dados pessoais. Se tiver, avisa-me,
   não o guardes, e diz-me o que fazer com ele. Isto vem antes de tudo o resto,
   porque depois de guardado fica no histórico para sempre.
3. **Guarda em grupos com sentido.** Um ponto de retorno por assunto, com uma
   mensagem clara em português a dizer o que mudou e porquê. Não guardes tudo num
   monte só com uma mensagem genérica: assim o histórico não serve para recuar
   nem para perceber nada.
4. **Confirma.** Mostra que ficou tudo guardado e o que ficou deliberadamente de
   fora.

Se alguma coisa não devia estar sob controlo de versões, como ficheiros gerados
ou pastas de dependências, diz-me antes de as guardares.

Não envies nada para servidores remotos sem eu pedir. Guardar localmente e
publicar são coisas diferentes.

## Porque importa

Guardar é criar pontos para onde se pode voltar. Sem eles, uma tentativa que corre
mal leva atrás o trabalho de uma tarde inteira. E o momento de guardar é o único
em que ainda dá para impedir que um segredo entre no histórico, porque depois já
não sai.

## Como saber se correu bem

- A lista do que está por guardar foi mostrada primeiro
- A procura de segredos aconteceu antes de guardar
- Os pontos de retorno estão agrupados por assunto, com mensagens claras
- Ficou dito o que não foi guardado e porquê
- Nada foi enviado para fora do computador sem eu pedir
