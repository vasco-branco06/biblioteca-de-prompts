---
id: SEG-02
nome: Auditoria às regras de acesso da base de dados
categoria: seguranca
nivel: recomendado
modo: diagnostico
origem: ccp-25
gatilhos:
  - acho que a minha base de dados está aberta a toda a gente
  - qualquer pessoa consegue ver os dados dos outros
  - liguei a base de dados ao site e não configurei permissões
  - não sei se as regras de acesso estão bem postas
  - auditoria à base de dados antes de publicar
nao_usar_quando:
  - o projeto não tem base de dados
  - a base de dados só é acedida a partir do servidor e nunca do navegador, e aí o risco está nas rotas, usar SEG-09
  - o que se procura são chaves ou palavras-passe expostas, usar SEG-01 ou SEG-03
  - já se sabe qual é a tabela desprotegida e o que se quer é corrigi-la
variaveis:
  - nome: plataforma_dados
    descricao: onde vivem os dados e que mecanismo de permissões usa
    obrigatoria: false
    omissao: detetar pelas dependências e configuração do projeto, e declarar numa linha o que foi encontrado
  - nome: alvo
    descricao: tabelas, coleções ou área a auditar
    obrigatoria: false
    omissao: auditar tudo
  - nome: chave_publica
    descricao: a chave ou identidade que o site entrega ao navegador de qualquer visitante
    obrigatoria: false
    omissao: assumir que existe uma e identificá-la na configuração
encadeia_com: [SEG-08, SEG-09, SEG-04]
---

## Prompt

Só diagnóstico. Não alteres regras, não corras migrações, não mexas na
configuração. Audita as permissões de acesso aos dados em {{plataforma_dados}},
sobre {{alvo}}.

1. Cobertura. Lista todas as tabelas e diz quais têm proteção por linha ativa e
   quais não têm. Uma tabela sem proteção é lida e escrita por qualquer pessoa
   que tenha {{chave_publica}}, que vai no código enviado ao navegador e por isso
   está à vista. Trata cada uma dessas como crítica, sem exceção.
2. Operações. Para cada tabela protegida, mostra as regras que existem para ler,
   inserir, atualizar e apagar, e verifica:
   - há regra para cada operação que o código usa?
   - existe atualização permitida sem a leitura correspondente?
   - alguma regra deixa passar tudo, ou não filtra pelo utilizador autenticado?
   - falta a condição de verificação na escrita, aquela que impede gravar linhas
     em nome de outro dono?
3. Chaves com poderes. Procura no código que corre no navegador qualquer uso de
   uma chave administrativa ou de serviço, ou seja, uma chave que ignora todas
   estas regras.
4. Exposição anónima. Diz que tabelas respondem a pedidos de quem não fez login,
   e quais dessas contêm dados pessoais.

Devolve uma tabela: nome | proteção ativa | lacunas por operação | risco descrito
em linguagem simples, sem jargão.

Ordena por gravidade, não pela ordem das tabelas.

As correções vão num bloco separado, marcado como proposta, para eu ler antes de
aplicar seja o que for.

## Como adaptar

O mecanismo muda de nome conforme {{plataforma_dados}}, a pergunta não. Em
Postgres e em serviços construídos sobre ele chama-se segurança ao nível da linha
e vive em políticas por tabela. Em bases de dados de documentos chama-se regras
de segurança e vive num ficheiro de regras. Se a base de dados não tiver
mecanismo nenhum e for acedida só pelo servidor, a proteção equivalente é a
verificação de dono dentro de cada rota, e o template certo passa a ser o SEG-08.

## Porque importa

Muita gente liga a base de dados ao site e assume que está fechada porque é
preciso fazer login para ver as páginas. Não é. A chave que o site entrega ao
navegador chega para falar diretamente com a base de dados, e sem regras por
linha isso significa que qualquer pessoa lê a tabela toda. É a falha mais comum
em projetos feitos depressa, e a mais fácil de explorar.

## Como saber se correu bem

- Nenhuma regra, migração ou ficheiro de configuração foi alterado
- A lista cobre todas as tabelas, incluindo as que ninguém se lembrava que existiam
- Cada tabela desprotegida aparece marcada como crítica
- As lacunas estão separadas por operação, e não resumidas a um sim ou não por tabela
- O risco de cada caso está descrito em linguagem que se percebe sem saber programar
- As correções vieram como proposta por aplicar
