---
id: DOC-05
nome: README para quem chega novo
categoria: documentacao
nivel: situacional
modo: execucao
origem: ccp-77
gatilhos:
  - preciso de um readme
  - quero partilhar isto com alguém
  - como é que outra pessoa põe isto a funcionar
  - vou pôr isto no GitHub
  - falta a documentação inicial
nao_usar_quando:
  - o documento é para a IA e não para pessoas, usar DOC-02
  - o que falta é explicar a organização interna, usar DOC-04
  - o projeto ainda não faz nada de útil
variaveis:
  - nome: publico
    descricao: quem vai ler, um colega, um cliente, ou eu próprio daqui a meses
    obrigatoria: false
    omissao: assumir alguém que nunca viu o projeto e sabe pouco de programação
encadeia_com: [DOC-04, DOC-02, TES-01]
---

## Prompt

Escreve um README para {{publico}}, para quem nunca viu este projeto.

Estrutura:

1. **O que isto faz**, em duas ou três frases, do ponto de vista de quem usa e
   não de quem construiu. Sem termos técnicos.
2. **Para quem serve** e que problema resolve.
3. **Como pôr a funcionar.** Passos numerados, com os comandos exatos, incluindo
   o que é preciso ter instalado antes. Diz o que se deve ver quando cada passo
   corre bem.
4. **Configuração necessária.** Que variáveis são precisas e onde se obtêm.
   Nunca escrevas valores reais, nem sequer como exemplo. Usa marcadores.
5. **Como correr os testes**, se existirem.
6. **Problemas comuns na instalação** e como se resolvem.
7. **Onde ficam as coisas**, em três ou quatro linhas, com remissão para o mapa
   do projeto se existir.

Linguagem clara, sem assumir conhecimento. Cada comando deve poder ser copiado e
colado tal como está.

Testa mentalmente o passo a passo como se fosses uma pessoa que acabou de
descarregar isto para um computador limpo. Se algum passo depender de coisa que
só existe no meu computador, isso é um defeito das instruções: assinala-o.

Não incluas secções vazias por convenção, como licença ou contribuições, se elas
não se aplicarem.

## Porque importa

O README é a primeira coisa que alguém lê, e é o que decide se consegue arrancar
sozinho ou se desiste. A pessoa mais provável de o ler és tu próprio daqui a três
meses, sem te lembrares de nada.

## Como saber se correu bem

- O que o projeto faz está descrito sem termos técnicos
- Os passos de instalação são copiáveis e dizem o que se deve ver
- Nenhum valor real de configuração aparece escrito
- As dependências do computador de origem foram assinaladas
- Não há secções vazias postas por hábito
