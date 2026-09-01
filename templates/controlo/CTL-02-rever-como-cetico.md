---
id: CTL-02
nome: Rever o próprio trabalho com olhos de cético
categoria: controlo
nivel: essencial
modo: execucao
origem: ccp-5
gatilhos:
  - revê o que acabaste de fazer
  - será que isso está mesmo bem
  - dá uma vista de olhos crítica a isso
  - antes de eu dar por bom
  - vê se não deixaste nada mal feito
nao_usar_quando:
  - o trabalho ainda não terminou
  - o que se procura é uma auditoria de segurança, usar SEG-07
  - a revisão é de um plano e não de código, usar PLA-07
variaveis:
  - nome: alvo
    descricao: o que rever
    obrigatoria: false
    omissao: rever o trabalho feito nesta sessão e dizer o que foi incluído
encadeia_com: [CTL-01, PLA-07, SEG-07]
---

## Prompt

Esquece que foste tu a escrever {{alvo}}. Revê-o como um programador experiente e
desconfiado, que não tem nada a defender.

Procura, por esta ordem:

1. **Erros.** Coisas que simplesmente não fazem o que deviam.
2. **Situações não previstas.** O que acontece com valores vazios, nulos, muito
   grandes, ou quando uma chamada externa falha a meio.
3. **Complicação desnecessária.** Sítios onde a solução é mais elaborada do que o
   problema exige.
4. **Inconsistências.** Onde este código faz as coisas de maneira diferente do
   resto do projeto.
5. **O que ficou por fazer e não foi dito.** Atalhos, casos deixados de fora,
   coisas assumidas em silêncio.

Lista os problemas do mais grave para o menos grave, e diz em cada um o que
acontece na prática se não for corrigido.

Corrige apenas os críticos, ou seja, aqueles que fazem a aplicação comportar-se
mal. Antes de corrigires, mostra-me a lista e diz quais vais corrigir.

Não corrijas os de estilo nem os de gosto. Esses ficam na lista para eu decidir.

Se não encontrares nada de grave, diz isso em vez de inventares problemas para
parecer diligente. Uma revisão que devolve sempre cinco problemas deixa de ter
significado.

## Porque importa

Quem escreve no impulso não vê os próprios erros, e isso vale para pessoas e para
ferramentas de IA. Reler com uma postura diferente, à procura de defeitos em vez
de à procura de terminar, encontra coisas que passaram despercebidas minutos
antes.

## Como saber se correu bem

- Os problemas estão ordenados por gravidade
- Cada um diz o que acontece na prática se não for corrigido
- A lista foi mostrada antes de qualquer correção
- Só os críticos foram corrigidos
- Se não havia nada de grave, foi dito, sem problemas inventados
