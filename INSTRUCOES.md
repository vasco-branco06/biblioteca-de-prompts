# Biblioteca de templates de prompt: instruções de construção

Documento de especificação. Quem o lê é o Claude Code (no Antigravity ou no terminal) e constrói a biblioteca a partir daqui. Não é um tutorial nem um manual de utilizador.

Autor do pedido: Vasco Branco.
Pasta da biblioteca: `C:\Users\Admin\Desktop\prompt maneger`
Data da especificação: 1 de setembro de 2026.

---

## 1. Objetivo

Criar uma biblioteca pessoal de templates de prompt que o Claude consulta sozinho. O Vasco descreve a tarefa em linguagem normal e o Claude vai buscar o melhor template, preenche-o com o contexto da conversa e executa-o. Não há copiar nem colar em momento nenhum.

Duas superfícies têm de funcionar:

1. Claude Code, dentro do Antigravity IDE, em qualquer projeto.
2. Claude Cowork, na app de desktop, com a pasta ligada como contexto.

---

## 2. Decisões já tomadas

Estas ficam fechadas. Não voltar a discutir nem propor alternativas.

| Assunto | Decisão |
|---|---|
| Mecanismo | Uma skill única de rota, com índice compacto e um ficheiro por template carregado só quando é preciso |
| Invocação | Automática, mas com aviso de uma linha a dizer qual o template usado e porquê |
| Âmbito da v1 | Converter as 78 da coleção original mais escrever 17 novos para marketing, estudo e dados |
| Formato | Tudo em template com variáveis. Nenhuma entrada pode ficar presa a um caso concreto |
| Crescimento | O Claude propõe guardar prompts que correram bem, e só grava com aprovação. Mais registo de uso |
| Utilização | Pessoal. Sem empacotamento para partilha, sem tratamento de licenças |
| Cópia de segurança | Repositório Git privado no GitHub |
| Idioma | Português europeu, sem emojis, sem travessões decorativos |

---

## 3. O que a biblioteca é, e o que não é

É um catálogo de instruções reutilizáveis que o Claude segue. Cada entrada descreve um método de trabalho, não um pedido concreto.

Não é uma coleção de textos para copiar. Não é uma base de dados de exemplos. Não é uma app.

Regra que decide qualquer dúvida de conversão: se uma entrada só serve para um projeto, um site ou um cliente específico, está mal convertida. Tem de servir para o próximo caso igual, seja ele qual for.

---

## 4. Arquitetura de ficheiros

```
prompt maneger/
├─ SKILL.md                    skill de rota, com o índice compacto embutido
├─ INSTRUCOES.md               este documento
├─ README.md                   o que isto é, como se usa, de onde veio a base
├─ fonte/
│  └─ colecao-original.md      as 78 originais, exportadas do Notion, intocadas
├─ templates/
│  ├─ planeamento/
│  ├─ diagnostico/
│  ├─ seguranca/
│  ├─ experiencia/
│  ├─ performance/
│  ├─ testes/
│  ├─ documentacao/
│  ├─ controlo/
│  ├─ marketing/
│  ├─ estudo/
│  └─ dados/
├─ regras/
│  └─ regras-permanentes.md    bloco pronto a colar no CLAUDE.md de cada projeto
├─ registo/
│  └─ uso.csv                  registo de utilizações
└─ ferramentas/
   ├─ gerar_indice.py          reconstrói o índice do SKILL.md a partir dos templates
   └─ registar_uso.py          acrescenta uma linha ao registo
```

### Localização e acesso nas duas superfícies

A pasta do Desktop é a biblioteca real. Só existe uma cópia.

Para o Claude Code a encontrar em todos os projetos, criar uma junção do Windows dentro da pasta de skills:

```
mklink /J "%USERPROFILE%\.claude\skills\biblioteca-de-prompts" "C:\Users\Admin\Desktop\prompt maneger"
```

Junções não precisam de privilégios de administrador. Se o comando falhar, parar e avisar, sem tentar copiar a pasta para os dois sítios. Duas cópias divergem sempre.

No Cowork, a pasta já está ligada como contexto, por isso o Claude lê o `SKILL.md` diretamente. Fica registada uma limitação conhecida: no Cowork a skill não aparece na lista de skills da conta, o que torna o disparo automático menos fiável do que no Claude Code. Se isso incomodar mais tarde, o caminho é publicar a skill de rota na conta. Não faz parte desta versão.

