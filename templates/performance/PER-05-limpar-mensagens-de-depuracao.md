---
id: PER-05
nome: Limpar mensagens de depuração esquecidas
categoria: performance
nivel: recomendado
modo: execucao
origem: ccp-41
gatilhos:
  - ficaram aqui mensagens de teste
  - a consola está cheia de coisas
  - antes de publicar quero limpar isto
  - tenho prints espalhados pelo código
  - deixei coisas de depuração no código
nao_usar_quando:
  - as mensagens fazem parte do registo permanente do sistema, e aí não são lixo
  - estamos a meio de uma investigação que depende delas, terminar DIA-05 primeiro
variaveis:
  - nome: alvo
    descricao: onde procurar
    obrigatoria: false
    omissao: procurar no projeto inteiro
encadeia_com: [DIA-05, PER-04, SEG-15]
---

## Prompt

Procura em {{alvo}} mensagens de depuração e restos de teste esquecidos no
código.

Mostra-me a lista antes de apagar, com ficheiro, linha e o que a mensagem
escreve.

Separa em três grupos, porque não são todos lixo:

1. **Lixo.** Mensagens temporárias, contadores, marcações de passagem, valores
   impressos para se perceber o que estava a acontecer.
2. **Registo a sério.** Mensagens que fazem parte do funcionamento normal e que
   alguém vai querer ler quando houver um problema em produção. Estas ficam.
3. **Perigosas.** Mensagens que escrevem dados pessoais, credenciais, conteúdos
   de pedidos ou identificadores internos. Estas saem primeiro, e são também um
   problema de segurança, não só de limpeza.

Marca também qualquer código de teste que tenha ficado ativo: valores fixos para
experimentar, verificações desligadas, atalhos que saltam a autenticação, dados
de exemplo.

Espera pela minha confirmação e só depois apagas. No fim, mostra o que foi
removido e confirma que a aplicação continua a arrancar.

## Porque importa

O que se escreve para perceber um problema fica no código muito depois de o
problema estar resolvido. Além de sujar, algumas destas mensagens escrevem em
registos coisas que nunca deviam lá estar, e ficam a acumular durante meses sem
ninguém reparar.

## Como saber se correu bem

- A lista foi mostrada antes de qualquer remoção
- As mensagens de registo permanente foram poupadas
- As que escrevem dados sensíveis foram assinaladas como risco de segurança
- Os atalhos de teste ainda ativos foram encontrados
- A aplicação continua a arrancar depois da limpeza
