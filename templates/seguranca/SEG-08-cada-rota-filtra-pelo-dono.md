---
id: SEG-08
nome: Cada pedido confirma que os dados são mesmo daquela pessoa
categoria: seguranca
nivel: situacional
modo: diagnostico
origem: ccp-53
gatilhos:
  - será que um utilizador consegue ver os dados de outro
  - o endereço tem o número da encomenda, isso é seguro
  - se eu mudar o número no link o que acontece
  - cada pessoa só devia ver as suas coisas
  - tenho contas de utilizador e dados separados por pessoa
nao_usar_quando:
  - o projeto não tem contas de utilizador
  - todos os dados são públicos por desenho
  - a pergunta é sobre páginas e não sobre dados, usar SEG-04
variaveis:
  - nome: recursos
    descricao: que tipos de dados pertencem a um utilizador neste projeto
    obrigatoria: false
    omissao: detetar no projeto e listar os que forem encontrados
  - nome: alvo
    descricao: rotas, funções de servidor ou consultas a examinar
    obrigatoria: false
    omissao: examinar tudo o que lê, altera ou apaga dados de utilizador
encadeia_com: [SEG-02, SEG-09, SEG-04]
---

## Prompt

Só diagnóstico, não alteres código.

Percorre {{alvo}} e encontra tudo o que lê, atualiza ou apaga {{recursos}}.

Para cada caso verifica:

1. De onde vem a identificação do recurso: do endereço, do corpo do pedido, dos
   parâmetros. Qualquer uma destas é controlada por quem faz o pedido.
2. Se o código confirma, antes de devolver ou alterar, que aquele recurso
   pertence à pessoa autenticada. Quero ver a comparação explícita entre o dono do
   recurso e a identidade da sessão.
3. Se essa confirmação acontece antes da operação e não depois.

Assume sempre que quem ataca troca a identificação por uma que não é dele. É a
coisa mais fácil de fazer e não precisa de ferramentas nenhumas.

Devolve: ficheiro e linha | operação | como entra a identificação | há
verificação de dono | o que se consegue ver ou alterar se não houver.

Ordena por gravidade.

Não aceites a proteção da base de dados como resposta suficiente. Ela é a segunda
linha e pode estar mal configurada; quero a verificação também aqui, no código.
Onde ela existir, diz que existe, mas continua a marcar a falta da verificação
no código.

Propõe a correção mínima dos três casos mais graves, sem a aplicares.

## Porque importa

Trocar um número no endereço e passar a ver os dados de outra pessoa é uma das
falhas mais comuns em aplicações feitas depressa, e das mais graves, porque não
exige competência nenhuma para ser explorada. Basta curiosidade.

## Como saber se correu bem

- Nenhum ficheiro foi alterado
- Cada caso aparece com ficheiro e linha
- A verificação de dono é procurada no código e não apenas na base de dados
- Cada falha diz em concreto o que se conseguiria alcançar
- As correções vieram propostas, não aplicadas
