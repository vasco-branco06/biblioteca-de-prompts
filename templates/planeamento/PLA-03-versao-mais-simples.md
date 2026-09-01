---
id: PLA-03
nome: A versão mais simples que já vale a pena
categoria: planeamento
nivel: recomendado
modo: diagnostico
origem: ccp-19
gatilhos:
  - tenho uma ideia mas não sei por onde começar
  - quero lançar isto depressa
  - isto está a ficar grande demais
  - o que é que preciso mesmo para a primeira versão
  - quero uma coisa simples para começar
nao_usar_quando:
  - o âmbito já está fechado e o que falta é ordenar as fases, usar PLA-04
  - existe um plano escrito que precisa de ser cortado, usar PLA-07
  - a primeira versão já está no ar e o pedido é acrescentar coisas
variaveis:
  - nome: ideia
    descricao: o que se quer construir
    obrigatoria: true
    omissao: perguntar, sem isto não há corte possível
  - nome: utilizador_alvo
    descricao: quem vai usar a primeira versão e para resolver o quê
    obrigatoria: false
    omissao: inferir da ideia e declarar a assunção numa linha
  - nome: prazo
    descricao: quando é que isto tem de estar no ar
    obrigatoria: false
    omissao: não assumir prazo, e dizer que o corte muda se houver um
encadeia_com: [PLA-02, PLA-04, PLA-07]
---

## Prompt

Quero {{ideia}}, para {{utilizador_alvo}}. Ajuda-me a decidir a versão mais
pequena que já resolve alguma coisa a essa pessoa.

Devolve duas listas separadas:

**Entra na primeira versão.** Só o que, faltando, faz a coisa deixar de servir
para nada. Para cada item, uma linha a dizer que problema resolve a quem a usa.

**Fica para depois.** Tudo o resto, com a razão de ficar de fora e o sinal que me
dirá que chegou a altura de o construir.

Aplica a cada candidato esta pergunta antes de o deixares entrar: se isto não
existisse, {{utilizador_alvo}} deixava de usar? Se a resposta for não, vai para a
segunda lista.

Marca à parte as coisas que parecem funcionalidades mas são na verdade decisões
de infraestrutura, como contas de utilizador, pagamentos ou notificações. São as
que mais custam e as que mais vezes entram sem serem precisas no primeiro dia.

Considera {{prazo}} se houver.

Não me proponhas uma versão simples que não faça nada de ponta a ponta. Pequena
não é incompleta.

## Porque importa

Quase todos os projetos que não chegam ao fim morrem por excesso de âmbito, não
por falta de capacidade. Decidir o que fica de fora é o trabalho, e é o que se
salta com mais facilidade porque cortar dá menos gozo do que acrescentar.

## Como saber se correu bem

- As duas listas existem e a segunda é maior do que a primeira
- Cada item que entra está justificado pelo problema que resolve a alguém
- Cada item que sai tem o sinal que dirá quando o retomar
- A primeira versão continua a funcionar de ponta a ponta
- As decisões caras aparecem sinalizadas como tal
