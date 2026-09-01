---
id: TES-04
nome: Testar os casos estranhos, não só o caminho feliz
categoria: testes
nivel: situacional
modo: execucao
origem: ccp-73
gatilhos:
  - só testei com dados bonitos
  - e se alguém deixar o campo vazio
  - as pessoas escrevem coisas que eu não esperava
  - isto parte com acentos
  - quero testar os casos limite
nao_usar_quando:
  - ainda não existe teste nenhum do percurso principal, usar TES-02 primeiro
  - a preocupação é a segurança do que entra e não a robustez, usar SEG-05
  - a preocupação é o volume de dados, usar TES-06
variaveis:
  - nome: funcionalidade
    descricao: o que testar
    obrigatoria: true
    omissao: perguntar
  - nome: ferramenta_testes
    descricao: com que ferramenta se escrevem os testes
    obrigatoria: false
    omissao: usar a que o projeto já tem
encadeia_com: [TES-02, TES-06, SEG-05]
---

## Prompt

Para {{funcionalidade}}, escreve testes com {{ferramenta_testes}} que cubram o
caso fácil e, sobretudo, os estranhos. É nos estranhos que estão os defeitos.

Antes de escreveres, lista os casos que vais cobrir e confirma comigo. Percorre
estas famílias e diz quais se aplicam:

1. **Vazio e ausente.** Campo vazio, campo com espaços, campo não enviado. São
   três coisas diferentes e falham de maneiras diferentes.
2. **Limites.** Zero, um, o máximo permitido, o máximo mais um, números negativos
   onde só fazem sentido positivos.
3. **Tipo errado.** Texto onde devia ser número, número onde devia ser texto,
   data impossível.
4. **Tamanho.** Texto muito longo, ficheiro muito grande, lista muito comprida.
5. **Caracteres.** Acentos, cedilhas, emojis, aspas, sinais que têm significado
   em bases de dados ou em endereços.
6. **Tempo e ordem.** Duas ações ao mesmo tempo, ação repetida, ação fora de
   ordem, sessão expirada a meio.

Para cada teste, define o que deve acontecer. Muitas vezes a resposta certa é
recusar com uma mensagem clara, e não aceitar. Se não souberes qual é o
comportamento correto de um caso, pergunta em vez de decidires.

No fim corre os testes e mostra o resultado. Se algum falhar, isso é um defeito
encontrado, não um teste mal escrito. Mostra-mo antes de corrigires.

## Porque importa

O caminho em que corre tudo bem é o único que se testa enquanto se constrói,
porque é o que se está a construir. As pessoas reais deixam campos vazios, colam
textos enormes e escrevem acentos, e é aí que a aplicação parte.

## Como saber se correu bem

- A lista de casos foi apresentada e confirmada antes de escrever
- As seis famílias foram consideradas, com justificação para as que não se aplicam
- Vazio, espaços e ausente foram tratados como casos distintos
- O comportamento esperado está definido em cada teste
- Os testes que falharam foram mostrados como defeitos, não corrigidos em silêncio
