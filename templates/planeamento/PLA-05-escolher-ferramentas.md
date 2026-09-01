---
id: PLA-05
nome: Escolher ferramentas simples, com a razão de cada uma
categoria: planeamento
nivel: recomendado
modo: diagnostico
origem: ccp-21
gatilhos:
  - com que ferramentas é que faço isto
  - não sei o que escolher
  - qual é a forma mais fácil de construir isto
  - preciso de uma base de dados mas não sei qual
  - o que é que uso para pôr isto no ar
nao_usar_quando:
  - o projeto já existe e tem ferramentas escolhidas, e trocar custa mais do que ganha
  - o que se quer saber é quanto custa e não o que usar, usar PLA-08
  - a escolha já está feita e o que falta é montar
variaveis:
  - nome: objetivo
    descricao: o que se quer construir, em uma frase
    obrigatoria: true
    omissao: perguntar
  - nome: experiencia
    descricao: com o que a pessoa já mexeu antes
    obrigatoria: false
    omissao: assumir que nunca programou e dizê-lo
  - nome: obrigacoes
    descricao: ferramentas que já estão decididas e não se discutem
    obrigatoria: false
    omissao: assumir que não há nenhuma
encadeia_com: [PLA-08, PLA-09, PLA-02]
---

## Prompt

Para {{objetivo}}, recomenda as ferramentas mais simples de usar por quem tem
{{experiencia}}. Respeita {{obrigacoes}}, que não estão em discussão.

Para cada peça que o projeto precisa, dá uma recomendação e escreve:

- Para que serve, em linguagem simples.
- Porque escolheste esta e não outra, em uma frase.
- Se tem plano grátis e até onde vai esse plano.
- O que fica difícil se um dia eu quiser mudar de ferramenta.

Recomenda uma por peça, não me dês três para eu escolher. Se houver mesmo um
empate, diz que há empate e o que o desempata.

Regras de escolha, por esta ordem:

1. Menos peças é melhor do que mais peças. Se duas necessidades se resolvem com
   uma ferramenta só, resolve com uma.
2. Aborrecido e muito usado ganha a novo e brilhante. Documentação farta e
   respostas já escritas valem mais do que funcionalidades.
3. Nada que eu não consiga perceber ao fim de uma tarde.

No fim, diz-me qual destas escolhas é a mais difícil de reverter mais tarde. É
essa que vale a pena pensar duas vezes.

Não recomendes nada por teres ouvido falar bem. Se não tiveres a certeza de que
uma ferramenta continua ativa e mantida, diz que é preciso confirmar em vez de
afirmares.

## Porque importa

Quem está a começar não tem como saber qual das centenas de opções é a certa, e a
escolha errada só aparece semanas depois, sob a forma de trabalho que não avança.
Uma recomendação com a razão explicada deixa decidir sem perceber dos detalhes.

## Como saber se correu bem

- Há uma recomendação por peça, e não uma lista de opções para eu escolher
- Cada uma vem com a razão em uma frase
- O plano grátis e o seu limite estão ditos
- A escolha mais difícil de reverter está assinalada
- Nada foi recomendado sem justificação nem afirmado sem certeza
