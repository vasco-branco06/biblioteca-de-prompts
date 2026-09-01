---
id: PER-11
nome: Bibliotecas instaladas que ninguém usa
categoria: performance
nivel: situacional
modo: diagnostico
origem: ccp-72
gatilhos:
  - devo ter aqui coisas instaladas que já não uso
  - a lista de dependências está enorme
  - instalei coisas para experimentar e ficaram
  - quero limpar as bibliotecas
  - isto precisa de tantas dependências assim
nao_usar_quando:
  - o que se procura são bibliotecas com falhas de segurança, usar SEG-06
  - o que se procura é código próprio não usado, usar PER-04
variaveis:
  - nome: gestor
    descricao: o gestor de pacotes do projeto
    obrigatoria: false
    omissao: detetar pelos ficheiros de dependências
encadeia_com: [SEG-06, PER-04, PER-07]
---

## Prompt

Só diagnóstico. Verifica que bibliotecas estão instaladas em {{gestor}} e não são
usadas em lado nenhum.

Para cada uma, diz:

- se é usada em código, em configuração, ou em nenhum sítio
- se é usada apenas durante o desenvolvimento ou também em produção
- se foi instalada diretamente ou veio arrastada por outra
- quanto pesa, se for uma que chega ao navegador

Verifica antes de a dares como não usada:

1. Ficheiros de configuração, que muitas vezes referem bibliotecas sem as
   importar no código.
2. Extensões e complementos de outras ferramentas.
3. Uso indireto, por convenção, sem importação explícita.
4. Scripts de arranque, de construção e de publicação.

Separa em três listas: não usada com certeza, usada só em configuração, e
incerta. Não removas nada.

Para as certas, diz o que se ganha em remover: peso, tempo de instalação, e menos
uma peça a poder trazer problemas de segurança no futuro.

## Porque importa

Cada biblioteca instalada é código de outra pessoa que entra no projeto, e
continua a contar como superfície de risco mesmo que nunca seja chamada. As que
sobraram de experiências ficam lá anos porque ninguém tem a certeza se podem sair.

## Como saber se correu bem

- Nada foi removido
- Os quatro sítios onde uma biblioteca pode ser usada sem importação foram
  verificados
- Existem três listas separadas por certeza
- Está distinguido o que é usado só em desenvolvimento
- Cada remoção proposta diz o que se ganha
