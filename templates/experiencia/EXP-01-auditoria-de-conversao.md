---
id: EXP-01
nome: Auditoria de conversão de uma página
categoria: experiencia
nivel: recomendado
modo: diagnostico
origem: ccp-31
gatilhos:
  - a minha landing page não converte nada
  - tenho visitas mas ninguém compra
  - as pessoas entram e saem logo
  - porque é que ninguém se regista
  - esta página não está a resultar
nao_usar_quando:
  - a página não tem objetivo de ação, é conteúdo informativo
  - o problema é não haver visitas, e aí a questão está antes da página
  - o pedido é sobre o primeiro impacto visual, usar EXP-02
variaveis:
  - nome: pagina
    descricao: a página a auditar
    obrigatoria: false
    omissao: usar a página principal do projeto e dizer qual foi
  - nome: acao_desejada
    descricao: o que se quer que o visitante faça
    obrigatoria: false
    omissao: inferir da página e declarar a assunção
  - nome: publico
    descricao: quem chega a esta página e de onde vem
    obrigatoria: false
    omissao: inferir do conteúdo e declarar a assunção
encadeia_com: [EXP-02, EXP-04, MKT-05]
---

## Prompt

Só diagnóstico. Audita {{pagina}} secção a secção, com {{acao_desejada}} como
único objetivo.

**Acima da dobra**, aquilo que se vê sem descer na página: percebe-se em cinco
segundos o que isto é e para quem é. Existe um único botão de ação principal, ou
há vários a competir entre si.

**Objeções.** Lista as cinco dúvidas que {{publico}}, desconfiado, teria antes de
agir. Depois diz quais estão respondidas na página e quais não estão. As que não
estão são o trabalho.

**Prova.** Onde está a prova de que isto funciona: números, testemunhos, casos,
garantias. Avalia se é credível ou se é do tipo genérico que qualquer pessoa
podia escrever sobre qualquer coisa.

**Fricção.** Cada passo entre chegar e agir. Conta os cliques, os campos, as
decisões, as coisas que obrigam a sair da página para ir buscar informação.

Entrega uma lista priorizada por impacto estimado, alto, médio ou baixo, e para
cada item a alteração concreta a fazer. Não escrevas conselhos gerais do tipo
melhorar a proposta de valor. Escreve a frase que devia estar lá.

Não alteres a página.

## Porque importa

Uma página que não converte costuma falhar por uma razão concreta e identificável,
não por não ser bonita. Ou não se percebe o que se vende, ou não se responde à
dúvida que trava a pessoa, ou há passos a mais entre a vontade e a ação.

## Como saber se correu bem

- Nada foi alterado na página
- As cinco objeções estão escritas do ponto de vista de quem visita
- Está dito quais são respondidas e quais não
- Cada recomendação é concreta e não um conselho genérico
- A lista está ordenada por impacto