---

## 5. Formato de um template

Um ficheiro `.md` por template, dentro da pasta da categoria, com nome `ID-nome-curto.md`.

Exemplo completo, para servir de molde:

```markdown
---
id: SEG-07
nome: Caça a campos que o utilizador não devia controlar
categoria: seguranca
nivel: situacional
modo: diagnostico
origem: ccp-55
gatilhos:
  - formulário guarda dados na base de dados
  - registo ou edição de perfil
  - suspeita de que alguém se promove a admin
  - auditoria antes de publicar
nao_usar_quando:
  - o projeto não tem base de dados
  - o projeto não tem contas de utilizador
variaveis:
  - nome: alvo
    descricao: ficheiros, rotas ou funcionalidade a auditar
    obrigatoria: false
    omissao: auditar o projeto inteiro
  - nome: campos_sensiveis
    descricao: campos que nunca devem vir do cliente
    obrigatoria: false
    omissao: usar a lista por defeito do template
encadeia_com: [SEG-02, TES-04]
---

## Prompt

Só diagnóstico, não alteres código. Em {{alvo}}, encontra todos os sítios onde
dados vindos do utilizador são guardados diretamente na base de dados...
(resto do texto, com as variáveis marcadas)

## Porque importa

Explicação em linguagem simples, para quem não programa. Duas ou três frases.

## Como saber se correu bem

- Devolveu uma tabela com ficheiro e linha
- Não alterou ficheiro nenhum
- Para cada caso, disse o que um atacante conseguiria
```

### Regras do formato

O campo `modo` só aceita três valores e governa o comportamento:

- `diagnostico`: nunca altera ficheiros. Só analisa e reporta.
- `execucao`: altera o projeto. Exige que o Claude anuncie o que vai mudar antes de mudar.
- `regra`: nunca é executado. Descreve comportamento permanente e serve para ir para o `CLAUDE.md`.

O campo `gatilhos` é o que faz a biblioteca acertar ou falhar. Escrever cada gatilho como a pessoa fala, não como um técnico escreveria. "o site está lento" é um bom gatilho. "otimização de performance" não é.

O campo `nao_usar_quando` é obrigatório em todos os templates e existe para travar disparos errados. Um template sem esta secção está incompleto.

Variáveis usam `{{chave}}`. Toda a variável tem de ter um comportamento definido para quando falta: ou o Claude infere do contexto e declara a assunção numa linha, ou usa o valor de `omissao`. Nunca pergunta se conseguir inferir com segurança, e nunca inventa em silêncio.

---

## 6. As duas famílias

A coleção original mistura duas coisas diferentes. Separá-las é obrigatório.

**Templates de tarefa.** Pedem um trabalho concreto num momento concreto. Vão para `templates/` e entram no índice.

**Regras permanentes.** Descrevem comportamento contínuo. Vão para `regras/regras-permanentes.md`, com `modo: regra`, e ficam fora do índice de seleção. Este ficheiro é um bloco pronto a colar no `CLAUDE.md` de qualquer projeto novo.

Critério de classificação: se o texto começa por "a partir de agora", ou descreve uma postura que se mantém durante toda a sessão em vez de uma tarefa que acaba, é regra. Na coleção original isto apanha pelo menos a 1, a 6 e a 44. Verificar as restantes com o mesmo critério e apresentar a lista antes de mover.

---

## 7. A skill de rota

`SKILL.md` na raiz. Estrutura obrigatória:

```markdown
---
name: biblioteca-de-prompts
description: Biblioteca pessoal de templates de prompt do Vasco. Usar sempre que
  o pedido corresponda a um método já catalogado: planear um projeto, diagnosticar
  uma avaria, auditar segurança, melhorar performance ou experiência, escrever
  testes, documentar, escrever copy ou conteúdo, estudar um documento, analisar
  dados. Usar também quando ele disser "usa o melhor prompt", "usa a biblioteca"
  ou escrever /prompt.
---

## Como escolher

(regras da secção 8)

## Índice

| ID | Nome | Quando usar | Modo |
|----|------|-------------|------|
| PLA-01 | ... | ... | ... |
```

O índice fica dentro do `SKILL.md`, com uma linha por template. Com cerca de 95 entradas isso dá um ficheiro que o Claude lê de uma vez, e a escolha passa a não precisar de nenhuma leitura extra. O texto completo de cada template só é lido depois de escolhido.

