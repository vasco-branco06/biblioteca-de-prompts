---
id: TES-05
nome: Primeiro um teste que falha, só depois a correção
categoria: testes
nivel: situacional
modo: execucao
origem: ccp-74
gatilhos:
  - este erro já apareceu duas vezes
  - corrigimos isto e voltou
  - quero garantir que este problema não volta
  - encontrei um defeito
  - isto tem de ficar resolvido de vez
nao_usar_quando:
  - o defeito não é reproduzível, usar DIA-06 primeiro
  - a causa ainda não é conhecida, usar DIA-05 primeiro
  - é uma alteração de aspeto sem comportamento a proteger
variaveis:
  - nome: defeito
    descricao: o que está mal, e os passos para o fazer acontecer
    obrigatoria: true
    omissao: perguntar, incluindo os passos exatos
  - nome: ferramenta_testes
    descricao: com que ferramenta se escrevem os testes
    obrigatoria: false
    omissao: usar a que o projeto já tem
encadeia_com: [DIA-05, TES-02, TES-04]
---

## Prompt

Sobre {{defeito}}: não corrijas ainda.

**Passo 1.** Escreve com {{ferramenta_testes}} um teste automático que reproduza
este defeito exatamente. O teste descreve o comportamento correto, aquele que
devia acontecer.

**Passo 2.** Corre esse teste e mostra-me que ele falha agora. Se passar, o teste
está errado: reescreve-o até falhar, e falhar pela razão certa. Um teste que
falha por outro motivo qualquer não protege nada.

**Passo 3.** Só depois corrige o código, o mínimo necessário para o teste passar.
Não aproveites para arrumar mais nada pelo caminho.

**Passo 4.** Corre o teste outra vez e mostra-me que passa. Corre também os
restantes testes do projeto e mostra-me que continuam a passar.

O teste fica no projeto para sempre. É o que impede o defeito de voltar sem
ninguém dar por isso.

Nunca alteres nem apagues o teste para o fazer passar. Se ele estiver a falhar
depois da correção, é a correção que está incompleta.

## Porque importa

Ver o teste falhar antes de corrigir é a única prova de que ele está mesmo a
verificar aquilo. Um teste escrito depois da correção passa desde o primeiro dia
e ninguém sabe se alguma vez apanharia o problema. Assim, o defeito fica com um
guarda permanente.

## Como saber se correu bem

- O teste foi escrito antes de qualquer correção
- Foi mostrado a falhar, e a falhar pela razão certa
- A correção foi mínima e não trouxe arrumações extra
- O teste passa no fim e os restantes continuam a passar
- O teste ficou guardado e não foi alterado para passar
