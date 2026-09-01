---
id: EXP-08
nome: Reescrever os textos da interface e as mensagens de erro
categoria: experiencia
nivel: situacional
modo: diagnostico
origem: ccp-63
gatilhos:
  - as mensagens de erro são horríveis
  - aparece erro 400 ao utilizador
  - os textos soam a robô
  - ninguém percebe o que fazer quando falha
  - os botões dizem todos enviar
nao_usar_quando:
  - o problema é faltarem estados e não os textos deles, usar EXP-03
  - o texto a rever é de marketing e não de interface, usar MKT-07
  - a interface ainda não tem textos definitivos
variaveis:
  - nome: alvo
    descricao: que ecrãs ou componentes rever
    obrigatoria: false
    omissao: rever todos os textos de interface do projeto
  - nome: tom
    descricao: como a marca fala com quem a usa
    obrigatoria: false
    omissao: próximo mas profissional, sem gracinhas em mensagens de erro
encadeia_com: [EXP-03, EXP-04, MKT-07]
---

## Prompt

Só diagnóstico, entrega em tabela, não alteres ficheiros.

Lista todas as frases de {{alvo}} que falam com quem usa: mensagens de erro,
botões, etiquetas, textos de exemplo dentro dos campos, dicas, confirmações,
ecrãs vazios, notificações, títulos de janelas.

Para cada uma avalia três coisas:

1. Soa a pessoa ou a máquina.
2. Diz o que aconteceu e o que fazer a seguir. Faltar a segunda parte é o defeito
   mais comum.
3. Evita jargão técnico e evita culpar quem está a usar.

Reescreve as que falham, em português europeu, com {{tom}}.

Nas mensagens de erro, presta atenção especial a três casos:

- Códigos e mensagens técnicas mostradas em bruto. Traduz para o que aconteceu e
  o que fazer.
- Mensagens que culpam quem usa, do género introduziu dados inválidos.
- Mensagens que revelam informação a mais sobre o sistema por dentro. Se
  encontrares alguma, marca-a também como problema de segurança.

Entrega: texto atual | onde está | problema | versão reescrita.

Mantém a mesma ordem de grandeza de comprimento, porque a interface tem espaço
limitado. Se uma reescrita não couber, di-lo.

## Porque importa

Estes textos são escritos à pressa, no meio de outra coisa, e depois ficam anos.
São a única voz do produto quando alguma coisa corre mal, e é exatamente aí que
a pessoa decide se pede ajuda, se tenta outra vez, ou se desiste.

## Como saber se correu bem

- A lista cobre todos os tipos de texto, incluindo ecrãs vazios e confirmações
- Cada reescrita diz o que aconteceu e o que fazer a seguir
- Nenhuma culpa quem está a usar
- As que revelam informação interna estão marcadas como risco
- Nada foi alterado nos ficheiros
