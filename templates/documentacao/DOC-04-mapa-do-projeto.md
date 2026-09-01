---
id: DOC-04
nome: O mapa do projeto, para quem chega sem memória
categoria: documentacao
nivel: situacional
modo: execucao
origem: ccp-70
gatilhos:
  - já não sei onde está cada coisa
  - explica-me como o projeto está organizado
  - preciso de um mapa disto
  - a IA anda perdida no meu projeto
  - onde é que fica cada parte
nao_usar_quando:
  - o projeto tem meia dúzia de ficheiros e vê-se de uma vez
  - o que se quer são as regras e decisões e não a estrutura, usar DOC-02
  - o documento é para quem vai instalar e usar, usar DOC-05
variaveis:
  - nome: ficheiro_mapa
    descricao: onde fica o mapa
    obrigatoria: false
    omissao: ARCHITECTURE.md na raiz do projeto
encadeia_com: [DOC-02, PER-10, DOC-05]
---

## Prompt

Explora o projeto e escreve {{ficheiro_mapa}}, com uma página no máximo.

Explica:

1. As pastas principais e o que cada uma faz. Uma linha por pasta.
2. O caminho que um pedido do utilizador percorre desde o clique até aos dados e
   de volta. Este é o ponto mais importante do documento: é o que orienta quem
   nunca viu isto.
3. Onde ficam as regras de negócio, ou seja, as decisões próprias deste projeto,
   por oposição ao que é montagem comum a qualquer aplicação.
4. Três a cinco convenções que este projeto segue, observadas no código e não
   inventadas.
5. Os sítios onde é preciso ter cuidado: partes frágeis, dependências entre
   coisas que não parecem ligadas, código que tem de mudar em conjunto.

Escreve para alguém que nunca viu o projeto, ou para ti próprio numa próxima
sessão sem memória nenhuma disto.

Não descrevas ficheiro a ficheiro. Descreve o mapa mental. Uma lista de ficheiros
com uma frase cada é inútil e desatualiza-se na semana seguinte.

Se encontrares partes do projeto cuja função não conseguires perceber, escreve
isso no documento em vez de inventares uma explicação plausível.

## Porque importa

Uma IA começa cada sessão sem se lembrar de nada, e por isso reinventa coisas que
já existem, no sítio errado. Um mapa curto lido no início corrige a maior parte
desses enganos, e serve igualmente a qualquer pessoa que chegue de novo.

## Como saber se correu bem

- Cabe numa página
- O caminho de um pedido está descrito de ponta a ponta
- As convenções foram observadas no código e não presumidas
- Não é uma lista de ficheiros
- As partes incompreendidas foram assinaladas em vez de inventadas
