---
id: TES-01
nome: Verificação rápida antes de publicar
categoria: testes
nivel: essencial
modo: execucao
origem: ccp-9
gatilhos:
  - quero publicar amanhã
  - vou pôr isto no ar
  - vamos lançar esta semana
  - antes de publicar
  - como é que sei que não parti nada
  - vou lançar isto hoje
nao_usar_quando:
  - o projeto ainda não está publicado nem tem para onde publicar
  - o que se quer é uma bateria de testes completa e não uma verificação rápida, usar TES-02
  - já existe esta verificação e o que falta é corrê-la
variaveis:
  - nome: essencial
    descricao: o que não pode falhar de maneira nenhuma neste projeto
    obrigatoria: false
    omissao: inferir do projeto, listar o que foi assumido, e pedir confirmação antes de escrever
  - nome: forma
    descricao: como se corre a verificação, comando único, lista manual ou automática
    obrigatoria: false
    omissao: escolher a mais simples que o projeto suporte e explicar como se corre
encadeia_com: [TES-02, SEG-01, DIA-03]
---

## Prompt

Cria uma verificação rápida que eu possa correr antes de publicar, que confirme
que {{essencial}} continua a funcionar.

Antes de escreveres, mostra-me a lista do que vais verificar e espera. Se essa
lista estiver errada, a verificação não vale nada.

Regras do que entra:

- Só o que é essencial. Se falhar, não se publica. Tudo o resto fica de fora.
- Tem de correr depressa. Se demorar mais do que dois minutos, ninguém a vai
  correr antes de publicar, e uma verificação que não se corre não existe.
- Tem de dizer com clareza o que falhou e onde, não apenas que falhou.

Inclui pelo menos:

1. A aplicação arranca e a página principal responde.
2. O percurso mais importante funciona de ponta a ponta.
3. A ligação à base de dados e aos serviços externos está de pé.
4. As variáveis de configuração necessárias existem no destino.
5. Não há segredos expostos no que vai ser publicado.

Entrega em {{forma}}, com instruções de como a correr em uma linha, e diz-me
onde a guardaste.

Corre-a uma vez à minha frente e mostra o resultado.

## Porque importa

Publicar é o momento em que os erros deixam de ser problema teu e passam a ser
problema de quem usa. Dois minutos de verificação apanham quase sempre a
configuração esquecida, que é a causa mais comum de um lançamento correr mal.

## Como saber se correu bem

- A lista do que se verifica foi aprovada antes de ser escrita
- A verificação corre em menos de dois minutos
- As mensagens de falha dizem o que falhou e onde
- Corre com um comando ou passo único
- Foi corrida uma vez e o resultado foi mostrado