O índice nunca é escrito à mão. É gerado por `ferramentas/gerar_indice.py`, que lê o frontmatter de todos os ficheiros em `templates/` e reescreve a tabela entre marcadores no `SKILL.md`. Correr sempre que se acrescenta ou altera um template.

---

## 8. Regras de seleção

Estas regras entram literalmente no `SKILL.md` e são o coração da coisa.

1. Ler o índice antes de responder a qualquer pedido de trabalho.
2. Escolher no máximo um template principal. Se o `encadeia_com` sugerir um seguinte, propor, não executar logo.
3. Se nenhum gatilho corresponder com clareza, não usar template nenhum e dizer numa linha que não há correspondência. Escolher um template a martelo é pior do que não escolher nenhum.
4. Verificar o `nao_usar_quando` antes de avançar. Se alguma condição se aplicar, descartar e procurar outro.
5. Um template de modo `diagnostico` nunca altera ficheiros, mesmo que o pedido pareça pedir a correção. Diagnosticar, reportar, e perguntar se quer que corrija.
6. Preencher as variáveis a partir do contexto da conversa e do projeto. Declarar as assunções numa linha. Perguntar só quando a dúvida muda mesmo o resultado.
7. Anunciar antes de trabalhar, numa linha e sem cerimónia: `Uso o SEG-07 (campos que o utilizador não devia controlar) porque falaste de um formulário que grava o perfil.`
8. Seguir o texto do template como instrução própria. Nunca o colar na resposta como se fosse conteúdo.
9. Registar o uso no fim.
10. Templates de modo `regra` nunca se executam. Se um for relevante, propor acrescentá-lo ao `CLAUDE.md` do projeto.

---

## 9. Registo de uso e crescimento

`registo/uso.csv`, com cabeçalho:

```
data_hora,id_template,superficie,projeto,pedido_resumo,resultado
```

Exemplo de linha: `2026-09-01T14:32:00,SEG-07,claude-code,projeto-exemplo,auditoria a formulario de perfil,bom`

`data_hora` em ISO 8601. `superficie` é `claude-code` ou `cowork`. `resultado` é `bom`, `mau` ou `nao_avaliado`. Acrescentar sempre uma linha, nunca reescrever o ficheiro. O `ferramentas/registar_uso.py` recebe os campos por argumento e faz o append. Abre no Excel sem tratamento nenhum, o que basta para ver mais tarde o que se usa e o que nunca se tocou.

Crescimento: quando o Vasco escreve um prompt à mão e o resultado é bom, o Claude propõe guardá-lo como template novo, já no formato da secção 5 e com a categoria e os gatilhos sugeridos. Só grava depois de ele dizer que sim, e corre logo o `gerar_indice.py`. Nunca guarda por iniciativa própria.

---

## 10. Núcleo novo a escrever

A coleção original cobre bem código, sites e segurança, e não cobre nada do resto. Escrever de raiz estes 17, no mesmo formato, com o mesmo nível de exigência:

**Marketing e conteúdo**

- MKT-01 Briefing de campanha a partir de um objetivo de negócio
- MKT-02 Copy de anúncio com vários ângulos e variantes
- MKT-03 Sequência de emails com objetivo definido
- MKT-04 Análise de um concorrente a partir do rasto público
- MKT-05 Auditoria de uma página para pesquisa clássica e para respostas de IA
- MKT-06 Calendário de conteúdo a partir de um tema central
- MKT-07 Reescrever texto que soa a gerado por IA

**Estudo e investigação**

- EST-01 Resumo estruturado de um documento longo, com o que ficou por responder
- EST-02 Ficha de estudo com progressão por níveis e flashcards
- EST-03 Revisão de literatura com fontes verificadas e nada inventado
- EST-04 Estrutura de um trabalho académico com critérios de avaliação
- EST-05 Explicação progressiva de um conceito difícil, da analogia à definição

**Dados**

- DAD-01 Diagnóstico de um ficheiro de dados: qualidade, buracos, tipos, duplicados
- DAD-02 Análise exploratória guiada por perguntas de negócio
- DAD-03 Transformação em Power Query, passo a passo e reproduzível
- DAD-04 Auditoria a um cálculo ou modelo de folha de cálculo
- DAD-05 Escolha do gráfico certo para a mensagem que se quer passar

Cada um leva as mesmas secções: prompt com variáveis, porque importa, como saber se correu bem. Nenhum pode assumir uma ferramenta específica sem a pôr numa variável.

