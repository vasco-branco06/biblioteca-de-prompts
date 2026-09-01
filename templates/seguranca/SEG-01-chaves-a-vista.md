---
id: SEG-01
nome: Palavras-passe e chaves escritas à vista no código
categoria: seguranca
nivel: essencial
modo: diagnostico
origem: ccp-8
gatilhos:
  - será que tenho palavras-passe no código
  - isto é seguro para publicar
  - colei aqui uma chave e não sei se faz mal
  - antes de pôr isto no GitHub
  - tenho medo de expor as minhas chaves
nao_usar_quando:
  - o que se procura é se a chave já foi para o histórico e já fugiu, usar SEG-03
  - o projeto não usa nenhum serviço externo nem base de dados
variaveis:
  - nome: alvo
    descricao: ficheiros ou pastas a examinar
    obrigatoria: false
    omissao: examinar o projeto inteiro, incluindo ficheiros de configuração e exemplos
encadeia_com: [SEG-03, SEG-02, DIA-03]
---

## Prompt

Só diagnóstico, não corrijas nada e não apagues nada.

Procura em {{alvo}} por segredos escritos diretamente no código ou em ficheiros
que vão parar a sítios públicos: palavras-passe, chaves de acesso a serviços,
tokens, ligações a bases de dados com a senha lá dentro, chaves privadas.

Procura também nos sítios onde as pessoas se esquecem que estão:

- ficheiros de exemplo e de configuração deixados para trás
- comentários com credenciais antigas
- ficheiros de teste e de demonstração
- scripts de arranque e de publicação
- código que é enviado para o navegador, onde qualquer visitante o consegue ler

Devolve uma tabela: ficheiro e linha | que tipo de segredo é | está em código que
chega ao navegador | risco em linguagem simples.

Nunca escrevas o valor do segredo na resposta, nem parte dele. Diz o tipo e onde
está. Se precisares de o identificar, usa os últimos quatro caracteres e mais
nada.

Ordena por gravidade: primeiro o que é público, depois o que dá acesso a dados,
depois o resto.

Para cada caso, diz o que um atacante conseguiria fazer com aquela chave em
concreto.

## Porque importa

Uma chave escrita no código é uma chave que anda com o código, e o código vai
para repositórios, para cópias e para o navegador de quem visita o site. É a
falha mais fácil de cometer e das mais caras, porque quem a encontra tem acesso
imediato ao que ela abre.

## Como saber se correu bem

- Nenhum ficheiro foi alterado
- Nenhum valor de segredo aparece escrito na resposta
- Cada caso tem ficheiro e linha
- Está dito quais chegam ao navegador
- Cada caso diz o que um atacante conseguiria fazer
