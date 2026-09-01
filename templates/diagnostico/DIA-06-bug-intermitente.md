---
id: DIA-06
nome: Apanhar o erro que só acontece às vezes
categoria: diagnostico
nivel: situacional
modo: diagnostico
origem: ccp-48
gatilhos:
  - às vezes acontece e às vezes não
  - não consigo repetir o erro
  - só acontece de vez em quando
  - quando quero mostrar a alguém funciona sempre
  - já aconteceu duas ou três vezes mas nunca quando quero
nao_usar_quando:
  - o erro acontece sempre, e então é DIA-05
  - o erro tem hora marcada e causa conhecida
  - já se sabe o que o desencadeia e falta corrigir
variaveis:
  - nome: problema
    descricao: o que acontece quando acontece
    obrigatoria: true
    omissao: perguntar
  - nome: circunstancias
    descricao: o que estava a acontecer nas vezes em que apareceu
    obrigatoria: false
    omissao: perguntar as três últimas vezes e o que tinham em comum
encadeia_com: [DIA-05, TES-05, TES-03]
---

## Prompt

Só diagnóstico. {{problema}} acontece de forma intermitente e não se consegue
repetir de propósito. Não proponhas correção nenhuma enquanto não o soubermos
repetir.

1. Pergunta-me pelas últimas vezes em que aconteceu, uma de cada vez, à procura
   do que {{circunstancias}} têm em comum: hora do dia, primeira ação depois de
   abrir, ligação lenta, muitos dados, duas janelas abertas, sessão antiga.
2. Lista as causas típicas de erros intermitentes e diz quais são compatíveis com
   o que descrevi:
   - ordem ou tempo das operações, quando duas coisas correm ao mesmo tempo
   - dados guardados em memória ou em cache que ficaram desatualizados
   - sessão ou credencial que expira
   - dependência de rede que às vezes responde depressa e às vezes não
   - estado que sobra de uma utilização anterior
3. Diz-me que registos temporários pôr, com marca de hora, para eu capturar o
   estado exato quando voltar a acontecer. Se estes só puderem ser colocados
   alterando ficheiros, pede-me autorização antes.
4. Explica-me como forçar as condições de propósito: simular ligação lenta,
   repetir a ação muitas vezes seguidas, abrir duas janelas, esperar que a sessão
   expire.

Só passamos à correção depois de conseguirmos fazer o erro aparecer quando
queremos. Enquanto isso não acontecer, qualquer correção é um palpite disfarçado.

## Porque importa

Um erro que não se consegue repetir também não se consegue confirmar como
resolvido. Quem corrige à sorte fica sem saber se o problema foi embora ou se
apenas não voltou ainda. Conseguir provocá-lo é metade do trabalho.

## Como saber se correu bem

- As perguntas sobre as ocorrências vieram uma de cada vez
- As causas típicas foram filtradas pelas que batem com o descrito
- Existe uma receita concreta para tentar provocar o erro
- Nenhuma correção foi proposta antes de o erro ser reproduzível
- Se foi preciso alterar ficheiros para registar, foi pedida autorização