---

## 11. Fases de construção

Trabalhar uma fase de cada vez. No fim de cada uma, mostrar o resultado e esperar aprovação antes de começar a seguinte. Não juntar fases.

**Fase 0. Preparação**
Criar a estrutura de pastas. Correr `git init`, criar o repositório privado no GitHub e ligar. `.gitignore` sem deixar passar segredos. Exportar a página do Notion para markdown e guardar em `fonte/colecao-original.md`, sem alterar uma vírgula. Confirmar que as 78 estão todas lá.

**Fase 1. Formato validado**
Converter três entradas à mão, uma de cada modo (uma de diagnóstico, uma de execução, uma de regra). Mostrar os três ficheiros. Só depois de aprovados é que se converte o resto. Se o formato tiver de mudar, muda agora, não a meio dos 78.

**Fase 2. Conversão em lote**
Converter as restantes, categoria a categoria, com uma paragem no fim de cada categoria. Em cada conversão: generalizar tudo o que é específico para variáveis, incluindo as tecnologias. Os prompts de segurança da coleção falam de Supabase, Next.js e Stripe pelo nome. Isso vira variável de stack, com uma nota a dizer como adaptar quando a ferramenta é outra. Manter o campo `origem` a apontar para o número original.

**Fase 3. Regras permanentes**
Aplicar o critério da secção 6, apresentar a lista das que vão sair do índice, e só depois mover. Escrever o `regras/regras-permanentes.md` como bloco pronto a colar.

**Fase 4. Núcleo novo**
Escrever os 17 da secção 10. Mostrar em grupos de cinco.

**Fase 5. Rota e acesso**
Escrever o `SKILL.md` com as regras da secção 8. Correr o `gerar_indice.py`. Criar a junção do Windows. Confirmar num projeto qualquer do Antigravity que o Claude Code vê a skill.

**Fase 6. Registo**
Escrever os dois scripts em `ferramentas/`. Testar o append.

**Fase 7. Testes de aceitação**
Correr a bateria da secção 12. Corrigir os gatilhos dos templates que falharem e repetir até passar.

**Fase 8. Fecho**
`README.md`, commit final, push para o repositório privado.

---

## 12. Testes de aceitação

Sem isto não está feito. Para cada frase, o Claude deve dizer que template escolheria, sem executar nada.

| Frase de teste | Esperado |
|---|---|
| o site está lento | template de diagnóstico das maiores lentidões |
| quero começar um projeto novo para gerir os meus treinos | entrevista antes de escrever seja o que for |
| acho que a minha base de dados está aberta a toda a gente | auditoria às políticas de acesso |
| isto ontem funcionava e hoje não | encontrar o que partiu |
| preciso de um anúncio para o Instagram | copy de anúncio |
| explica-me lá o que fizeste aí | explicação em linguagem simples |
| quantos utilizadores é que isto aguenta | teste com muitos dados |
| tenho um pdf de 80 páginas para estudar até quinta | resumo estruturado |
| este excel tem valores esquisitos | diagnóstico de ficheiro de dados |
| quero publicar amanhã | verificação rápida antes de publicar |
| o formulário cria dois registos quando clico depressa | blindagem ao duplo clique |
| a minha landing page não converte nada | auditoria de conversão |
| qual é a capital da Argentina | nenhum template |
| obrigado, ficou bom | nenhum template |
| apaga a pasta antiga | nenhum template, e a regra de pedir autorização aplica-se |

Critério de passagem: pelo menos 11 dos 12 primeiros certos, e os 3 últimos a não disparar template nenhum. Um falso disparo conta mais grave do que uma escolha errada, porque estraga a confiança na coisa toda.

Teste adicional de variáveis: dar um pedido sem contexto suficiente e confirmar que o Claude declara a assunção em vez de inventar em silêncio.

---

## 13. O que não fazer

- Não criar uma skill por template. Enche a lista e piora a escolha.
- Não duplicar a biblioteca entre o Desktop e a pasta de skills. Uma cópia, uma junção.
- Não escrever o índice à mão.
- Não deixar nenhum template sem `nao_usar_quando`.
- Não converter nada mantendo um caso concreto lá dentro.
- Não acrescentar funcionalidades que não estão aqui. Se parecer que falta alguma coisa, propor e esperar.
- Não usar emojis nem travessões decorativos em nada do que se escreve.
