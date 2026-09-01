---
id: EXP-05
nome: Deixar de parecer feito por IA
categoria: experiencia
nivel: recomendado
modo: diagnostico
origem: ccp-35
gatilhos:
  - isto parece um template
  - está funcional mas sem alma
  - parece igual a todos os sites
  - percebe-se logo que foi feito por IA
  - quero que isto tenha personalidade
nao_usar_quando:
  - o que está mal é a legibilidade ou a usabilidade e não o carácter, usar EXP-02
  - o projeto tem manual de marca definido e a questão é cumpri-lo, usar EXP-09
  - o texto é que soa a gerado, e não o desenho, usar MKT-07
variaveis:
  - nome: pagina
    descricao: o que avaliar
    obrigatoria: false
    omissao: avaliar as páginas visíveis ao público
  - nome: personalidade
    descricao: como a marca ou o projeto quer ser visto
    obrigatoria: false
    omissao: perguntar, porque sem isto as alternativas saem tão genéricas como o problema
encadeia_com: [EXP-02, EXP-09, MKT-07]
---

## Prompt

Só diagnóstico. Aponta em {{pagina}} os sinais de molde genérico:

- secção de topo seguida de três cartões e testemunhos, sempre pela mesma ordem
- gradientes em tons de roxo ou azul por defeito
- ícones todos do mesmo conjunto, colocados sem intenção, um por cartão
- espaçamentos uniformes do princípio ao fim, sem ritmo nem variação
- texto de exemplo vazio, do género transforme o seu negócio ou soluções
  inovadoras
- fotografias de banco de imagens reconhecíveis
- tudo centrado, tudo simétrico, tudo com a mesma largura

Para cada sinal encontrado, propõe uma alternativa concreta alinhada com
{{personalidade}}: uma decisão de disposição inesperada, uma escolha tipográfica
com carácter, um detalhe próprio, uma assimetria com intenção, uma cor que não
esteja na paleta óbvia.

Não me digas para tornar mais moderno nem mais limpo. Diz o que um designer
faria: que tipo de letra, que tamanho, que quebra de grelha, que elemento
sacrificar para outro respirar.

Marca à parte as escolhas genéricas que devem ficar como estão por serem
convenções úteis. Um menu no topo é previsível porque funciona, e mudar isso
custa usabilidade sem ganhar nada.

Não alteres ficheiros.

## Porque importa

Quando se pede um site a uma ferramenta de IA sem direção, sai sempre a mesma
disposição, e as pessoas já reconhecem esse ar sem conseguirem explicar porquê. O
efeito é de desconfiança: parece uma página montada à pressa, não um produto de
alguém que se importa.

## Como saber se correu bem

- Cada sinal aparece com o sítio onde está
- Cada alternativa é uma decisão concreta e não um adjetivo
- As propostas estão ligadas à personalidade pretendida
- As convenções úteis ficaram assinaladas para não serem mexidas
- Nada foi alterado
