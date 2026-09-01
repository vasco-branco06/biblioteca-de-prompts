---
id: SEG-03
nome: Os segredos já fugiram, e agora
categoria: seguranca
nivel: recomendado
modo: diagnostico
origem: ccp-26
gatilhos:
  - acho que já enviei uma chave para o GitHub
  - apaguei a chave do ficheiro, já está resolvido
  - tinha um ficheiro de configuração no repositório
  - o repositório era público
  - isto pode ter escapado alguma coisa
nao_usar_quando:
  - o projeto não tem histórico de alterações guardado
  - a procura é só pelos ficheiros de agora, usar SEG-01
  - o projeto nunca saiu do computador e nunca foi partilhado
variaveis:
  - nome: prefixo_publico
    descricao: a marca que faz uma variável ser enviada para o navegador nesta stack
    obrigatoria: false
    omissao: detetar pela stack do projeto e dizer qual é
  - nome: servicos
    descricao: que serviços externos o projeto usa, para saber que formatos de chave procurar
    obrigatoria: false
    omissao: detetar pelas dependências e configuração
encadeia_com: [SEG-01, SEG-02, SEG-14]
---

## Prompt

Só diagnóstico, em três frentes. Não alteres ficheiros nem reescrevas histórico.

**Histórico.** Procura em todos os pontos guardados, e não apenas nos ficheiros
de agora, por segredos que alguma vez tenham sido gravados: ficheiros de
configuração, chaves de {{servicos}}, tokens, ligações a bases de dados com senha.
Diz-me em que ponto do histórico e em que ficheiro.

Regra que muda tudo: se um segredo esteve alguma vez no histórico, apagá-lo agora
não resolve. Ele continua lá e continua legível para quem tenha uma cópia. Tem de
ser trocado no serviço que o emitiu. Marca claramente quais têm de ser trocados.

**Navegador.** Procura variáveis marcadas com {{prefixo_publico}} que contenham
coisas que só deviam existir no servidor, e qualquer segredo importado por código
que corre no navegador.

**Prevenção.** Confirma se os ficheiros de configuração com segredos estão
excluídos do controlo de versões, e se essa exclusão foi feita antes ou depois de
já terem sido gravados.

Devolve uma lista ordenada: segredo | onde está | já saiu para fora | trocar sim
ou não | o que fazer primeiro.

Não escrevas o valor de nenhum segredo. Identifica-os pelo tipo e pelo sítio.

## Porque importa

Muita gente apaga a chave do ficheiro, vê que já não aparece, e fica descansada.
O histórico guarda tudo o que alguma vez lá esteve, e é a primeira coisa que
alguém consulta. A única correção real é trocar a chave no serviço.

## Como saber se correu bem

- A procura cobriu o histórico e não só os ficheiros atuais
- Cada segredo encontrado diz se tem de ser trocado
- Nenhum valor de segredo aparece escrito
- Ficou claro o que está exposto ao navegador
- Nada foi alterado nem o histórico reescrito
