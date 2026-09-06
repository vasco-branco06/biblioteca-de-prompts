---
id: MKT-05
nome: Auditoria de uma página para pesquisa e para respostas de IA
categoria: marketing
nivel: recomendado
modo: diagnostico
origem: novo
gatilhos:
  - a minha página não aparece no Google
  - quero que a IA cite o meu site
  - ninguém me encontra
  - como é que apareço nas respostas do ChatGPT
  - preciso de melhorar o SEO desta página
nao_usar_quando:
  - a página existe mas o problema é converter quem já lá chega, usar EXP-01
  - o problema é velocidade ou telemóvel, usar PER-03 ou EXP-06
  - a análise é sobre um concorrente e não sobre a minha página, usar MKT-04
variaveis:
  - nome: pagina
    descricao: a página a auditar
    obrigatoria: true
    omissao: perguntar
  - nome: consultas
    descricao: o que uma pessoa escreve quando devia encontrar esta página
    obrigatoria: false
    omissao: derivar do conteúdo, propor cinco, e pedir confirmação antes de avaliar
  - nome: mercado
    descricao: país e idioma do público
    obrigatoria: false
    omissao: assumir Portugal e português europeu, e declarar a assunção
encadeia_com: [MKT-04, MKT-06, EXP-01, EXP-06]
---

## Prompt

Só diagnóstico. Audita {{pagina}} em duas frentes, para {{consultas}} em
{{mercado}}. São duas frentes diferentes e não uma só, porque quem procura e
quem pergunta a um modelo esperam coisas diferentes.

**Frente um, pesquisa clássica.**

1. Intenção. Para cada consulta, a página responde ao que a pessoa quer, ou
   responde a outra coisa parecida. Este é o ponto que decide tudo o resto.
2. Título e descrição. Dizem o que a pessoa vai encontrar, ou são um slogan.
3. Estrutura. Os títulos intermédios seguem uma hierarquia e cobrem as
   subperguntas, ou são decorativos.
4. Ligações internas. Que páginas apontam para esta, com que texto, e para onde
   esta aponta a seguir.
5. Dados estruturados. Existem, estão corretos, e correspondem ao que está
   visível na página.
6. Fundamentos técnicos. A página é indexável, tem endereço único e estável, e
   carrega em condições no telemóvel.

**Frente dois, respostas de IA.**

7. Cada secção responde a uma pergunta de forma completa, sem depender do resto
   da página. Um modelo cita parágrafos, não sites.
8. As afirmações têm número, data e origem. Uma frase com dados verificáveis é
   citada; uma opinião genérica não.
9. Fica claro quem escreve, com que autoridade, e quando foi atualizado.
10. A informação essencial está em texto e não presa dentro de imagens ou
    carregada só depois por código.
11. A entidade principal, a marca ou o produto, está nomeada de forma
    consistente e associada ao que faz.
12. Existe alguma coisa aqui que só exista aqui: um número próprio, um método,
    um caso. Uma página que repete o consenso não tem razão nenhuma para ser a
    citada.

Devolve uma lista priorizada por impacto, com a alteração concreta de cada item.
Escreve a frase que devia lá estar, em vez de dizeres para melhorar o texto.

Não alteres a página. Se alguma coisa não conseguires verificar sem acesso a
ferramentas que não tens, diz isso em vez de a avaliares às escuras.

## Porque importa

Cada vez mais respostas são lidas sem se abrir o site, e o que faz uma página
ser citada não é o mesmo que a faz posicionar-se. As duas coisas partilham
fundações e divergem no essencial: uma quer atrair o clique, a outra quer ser
extraível.

## Como saber se correu bem

- As consultas foram confirmadas antes da avaliação
- A correspondência com a intenção foi avaliada consulta a consulta
- As duas frentes foram avaliadas em separado
- Cada recomendação traz a frase concreta a usar
- O que não foi possível verificar ficou assinalado
