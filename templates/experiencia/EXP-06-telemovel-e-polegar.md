---
id: EXP-06
nome: Auditoria de telemóvel, com uma mão e o polegar
categoria: experiencia
nivel: recomendado
modo: diagnostico
origem: ccp-36
gatilhos:
  - no telemóvel isto fica mau
  - os botões são pequenos demais
  - tenho de fazer zoom para ler
  - a página anda para o lado no telemóvel
  - a maior parte das visitas é de telemóvel
nao_usar_quando:
  - o produto só é usado em computador, por desenho
  - a preocupação é a velocidade e não o toque, usar EXP-10
  - a aplicação é nativa e não uma página web
variaveis:
  - nome: largura
    descricao: a largura de ecrã a testar
    obrigatoria: false
    omissao: usar cerca de 375 pontos, que é o telemóvel pequeno comum
  - nome: pagina
    descricao: as páginas a testar
    obrigatoria: false
    omissao: testar o percurso principal, do primeiro ecrã até à ação
encadeia_com: [EXP-02, EXP-04, EXP-10]
---

## Prompt

Só diagnóstico. Analisa {{pagina}} num ecrã de {{largura}}, a assumir uso com uma
só mão e o polegar. Não me digas apenas se é responsivo.

1. **Alvos de toque.** Os botões e ligações têm pelo menos quarenta e quatro por
   quarenta e quatro pontos, e espaço suficiente entre si para não haver toques
   errados. Lista os que não têm, com o componente.
2. **Alcance.** O botão de ação principal está na zona que o polegar alcança sem
   mudar a pega, ou está no topo do ecrã. O topo é a pior zona num telemóvel e a
   melhor num computador, e é aí que a maioria dos sites o põe.
3. **Largura.** Há deslocamento horizontal acidental, texto que obriga a fazer
   zoom, ou tabelas e blocos de código que rebentam a largura.
4. **Camadas.** Menus, janelas e avisos fecham-se com facilidade, e não tapam o
   conteúdo nem o campo que se está a preencher quando o teclado abre.
5. **Primeiro ecrã.** O que se vê sem descer inclui a proposta de valor e uma
   ação, ou apenas o cabeçalho e o logótipo.

Lista cada problema com o componente e a correção, ordenado por impacto.

Não alteres nada.

## Porque importa

A maioria das visitas chega de telemóvel, com uma mão ocupada e a andar. O site
ajustar-se ao ecrã é o mínimo e não chega: se o botão for pequeno demais para
acertar, ou estiver longe do polegar, a pessoa não age, e nada nas estatísticas
explica porquê.

## Como saber se correu bem

- Os alvos de toque foram medidos e não avaliados a olho
- A posição da ação principal foi avaliada em relação ao alcance do polegar
- O deslocamento horizontal foi verificado
- O comportamento com o teclado aberto foi considerado
- Cada problema tem componente e correção
