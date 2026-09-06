---
name: biblioteca-de-prompts
description: >-
  Biblioteca pessoal de templates de prompt do Vasco. Usar sempre que
  o pedido corresponda a um método já catalogado: planear um projeto, diagnosticar
  uma avaria, auditar segurança, melhorar performance ou experiência, escrever
  testes, documentar, escrever copy ou conteúdo, estudar um documento, analisar
  dados. Usar também quando ele disser "usa o melhor prompt", "usa a biblioteca"
  ou escrever /prompt.
---

# Biblioteca de prompts

Catálogo de métodos de trabalho reutilizáveis. Cada entrada do índice é um
ficheiro em `templates/`, com o texto completo do prompt, o que ele faz e como se
sabe que correu bem. O índice serve para escolher; o ficheiro só se lê depois de
escolhido.

## Como escolher

1. Lê o índice antes de responderes a qualquer pedido de trabalho.
2. Escolhe no máximo um template principal. Se o `encadeia_com` sugerir um
   seguinte, propõe-no, não o executes.
3. Se nenhum gatilho corresponder com clareza, não uses template nenhum e diz
   numa linha que não há correspondência. Escolher um a martelo é pior do que não
   escolher nenhum.
4. Verifica o `nao_usar_quando` antes de avançares. Se alguma condição se
   aplicar, descarta e procura outro.
5. Um template de modo `diagnostico` nunca altera ficheiros, mesmo que o pedido
   pareça pedir a correção. Diagnostica, reporta, e pergunta se queres que
   corrija.
6. Preenche as variáveis a partir do contexto da conversa e do projeto. Declara
   as assunções numa linha. Pergunta só quando a dúvida muda mesmo o resultado.
7. Anuncia antes de trabalhar, numa linha e sem cerimónia.
8. Segue o texto do template como instrução tua. Nunca o coles na resposta como
   se fosse conteúdo.
9. Regista o uso no fim.
10. Templates de modo `regra` nunca se executam. Se um for relevante, propõe
    acrescentá-lo ao `CLAUDE.md` do projeto.

Forma do anúncio:

> Uso o SEG-10 (campos que o utilizador não devia controlar) porque falaste de um
> formulário que grava o perfil.

## Modos

- `diagnostico`: nunca altera ficheiros. Analisa e reporta.
- `execucao`: altera o projeto ou produz um artefacto. Anuncia o que vai mudar
  antes de mudar.
- `regra`: nunca é executado. Vive em `regras/regras-permanentes.md` e fica fora
  deste índice.

## Variáveis

As variáveis aparecem como `{{chave}}` no texto do template e estão declaradas no
frontmatter, cada uma com o seu comportamento quando falta. Ou se infere do
contexto e se declara a assunção numa linha, ou se usa o valor de `omissao`.
Nunca perguntes o que consegues inferir com segurança, e nunca inventes em
silêncio.

## Regras permanentes

Três entradas da coleção descrevem comportamento contínuo e não tarefas. Estão em
`regras/regras-permanentes.md`, fora deste índice, e propõem-se para o
`CLAUDE.md` do projeto em vez de serem executadas.

## Registo

No fim de cada utilização, acrescenta uma linha a `registo/uso.csv`, com o
formato `data_hora,id_template,superficie,projeto,pedido_resumo,resultado`. A
data em ISO 8601, a superfície como `claude-code` ou `cowork`, e o resultado como
`bom`, `mau` ou `nao_avaliado`. Acrescenta sempre, nunca reescrevas o ficheiro.

## Crescimento

Quando o Vasco escrever um prompt à mão e o resultado for bom, propõe guardá-lo
como template novo, já no formato dos existentes e com categoria e gatilhos
sugeridos. Só grava depois de ele dizer que sim, e corre logo
`ferramentas/gerar_indice.py`. Nunca guardes por iniciativa própria.

## Índice

<!-- INICIO INDICE. Gerado por ferramentas/gerar_indice.py. Nao editar a mao. -->

