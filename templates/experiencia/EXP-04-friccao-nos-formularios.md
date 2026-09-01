---
id: EXP-04
nome: Reduzir a fricção nos formulários
categoria: experiencia
nivel: recomendado
modo: diagnostico
origem: ccp-34
gatilhos:
  - as pessoas começam a preencher e desistem
  - o formulário é muito comprido
  - só dá erro no fim quando carrego em enviar
  - perco tudo o que escrevi quando falha
  - tenho um formulário de registo com muitos campos
nao_usar_quando:
  - o projeto não tem formulários
  - a preocupação é a validação do ponto de vista da segurança, usar SEG-05
  - o que se quer é só reescrever os textos, usar EXP-08
variaveis:
  - nome: formularios
    descricao: que formulários analisar
    obrigatoria: false
    omissao: analisar todos os do projeto
encadeia_com: [EXP-03, EXP-08, TES-03, SEG-05]
---

## Prompt

Só diagnóstico. Analisa {{formularios}}, um a um.

**Campos.** Lista todos e, para cada um, diz se pode ser eliminado, tornado
opcional, ou pedido mais tarde. Justifica porque é que cada campo que fica é
mesmo necessário agora, neste momento do percurso. A pergunta a fazer a cada
campo é: o que acontece se eu não souber isto hoje.

**Etiquetas.** Estão sempre visíveis, ou existem só como texto de exemplo dentro
do campo que desaparece assim que se começa a escrever. Se desaparecem, a pessoa
deixa de saber o que estava a preencher.

**Validação.** Avisa enquanto se preenche e diz como corrigir, ou só rebenta no
fim, ao carregar em enviar, com tudo errado de uma vez.

**Botão.** Diz a ação concreta, como criar a minha conta, ou é genérico, como
enviar.

**Recuperação.** Se der erro no envio, o que estava escrito perde-se.

**Teclado e telemóvel.** Cada campo abre o teclado certo no telemóvel, e a ordem
de navegação por teclado segue a ordem visual.

Entrega a versão enxuta de cada formulário e a lista de alterações ordenada por
fricção removida. Não alteres nada.

## Porque importa

Cada campo a mais é uma oportunidade de desistir, e a desistência acontece em
silêncio: ninguém escreve a dizer que achou o formulário chato. Um formulário
curto com erros bem explicados converte mais do que um bonito e comprido.

## Como saber se correu bem

- Cada campo que fica está justificado por uma necessidade de agora
- Está dito se as etiquetas desaparecem ao escrever
- O momento da validação foi avaliado, e não só a existência dela
- Ficou claro se o conteúdo escrito se perde em caso de erro
- Existe uma versão enxuta proposta para cada formulário
