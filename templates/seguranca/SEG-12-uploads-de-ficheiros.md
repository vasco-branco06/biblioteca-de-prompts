---
id: SEG-12
nome: Ficheiros enviados pelos utilizadores
categoria: seguranca
nivel: situacional
modo: diagnostico
origem: ccp-57
gatilhos:
  - as pessoas podem carregar fotografias
  - tenho uma zona de anexos
  - deixo enviar ficheiros no formulário
  - onde é que ficam guardados os ficheiros que enviam
  - será que alguém pode ver os ficheiros de outra pessoa
nao_usar_quando:
  - o projeto não aceita ficheiros enviados por utilizadores
  - a preocupação é com o tamanho e a velocidade e não com segurança, usar PER-02
variaveis:
  - nome: armazenamento
    descricao: onde ficam os ficheiros e que mecanismo de permissões tem
    obrigatoria: false
    omissao: detetar pela configuração do projeto e dizer o que foi encontrado
  - nome: tipos_aceites
    descricao: que tipos de ficheiro deviam mesmo ser aceites
    obrigatoria: false
    omissao: inferir do uso e declarar a assunção
encadeia_com: [SEG-05, SEG-02, SEG-14]
---

## Prompt

Só diagnóstico. Para cada sítio onde o projeto aceita ficheiros enviados:

**Do lado do servidor**, e não do navegador, verifica:

1. Há limite de tamanho, e o que acontece quando é ultrapassado.
2. O tipo de ficheiro é verificado pelo conteúdo real e não apenas pela extensão
   nem pelo tipo que o próprio pedido declara. Ambos se alteram à mão em
   segundos.
3. O nome do ficheiro é limpo antes de ser usado: sem caminhos relativos, sem
   barras, sem nomes que saiam da pasta prevista.
4. O ficheiro é guardado com um nome gerado pelo sistema, ou com o nome que a
   pessoa escolheu.
5. {{tipos_aceites}} está definido como lista do que entra, e não como lista do
   que se recusa.

**Em {{armazenamento}}**, verifica:

6. Alguma pasta é pública e contém ficheiros que deviam ser privados.
7. As permissões limitam quem lê e quem escreve, por pessoa.
8. Alguém consegue ler o ficheiro de outra pessoa trocando o caminho.

Assume duas tentativas: um ficheiro disfarçado de imagem, e um nome com caminho
relativo lá dentro. Diz o que acontece em cada uma.

Devolve: sítio, ficheiro e linha | validações em falta | pasta pública | o que se
consegue abusar. Não alteres nada.

## Porque importa

Aceitar ficheiros é abrir uma porta para dentro do servidor. O risco não é só o
ficheiro em si; é o nome dele, o sítio onde vai parar, e quem consegue ir lá
buscá-lo depois. Uma pasta pública com anexos privados é uma fuga silenciosa que
ninguém deteta.

## Como saber se correu bem

- Todas as verificações foram avaliadas do lado do servidor
- O tipo do ficheiro é verificado pelo conteúdo e não pela extensão
- Está dito se as pastas de armazenamento são públicas
- Foi testado se se consegue chegar aos ficheiros de outra pessoa
- Nada foi alterado