| ID | Nome | Quando usar | Modo |
|----|------|-------------|------|
| PLA-01 | Planeia primeiro, mexe depois | antes de mexeres diz-me o que vais fazer; quero ver o plano primeiro; não mexas ainda; isto parece grande, como é que vais fazer; explica-me o que vais alterar antes de alterares | diagnostico |
| PLA-02 | Entrevista antes de escrever seja o que for | quero começar um projeto novo; tenho uma ideia para uma app; quero fazer um site para; por onde é que começo; ajuda-me a montar isto do zero | execucao |
| PLA-03 | A versão mais simples que já vale a pena | tenho uma ideia mas não sei por onde começar; quero lançar isto depressa; isto está a ficar grande demais; o que é que preciso mesmo para a primeira versão; quero uma coisa simples para começar | diagnostico |
| PLA-04 | Fatiar o plano em fases que já funcionam | tenho o plano e não sei por onde começar; isto é muito trabalho de uma vez; quero ver alguma coisa a funcionar depressa; divide-me isto em partes; por que fase é que começo | execucao |
| PLA-05 | Escolher ferramentas simples, com a razão de cada uma | com que ferramentas é que faço isto; não sei o que escolher; qual é a forma mais fácil de construir isto; preciso de uma base de dados mas não sei qual; o que é que uso para pôr isto no ar | diagnostico |
| PLA-06 | Especificação com critérios que eu consigo testar | quero garantir que fica bem feito; como é que eu confirmo que ficou como pedi; escreve o que isto tem de fazer antes de programares; preciso de uma lista do que tem de funcionar; quero uma especificação | execucao |
| PLA-07 | Cortar o que está complicado a mais | isto parece complicado demais para o que eu quero; será que preciso disto tudo; o plano ficou enorme; revê este plano com olhos críticos; simplifica-me isto antes de começarmos | diagnostico |
| PLA-08 | Quanto vai custar e até onde é grátis | quanto é que isto me vai custar; isto é grátis; não quero surpresas na fatura; a partir de quantos utilizadores começo a pagar; quero saber os custos antes de avançar | diagnostico |
| PLA-09 | As decisões que faltam, com recomendação para cada uma | o que é que temos de decidir antes de começar; não quero que decidas sozinho; que escolhas é que isto implica; antes de construires esta funcionalidade; quais são as decisões importantes aqui | diagnostico |
| PLA-10 | Estimativa honesta de tempo, risco e a experiência que tira a dúvida | quanto tempo é que isto demora; vale a pena avançar com isto; onde é que me vou atrapalhar; isto é muito ambicioso; por onde é mais seguro começar | diagnostico |
| DIA-01 | Parar e diagnosticar, sem mexer em mais nada | para; isto está a piorar; não mexas mais; estás a fazer coisas que eu não pedi; já não percebo o que se está a passar aqui | diagnostico |
| DIA-02 | Encontrar a alteração que partiu isto | isto ontem funcionava e hoje não; deixou de funcionar e não sei o que mudou; o que é que estragou isto; estava tudo bem até há pouco; alguma coisa que mexemos partiu outra coisa | diagnostico |
| DIA-03 | Funciona no meu computador mas não no site publicado | aqui funciona mas no site dá erro; depois de publicar deixou de funcionar; o site publicado está em branco; no meu computador está tudo bem; só dá erro na versão que está no ar | diagnostico |
| DIA-04 | Voltar atrás na última alteração | desfaz o que fizeste; volta atrás; isso piorou, anula; quero como estava antes; esquece essa alteração | execucao |
| DIA-05 | Provar a causa com registos, em vez de adivinhar | já tentámos três correções e continua igual; não sabemos porque é que isto acontece; estás a adivinhar; preciso de perceber o que se passa lá dentro; o erro não faz sentido nenhum | execucao |
| DIA-06 | Apanhar o erro que só acontece às vezes | às vezes acontece e às vezes não; não consigo repetir o erro; só acontece de vez em quando; quando quero mostrar a alguém funciona sempre; já aconteceu duas ou três vezes mas nunca quando quero | diagnostico |
| DIA-07 | Recuperar um ficheiro apagado | apaguei um ficheiro sem querer; desapareceu um ficheiro; onde é que foi parar aquele ficheiro; apaguei a pasta errada; preciso de recuperar uma coisa que apaguei | execucao |
| SEG-01 | Palavras-passe e chaves escritas à vista no código | será que tenho palavras-passe no código; isto é seguro para publicar; colei aqui uma chave e não sei se faz mal; antes de pôr isto no GitHub; tenho medo de expor as minhas chaves | diagnostico |
| SEG-02 | Auditoria às regras de acesso da base de dados | acho que a minha base de dados está aberta a toda a gente; qualquer pessoa consegue ver os dados dos outros; liguei a base de dados ao site e não configurei permissões; não sei se as regras de acesso estão bem postas; auditoria à base de dados antes de publicar | diagnostico |
| SEG-03 | Os segredos já fugiram, e agora | acho que já enviei uma chave para o GitHub; apaguei a chave do ficheiro, já está resolvido; tinha um ficheiro de configuração no repositório; o repositório era público; isto pode ter escapado alguma coisa | diagnostico |
| SEG-04 | Que páginas exigem login e quais estão abertas | qualquer pessoa consegue entrar na área de administração; que páginas é que estão protegidas; isto precisa de login; esqueci-me de trancar alguma página; quem é que consegue ver o quê | diagnostico |
| SEG-05 | Validar tudo o que vem do utilizador | os meus formulários são seguros; alguém pode escrever coisas estranhas nos campos; isto aceita qualquer coisa; tenho medo de ataques pelos formulários; o que acontece se escreverem código no campo | diagnostico |
| SEG-06 | Bibliotecas com falhas de segurança conhecidas | as bibliotecas que uso são seguras; apareceu-me um aviso de vulnerabilidade; isto está desatualizado; devia atualizar as dependências; vi uma notícia sobre uma falha numa biblioteca | diagnostico |
| SEG-07 | Olhar para o projeto como quem o quer atacar | isto é seguro; por onde é que me podem atacar; quero uma verificação geral de segurança; nunca pensei nisto do ponto de vista da segurança; o que é que pode correr mal em termos de segurança | diagnostico |
| SEG-08 | Cada pedido confirma que os dados são mesmo daquela pessoa | será que um utilizador consegue ver os dados de outro; o endereço tem o número da encomenda, isso é seguro; se eu mudar o número no link o que acontece; cada pessoa só devia ver as suas coisas; tenho contas de utilizador e dados separados por pessoa | diagnostico |
| SEG-09 | A proteção tem de estar no servidor, não no ecrã | escondi o botão de administrador, chega; a verificação está toda num sítio só; o que acontece se alguém chamar isto diretamente; só os administradores é que veem esta opção; tenho a proteção na camada de entrada | diagnostico |
| SEG-10 | Campos que o utilizador não devia poder controlar | o formulário guarda os dados direto na base de dados; alguém pode promover-se a administrador; tenho um formulário de perfil que grava tudo; o registo aceita o que vier; será que dá para alguém mudar o próprio plano | diagnostico |
| SEG-11 | Avisos de serviços externos e tarefas agendadas | recebo avisos do sistema de pagamentos; tenho uma tarefa que corre todos os dias; como é que sei que o aviso veio mesmo de quem diz; alguém pode fingir que me pagou; tenho um endereço que recebe notificações automáticas | diagnostico |
| SEG-12 | Ficheiros enviados pelos utilizadores | as pessoas podem carregar fotografias; tenho uma zona de anexos; deixo enviar ficheiros no formulário; onde é que ficam guardados os ficheiros que enviam; será que alguém pode ver os ficheiros de outra pessoa | diagnostico |
| SEG-13 | Ordens escondidas no texto que chega ao modelo de IA | o meu site usa inteligência artificial; tenho um assistente que lê mensagens dos utilizadores; o modelo consegue enviar emails; dou documentos de utilizadores a ler à IA; isto resume páginas da internet automaticamente | diagnostico |
| SEG-14 | O que me rebenta a conta ou o servidor se for abusado | e se alguém puser um programa a chamar isto sem parar; tenho medo de receber uma fatura enorme; isto pode ser usado para enviar spam em meu nome; quanto é que alguém me pode fazer gastar; o servidor aguenta se alguém quiser abusar | diagnostico |
| SEG-15 | O que a aplicação deixa escapar sem dar por isso | o erro mostra coisas técnicas ao utilizador; outro site consegue chamar a minha API; o que é que os meus registos guardam; apareceu-me um erro com o nome das tabelas; isto revela se um email já existe | diagnostico |
| SEG-16 | Limitar as tentativas de entrada | alguém pode tentar adivinhar a palavra-passe; o login não tem limite de tentativas; tenho medo que entrem na conta de um cliente; quantas vezes é que se pode falhar a palavra-passe; isto tem proteção contra tentativas repetidas | diagnostico |
| EXP-01 | Auditoria de conversão de uma página | a minha landing page não converte nada; tenho visitas mas ninguém compra; as pessoas entram e saem logo; porque é que ninguém se regista; esta página não está a resultar | diagnostico |
| EXP-02 | O teste dos cinco segundos e a hierarquia visual | percebe-se logo o que isto é; a página parece confusa; não sei se as pessoas percebem para onde olhar; está tudo com o mesmo peso; qual é a primeira impressão que isto dá | diagnostico |
| EXP-03 | Inventário de estados: a carregar, erro, vazio, sucesso | fica um ecrã em branco enquanto carrega; quando dá erro não aparece nada; o utilizador não sabe se aconteceu alguma coisa; a primeira vez que se entra está tudo vazio; não sei se tratei todos os casos | diagnostico |
| EXP-04 | Reduzir a fricção nos formulários | as pessoas começam a preencher e desistem; o formulário é muito comprido; só dá erro no fim quando carrego em enviar; perco tudo o que escrevi quando falha; tenho um formulário de registo com muitos campos | diagnostico |
| EXP-05 | Deixar de parecer feito por IA | isto parece um template; está funcional mas sem alma; parece igual a todos os sites; percebe-se logo que foi feito por IA; quero que isto tenha personalidade | diagnostico |
| EXP-06 | Auditoria de telemóvel, com uma mão e o polegar | no telemóvel isto fica mau; os botões são pequenos demais; tenho de fazer zoom para ler; a página anda para o lado no telemóvel; a maior parte das visitas é de telemóvel | diagnostico |
| EXP-07 | Auditoria de acessibilidade | isto é acessível; uma pessoa que não veja consegue usar isto; o texto está muito claro e não se lê; só se consegue usar com rato; preciso de cumprir as regras de acessibilidade | diagnostico |
| EXP-08 | Reescrever os textos da interface e as mensagens de erro | as mensagens de erro são horríveis; aparece erro 400 ao utilizador; os textos soam a robô; ninguém percebe o que fazer quando falha; os botões dizem todos enviar | diagnostico |
| EXP-09 | Consistência visual e conjunto mínimo de decisões | tenho cinco vermelhos quase iguais; os botões estão todos ligeiramente diferentes; isto parece amador mas não sei porquê; cada página tem espaçamentos diferentes; quero organizar as cores e os tamanhos | diagnostico |
| EXP-10 | Velocidade sentida, e não apenas a medida | parece lento mas os testes dizem que está rápido; fica um bocado em branco antes de aparecer; as coisas saltam de sítio enquanto carrega; clico e parece que não aconteceu nada; dá a sensação de que está sempre à espera | diagnostico |
| PER-01 | Arrumar o código por dentro com rede de segurança | isto está uma confusão, arruma; quero limpar o código sem partir nada; dá para organizar isto melhor; o código funciona mas está mal feito; preciso de refatorar | execucao |
| PER-02 | Imagens, prioridade e o salto do conteúdo | o conteúdo salta enquanto carrega; a imagem grande do topo demora imenso; as imagens são muito pesadas; cliquei e ele mudou de sítio; o Google diz que a minha página é instável | diagnostico |
| PER-03 | As três maiores lentidões | o site está lento; isto demora imenso a abrir; porque é que isto é tão lento; as pessoas queixam-se da lentidão; preciso de acelerar isto | diagnostico |
| PER-04 | Código que já não é usado por ninguém | deve haver aqui muita coisa a mais; isto ainda é usado; tenho ficheiros que já não sei para que servem; quero limpar o projeto; sobrou código de coisas que já tirámos | diagnostico |
| PER-05 | Limpar mensagens de depuração esquecidas | ficaram aqui mensagens de teste; a consola está cheia de coisas; antes de publicar quero limpar isto; tenho prints espalhados pelo código; deixei coisas de depuração no código | execucao |
| PER-06 | Consultas repetidas dentro de ciclos | a página com a lista está lenta; com poucos dados era rápido e agora arrasta; quanto mais registos mais lento fica; a listagem demora imenso a abrir; isto faz muitos pedidos à base de dados | diagnostico |
| PER-07 | Emagrecer o que carrega no arranque | a primeira visita demora imenso; no telemóvel com dados móveis é insuportável; o site é pesado a abrir; descarrega muita coisa antes de aparecer; quero reduzir o tamanho do site | diagnostico |
| PER-08 | A mesma lógica repetida em vários sítios | ando sempre a corrigir a mesma coisa em vários sítios; isto está copiado em três sítios; mudei num sítio e esqueci-me do outro; há muito código repetido aqui; dá para juntar isto tudo | diagnostico |
| PER-09 | Partir o ficheiro ou a função que ficou gigante | este ficheiro tem duas mil linhas; já ninguém percebe o que está aqui; esta função faz coisas de mais; tenho um ficheiro que faz tudo; isto precisa de ser dividido | execucao |
| PER-10 | Alinhar ao padrão que o projeto já usa | cada parte do código faz as coisas à sua maneira; isto está inconsistente; construí isto ao longo de várias sessões e ficou tudo diferente; qual é a forma certa de fazer isto neste projeto; quero uniformizar a maneira de fazer as coisas | diagnostico |
| PER-11 | Bibliotecas instaladas que ninguém usa | devo ter aqui coisas instaladas que já não uso; a lista de dependências está enorme; instalei coisas para experimentar e ficaram; quero limpar as bibliotecas; isto precisa de tantas dependências assim | diagnostico |
| TES-01 | Verificação rápida antes de publicar | quero publicar amanhã; vou pôr isto no ar; antes de publicar; como é que sei que não parti nada; vou lançar isto hoje | execucao |
| TES-02 | Testar o percurso que não pode falhar | quero ser avisado se isto partir; o registo não pode falhar nunca; preciso de testes para o que é importante; já parti isto duas vezes sem dar por isso; quero garantir que o principal continua a funcionar | execucao |
| TES-03 | Blindar o duplo clique e os cliques repetidos | o formulário cria dois registos quando clico depressa; apareceram encomendas repetidas; se carregar duas vezes acontece duas vezes; cobrou duas vezes ao mesmo cliente; as pessoas carregam outra vez porque parece que não fez nada | execucao |
| TES-04 | Testar os casos estranhos, não só o caminho feliz | só testei com dados bonitos; e se alguém deixar o campo vazio; as pessoas escrevem coisas que eu não esperava; isto parte com acentos; quero testar os casos limite | execucao |
| TES-05 | Primeiro um teste que falha, só depois a correção | este erro já apareceu duas vezes; corrigimos isto e voltou; quero garantir que este problema não volta; encontrei um defeito; isto tem de ficar resolvido de vez | execucao |
| TES-06 | Testar com muitos dados, não com três exemplos | quantos utilizadores é que isto aguenta; com poucos dados funciona bem; e se tiver mil registos; isto aguenta o lançamento; não sei se isto escala | execucao |
| DOC-01 | Explica em linguagem simples | explica-me lá o que fizeste aí; não percebi nada do que disseste; o que é isso que acabaste de dizer; fala como se eu não soubesse programar; explica isso por palavras simples | diagnostico |
| DOC-02 | A memória do projeto para as próximas sessões | estou farto de repetir as mesmas coisas; de cada vez que abro isto começamos do zero; já respondi a essa pergunta três vezes; quero que te lembres das decisões do projeto; cria o ficheiro de regras do projeto | execucao |
| DOC-03 | Explica o que fizeste e porquê, para eu aprender | quero perceber o que mudou no projeto; explica-me para eu aprender; o que é que isto muda daqui para a frente; resume o que fizeste nesta tarefa; quero aprender e não só receber código | diagnostico |
| DOC-04 | O mapa do projeto, para quem chega sem memória | já não sei onde está cada coisa; explica-me como o projeto está organizado; preciso de um mapa disto; a IA anda perdida no meu projeto; onde é que fica cada parte | execucao |
| DOC-05 | README para quem chega novo | preciso de um readme; quero partilhar isto com alguém; como é que outra pessoa põe isto a funcionar; vou pôr isto no GitHub; falta a documentação inicial | execucao |
| DOC-06 | Registar a decisão e as alternativas rejeitadas | acabámos de decidir uma coisa importante; regista esta decisão; não quero voltar a discutir isto daqui a um mês; porque é que escolhemos isto mesmo; guarda o porquê desta escolha | execucao |
| CTL-01 | Fechar o ciclo: escrever, experimentar, corrigir até passar | disseste que estava feito e não está; experimenta antes de me dizeres que acabaste; quero ver a prova de que funciona; não me digas feito sem confirmares; corre isso e mostra o resultado | execucao |
| CTL-02 | Rever o próprio trabalho com olhos de cético | revê o que acabaste de fazer; será que isso está mesmo bem; dá uma vista de olhos crítica a isso; antes de eu dar por bom; vê se não deixaste nada mal feito | execucao |
| CTL-03 | Guardar o trabalho em segurança | guarda o que já está feito; não quero perder isto; antes de continuarmos guarda tudo; faz um ponto de retorno; vamos parar por hoje | execucao |
| CTL-04 | Resume o que percebeste antes de avançar | antes de avançares diz-me o que percebeste; quero confirmar que estamos a falar do mesmo; repete-me o que te pedi; não tenho a certeza de que me percebeste; explica-me o que vais fazer em três frases | diagnostico |
| CTL-05 | Dois ou três caminhos, com vantagens e desvantagens | há outra maneira de fazer isto; não escolhas logo o primeiro caminho; quais são as opções; quero decidir eu como é que isto se faz; dá-me alternativas antes de avançares | diagnostico |
| CTL-06 | Pensar a fundo antes de decidir | isto é uma decisão importante; pensa bem antes de responder; não tenhas pressa nesta; isto vai ser difícil de mudar depois; preciso que penses a sério nisto | diagnostico |
| CTL-07 | Gravar a correção como regra do projeto | já te disse isto três vezes; isto é uma regra permanente; grava isso para não voltares a fazer; de agora em diante é sempre assim; não quero repetir isto em cada conversa | execucao |
| CTL-08 | Investigar num subagente e receber só o resumo | antes de mexeres investiga como isto funciona; não me encham a conversa com ficheiros todos; preciso que percebas o projeto antes de avançar; lê isto tudo mas dá-me só o resumo; vê como está feita esta parte | diagnostico |
| CTL-09 | A conversa está a ficar grande | esta conversa já vai longa; andas a repetir-te; já não te lembras do que combinámos ao princípio; isto está a ficar caro; acho que já te perdeste | diagnostico |
| MKT-01 | Briefing de campanha a partir de um objetivo de negócio | quero fazer uma campanha; preciso de divulgar isto; quero mais vendas no próximo mês; vamos lançar isto e não sei por onde começar; preciso de trazer gente para aqui | execucao |
| MKT-02 | Copy de anúncio com vários ângulos e variantes | preciso de um anúncio; escreve-me um anúncio para o Instagram; preciso de texto para uma campanha paga; não sei o que hei de escrever no anúncio; quero testar várias versões do mesmo anúncio | execucao |
| MKT-03 | Sequência de emails com objetivo definido | preciso de uma sequência de emails; as pessoas inscrevem-se e depois não acontece nada; quero fazer um seguimento automático; tenho uma lista e não faço nada com ela; quero uma série de emails para quem descarrega isto | execucao |
| MKT-04 | Análise de um concorrente a partir do rasto público | o que é que a concorrência anda a fazer; analisa-me este concorrente; porque é que eles vendem mais do que eu; como é que eles se posicionam; quero perceber contra quem estou a competir | diagnostico |
| MKT-05 | Auditoria de uma página para pesquisa e para respostas de IA | a minha página não aparece no Google; quero que a IA cite o meu site; ninguém me encontra; como é que apareço nas respostas do ChatGPT; preciso de melhorar o SEO desta página | diagnostico |
| MKT-06 | Calendário de conteúdo a partir de um tema central | nunca sei sobre o que hei de publicar; preciso de um plano de conteúdos; quero publicar com regularidade; fico sem ideias ao fim de duas semanas; o que é que publico este mês | execucao |
| MKT-07 | Reescrever texto que soa a gerado por IA | isto soa a escrito por IA; o texto está correto mas não parece meu; parece que foi tudo gerado; quero que isto soe a pessoa; este texto não tem voz nenhuma | execucao |
| EST-01 | Resumo estruturado de um documento longo | tenho um pdf de oitenta páginas para estudar; preciso de perceber isto até quinta; resume-me este documento; não tenho tempo para ler isto tudo; o que é que interessa mesmo neste relatório | execucao |
| EST-02 | Ficha de estudo com progressão por níveis e flashcards | tenho teste na próxima semana; preciso de decorar isto; como é que estudo esta matéria; quero fazer flashcards disto; tenho de saber isto de cor | execucao |
| EST-03 | Revisão de literatura com fontes verificadas | preciso de fazer o estado da arte; o que é que já se escreveu sobre isto; preciso de fontes para este trabalho; faz-me uma revisão de literatura; preciso de referências académicas sobre este tema | execucao |
| EST-04 | Estrutura de um trabalho académico com os critérios à vista | tenho de entregar um trabalho e não sei como o organizar; por onde começo este relatório; quantas páginas para cada parte; tenho a matéria toda mas não sei estruturar; como é que estruturo a tese | execucao |
| EST-05 | Explicação progressiva de um conceito difícil | não estou a perceber isto de todo; explica-me isto do início; já li três vezes e não entra; o que é isto na prática; toda a gente diz que é simples e eu não percebo | diagnostico |
| DAD-01 | Diagnóstico de um ficheiro de dados | este excel tem valores esquisitos; as contas não batem certo; recebi um ficheiro e não sei se posso confiar nele; há linhas repetidas nesta folha; antes de analisar isto quero saber se está bom | diagnostico |
| DAD-02 | Análise exploratória guiada por perguntas de negócio | o que é que estes dados me dizem; tenho isto tudo e não sei o que fazer com os dados; quero perceber o que se está a passar nas vendas; analisa-me este ficheiro; que conclusões se tiram daqui | diagnostico |
| DAD-03 | Transformação de dados passo a passo e reproduzível | tenho de limpar isto antes de usar; preciso de juntar estes dois ficheiros; todos os meses faço isto à mão; preciso de mudar o formato destas colunas; quero automatizar esta preparação de dados | execucao |
| DAD-04 | Auditoria a um cálculo ou modelo de folha de cálculo | as contas não batem certo; este total está errado e não sei porquê; herdei esta folha de outra pessoa; vou apresentar isto e quero ter a certeza; confias neste ficheiro de orçamento | diagnostico |
| DAD-05 | Escolher o gráfico certo para a mensagem | que gráfico é que uso para isto; este gráfico não se percebe; quero mostrar isto numa apresentação; faço um gráfico de barras ou de linhas; como é que mostro esta evolução | diagnostico |

<!-- FIM INDICE -->
