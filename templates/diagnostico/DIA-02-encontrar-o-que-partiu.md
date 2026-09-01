---
id: DIA-02
nome: Encontrar a alteração que partiu isto
categoria: diagnostico
nivel: recomendado
modo: diagnostico
origem: ccp-11
gatilhos:
  - isto ontem funcionava e hoje não
  - deixou de funcionar e não sei o que mudou
  - o que é que estragou isto
  - estava tudo bem até há pouco
  - alguma coisa que mexemos partiu outra coisa
nao_usar_quando:
  - isto nunca funcionou, e então não há nada que tenha partido
  - o problema só acontece no site publicado e não no computador, usar DIA-03
  - a falha é intermitente e não se consegue repetir, usar DIA-06
  - o projeto não tem histórico de alterações guardado
variaveis:
  - nome: funcionalidade
    descricao: o que funcionava e deixou de funcionar
    obrigatoria: false
    omissao: perguntar, porque sem isto a procura no histórico não tem alvo
  - nome: momento
    descricao: quando é que ainda funcionava, mesmo que seja aproximado
    obrigatoria: false
    omissao: perguntar, e na falta de resposta olhar para as alterações do último dia
encadeia_com: [DIA-01, DIA-04, DIA-05, TES-05]
---

## Prompt

Só diagnóstico. Não corrijas nada.

{{funcionalidade}} funcionava e deixou de funcionar. Vamos encontrar a alteração
responsável, não adivinhar a causa.

1. Confirma comigo o que funcionava, o que acontece agora em vez disso, e desde
   {{momento}}. Se alguma destas três coisas não estiver clara, pergunta antes de
   avançar.
2. Percorre o histórico de alterações desde esse momento. Lista as que tocam,
   direta ou indiretamente, na funcionalidade partida. Ignora as que não têm
   qualquer relação e diz quantas ignoraste.
3. Ordena as suspeitas, da mais provável para a menos, e explica em uma linha
   porque cada uma é suspeita.
4. Mostra-me a alteração mais suspeita, o que mudou nela, e o que isso passou a
   fazer de diferente.

Se o histórico não bastar para decidir, diz quais são as duas ou três alterações
empatadas e o que eu posso experimentar para desempatar.

Não presumas que a alteração mais recente é a culpada. Muitas vezes o problema
foi introduzido antes e só ficou visível agora.

## Porque importa

Procurar às cegas num projeto inteiro pode demorar horas. O histórico reduz a
procura ao que mudou desde o momento em que ainda estava bom, e isso costuma ser
uma lista curta.

## Como saber se correu bem

- Nada foi corrigido nem alterado
- As três perguntas de enquadramento foram confirmadas antes da procura
- As suspeitas vêm ordenadas e justificadas
- A alteração suspeita foi mostrada e explicada
- Se houve empate, ficou dito como desempatar
