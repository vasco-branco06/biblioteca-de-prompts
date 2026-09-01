---
id: EXP-03
nome: Inventário de estados: a carregar, erro, vazio, sucesso
categoria: experiencia
nivel: recomendado
modo: diagnostico
origem: ccp-33
gatilhos:
  - fica um ecrã em branco enquanto carrega
  - quando dá erro não aparece nada
  - o utilizador não sabe se aconteceu alguma coisa
  - a primeira vez que se entra está tudo vazio
  - não sei se tratei todos os casos
nao_usar_quando:
  - o site é estático e não carrega dados nem reage a ações
  - a preocupação é só com o duplo clique, usar TES-03
  - o que se quer é reescrever as mensagens e não inventariar estados, usar EXP-08
variaveis:
  - nome: alvo
    descricao: ecrãs ou componentes a inventariar
    obrigatoria: false
    omissao: percorrer tudo o que carrega dados ou reage a uma ação
encadeia_com: [EXP-08, TES-03, EXP-10]
---

## Prompt

Só diagnóstico. Percorre {{alvo}} e faz o inventário de estados.

Para cada componente que carrega dados ou reage a uma ação, listas, formulários,
botões, pesquisas, envios de ficheiros, diz quais destes estão feitos e quais
faltam:

1. **A carregar.** Com indicação visível de que algo está a acontecer, e não uma
   página em branco.
2. **Erro.** Com mensagem que uma pessoa perceba e com forma de tentar outra vez
   ou sair dali.
3. **Vazio na primeira utilização.** Com indicação do que fazer a seguir, e não
   apenas sem resultados. Este é o mais esquecido de todos e é o primeiro que
   qualquer utilizador novo vê.
4. **Vazio por filtro.** Diferente do anterior: aqui há dados, só não há nenhum
   que corresponda. A mensagem tem de ser outra.
5. **Sucesso.** Com confirmação visível de que aconteceu.
6. **Em processamento.** Com o botão bloqueado, para não ser possível repetir a
   ação enquanto a primeira decorre.

Entrega uma tabela com uma linha por componente e uma coluna por estado, com sim
ou não em cada cruzamento, e para cada não uma linha a dizer o que implementar.

Não implementes nada. Ordena os que faltam por quantas pessoas os vão encontrar:
o vazio da primeira utilização é visto por todos os utilizadores novos, o erro de
rede por poucos.

## Porque importa

Constrói-se quase sempre só o caso em que corre tudo bem, porque é o único que se
testa enquanto se desenvolve. Os outros estados são os que o utilizador real
encontra, e quando faltam ele fica a olhar para um ecrã que não diz nada, sem
saber se esperou pouco ou se partiu alguma coisa.

## Como saber se correu bem

- A tabela cobre todos os componentes que carregam dados
- O vazio da primeira utilização está separado do vazio por filtro
- Cada estado em falta tem descrito o que implementar
- A ordem segue quantas pessoas encontram cada falha
- Nada foi implementado
