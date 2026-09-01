---
id: DIA-03
nome: Funciona no meu computador mas não no site publicado
categoria: diagnostico
nivel: recomendado
modo: diagnostico
origem: ccp-12
gatilhos:
  - aqui funciona mas no site dá erro
  - depois de publicar deixou de funcionar
  - o site publicado está em branco
  - no meu computador está tudo bem
  - só dá erro na versão que está no ar
nao_usar_quando:
  - o erro também acontece no computador, e então é DIA-02 ou DIA-05
  - o site nunca chegou a ser publicado
  - o problema é lentidão e não erro, usar PER-03
variaveis:
  - nome: erro
    descricao: a mensagem ou o comportamento exato no site publicado
    obrigatoria: false
    omissao: perguntar, e pedir a mensagem tal como aparece, sem resumir
  - nome: onde_publicado
    descricao: o serviço onde o site está no ar
    obrigatoria: false
    omissao: detetar pela configuração do projeto e dizer o que foi encontrado
encadeia_com: [DIA-01, SEG-01, TES-01]
---

## Prompt

Só diagnóstico, não alteres nem publiques nada.

O projeto funciona no meu computador e dá {{erro}} em {{onde_publicado}}. Antes
de mudares seja o que for, encontra a diferença entre os dois sítios.

Pergunta-me primeiro a mensagem de erro exata, tal como aparece, e onde a vejo:
no ecrã, na consola do navegador, ou nos registos do serviço. Um erro resumido
por mim não serve.

Depois percorre as diferenças que explicam quase todos estes casos:

1. Variáveis de configuração que existem no computador e não no serviço, ou que
   lá estão com outro valor. Compara as duas listas, nome a nome, sem mostrar
   valores secretos.
2. Coisas que só existem localmente: ficheiros não enviados, dependências
   instaladas à mão, pastas ignoradas pelo controlo de versões.
3. Diferenças de ambiente: versão da linguagem, sistema de ficheiros que
   distingue maiúsculas de minúsculas, fuso horário.
4. Passos que correm ao publicar e não correm localmente, ou o contrário.
5. Endereços fixos apontados ao computador local em vez do endereço público.

Aponta a causa mais provável e como a confirmar antes de tentar a correção.

## Porque importa

Este é o problema mais comum de todos, e quase nunca é o código. É uma diferença
de configuração entre dois sítios que se assumiu serem iguais. Procurar a
diferença, em vez de mexer no código, resolve na primeira tentativa.

## Como saber se correu bem

- A mensagem de erro exata foi pedida antes de qualquer hipótese
- As duas listas de configuração foram comparadas nome a nome
- Nenhum valor secreto foi mostrado nem escrito
- A causa mais provável veio com forma de a confirmar
- Nada foi alterado nem publicado
