---
id: TES-03
nome: Blindar o duplo clique e os cliques repetidos
categoria: testes
nivel: recomendado
modo: execucao
origem: ccp-43
gatilhos:
  - o formulário cria dois registos quando clico depressa
  - apareceram encomendas repetidas
  - se carregar duas vezes acontece duas vezes
  - cobrou duas vezes ao mesmo cliente
  - as pessoas carregam outra vez porque parece que não fez nada
nao_usar_quando:
  - o botão não desencadeia nenhuma ação com consequência
  - o problema é a falta de estados em geral, usar EXP-03
  - a duplicação vem de avisos externos repetidos, usar SEG-11
variaveis:
  - nome: alvo
    descricao: o botão, formulário ou ação em causa
    obrigatoria: true
    omissao: perguntar qual é
  - nome: consequencia
    descricao: o que a ação faz, para se perceber a gravidade da repetição
    obrigatoria: false
    omissao: detetar no código e dizer o que foi encontrado
encadeia_com: [EXP-03, SEG-11, TES-04]
---

## Prompt

Primeiro diagnostica, depois blinda. Não faças as duas coisas ao mesmo tempo.

**Diagnóstico.** Em {{alvo}}, o que acontece se eu clicar duas vezes depressa, ou
clicar outra vez enquanto está a carregar. Responde em concreto sobre
{{consequencia}}: cria dois registos, envia o pedido duas vezes, cobra duas
vezes, envia dois emails. Diz-me também se o problema está no ecrã, no servidor,
ou nos dois.

Espera pela minha confirmação antes de alterares.

**Blindagem.** Depois de eu confirmar:

1. No ecrã, desativa o botão e mostra que está a processar assim que é clicado, e
   reativa quando termina, tanto em caso de sucesso como de erro. Reativar só no
   sucesso deixa o utilizador preso quando falha.
2. No servidor, garante que o mesmo pedido enviado duas vezes só produz efeito
   uma. A proteção do ecrã não chega: quem recarrega a página, tem rede
   instável, ou chama diretamente o servidor, contorna-a.

A segunda parte é a que importa. A primeira é conforto, a segunda é correção.

**Teste.** Mostra-me como verificar isto sem ter de clicar mesmo muito rápido:
enviar o mesmo pedido duas vezes de propósito, ou simular rede lenta. Deixa esse
teste guardado no projeto.

## Porque importa

Toda a gente clica duas vezes, e quem tem rede fraca clica três. Sem proteção do
lado do servidor, isso são registos a dobrar e cobranças repetidas, que é o tipo
de erro que se descobre pela reclamação de um cliente.

## Como saber se correu bem

- O diagnóstico veio antes da alteração e foi confirmado
- A proteção existe no servidor e não apenas no ecrã
- O botão reativa também quando há erro
- Existe forma de testar sem depender da velocidade dos dedos
- O teste ficou guardado no projeto
