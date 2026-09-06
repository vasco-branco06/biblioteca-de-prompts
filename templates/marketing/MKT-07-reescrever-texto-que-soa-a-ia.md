---
id: MKT-07
nome: Reescrever texto que soa a gerado por IA
categoria: marketing
nivel: recomendado
modo: execucao
origem: novo
gatilhos:
  - isto soa a escrito por IA
  - o texto está correto mas não parece meu
  - parece que foi tudo gerado
  - quero que isto soe a pessoa
  - este texto não tem voz nenhuma
nao_usar_quando:
  - o problema é o desenho da página e não o texto, usar EXP-05
  - o texto é de interface e não prosa, usar EXP-08
  - o texto está factualmente errado, e aí corrige-se o conteúdo primeiro
variaveis:
  - nome: texto
    descricao: o que reescrever
    obrigatoria: true
    omissao: perguntar
  - nome: voz
    descricao: como quem escreve fala, com exemplos se existirem
    obrigatoria: false
    omissao: perguntar por dois ou três textos que a pessoa tenha escrito, e na falta deles assumir tom direto e sem cerimónia
  - nome: publico
    descricao: quem lê
    obrigatoria: false
    omissao: inferir do texto e declarar a assunção
encadeia_com: [EXP-05, EXP-08, MKT-02]
---

## Prompt

Reescreve {{texto}} para {{publico}}, na voz de {{voz}}, sem mudar o que ele diz.

Primeiro, marca no original os sinais de escrita automática. Procura estes, que
são os que aparecem quase sempre:

- Contraste binário a fingir profundidade, do género não é isto, é aquilo.
- Aberturas a limpar a garganta, que anunciam o assunto antes de o tratar.
- Revelações a seguir a dois pontos, usadas como efeito.
- Grupos de três, quando dois chegavam e o terceiro só existe pelo ritmo.
- Finais a subir de tom, com uma conclusão grandiosa que não acrescenta nada.
- Travessões usados como decoração em vez de pontuação.
- Frases todas do mesmo comprimento, uma atrás da outra.
- Superlativos vazios: poderoso, robusto, incrível, transformador.
- Palavras de registo importado: aprofundar, alavancar, potenciar, entregar valor.
- Ressalvas a mais, a proteger-se de tudo antes de afirmar seja o que for.

Depois reescreve, com estas regras:

1. Mantém o significado e os factos. Isto é reescrita, não edição de conteúdo.
2. Varia o comprimento das frases. Uma curta a seguir a uma longa faz mais pela
   naturalidade do que qualquer palavra escolhida a dedo.
3. Corta adjetivos e devolve concreto. Uma solução robusta não diz nada; aguenta
   mil pedidos por minuto diz.
4. Usa as palavras que a pessoa usaria a falar. Se não dissesse aquilo em voz
   alta, não escreve.
5. Deixa as frases irem direitas ao assunto. A primeira frase trata do tema.

Entrega em duas partes: o texto reescrito, e uma lista curta do que mudaste e
porquê. Quero perceber o padrão para o corrigir sozinho da próxima vez.

Se {{texto}} já estiver bem escrito, diz isso e não mexas. Reescrever um texto
que já tem voz própria estraga-o.

## Porque importa

As pessoas já reconhecem esta escrita, mesmo sem saberem nomear o que a
denuncia, e o efeito é de desconfiança. O problema não é a gramática, que está
sempre certa; é o ritmo uniforme e a ausência de alguém do outro lado.

## Como saber se correu bem

- Os sinais foram marcados no original antes da reescrita
- O significado e os factos mantiveram-se
- As frases têm comprimentos variados
- Os adjetivos vagos foram trocados por informação concreta
- Existe a lista do que mudou e porquê
