---
id: SEG-16
nome: Limitar as tentativas de entrada
categoria: seguranca
nivel: situacional
modo: diagnostico
origem: ccp-61
gatilhos:
  - alguém pode tentar adivinhar a palavra-passe
  - o login não tem limite de tentativas
  - tenho medo que entrem na conta de um cliente
  - quantas vezes é que se pode falhar a palavra-passe
  - isto tem proteção contra tentativas repetidas
nao_usar_quando:
  - o projeto não tem login próprio e a autenticação é feita por um serviço externo que já limita
  - o site não tem contas de utilizador
  - a preocupação é com outros pontos caros e não com o login, usar SEG-14
variaveis:
  - nome: metodo_login
    descricao: como se entra, palavra-passe, código por email, ou serviço externo
    obrigatoria: false
    omissao: detetar no projeto e dizer o que foi encontrado
encadeia_com: [SEG-14, SEG-15, SEG-04]
---

## Prompt

Só diagnóstico.

Verifica se {{metodo_login}} tem travão a tentativas repetidas.

1. Quantas tentativas falhadas são permitidas, em que intervalo, e o que acontece
   ao ultrapassar: espera, bloqueio da conta, ou nada.
2. O limite conta por conta, por origem do pedido, ou por ambos. Só por conta não
   trava quem experimenta a mesma palavra-passe comum em mil contas diferentes.
   Só por origem não trava quem muda de origem.
3. As mensagens de erro dizem se o email existe. Se a resposta for diferente para
   conta inexistente e para palavra-passe errada, está a entregar-se metade do
   trabalho a quem ataca.
4. O tempo de resposta é diferente nos dois casos. Isso revela a mesma coisa sem
   dizer nada.
5. A recuperação de palavra-passe e o envio de códigos têm o mesmo travão. É
   frequente proteger-se a porta da frente e deixar a das traseiras aberta.

Se faltar o travão, propõe um plano simples: onde entra, que números usar, e o
que a pessoa legítima sente quando se engana três vezes seguidas. Uma proteção que
tranca clientes reais também é um problema.

Não implementes nada.

## Porque importa

Sem limite, adivinhar palavras-passe deixa de exigir sorte e passa a exigir só
tempo de computador, que é barato. E as listas de palavras-passe mais usadas são
públicas, por isso a maioria das contas cai em poucos minutos.

## Como saber se correu bem

- Ficou dito qual é o limite atual, ou que não existe nenhum
- Foi avaliado o limite por conta e por origem
- As mensagens e os tempos de resposta foram verificados quanto a revelarem se a
  conta existe
- A recuperação de palavra-passe foi verificada com o mesmo critério
- O plano proposto considera o incómodo para quem se engana de boa fé
