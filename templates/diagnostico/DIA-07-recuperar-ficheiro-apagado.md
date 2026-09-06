---
id: DIA-07
nome: Recuperar um ficheiro apagado
categoria: diagnostico
nivel: situacional
modo: execucao
origem: ccp-49
gatilhos:
  - apaguei um ficheiro sem querer
  - desapareceu um ficheiro
  - onde é que foi parar aquele ficheiro
  - apaguei sem querer a pasta errada
  - preciso de recuperar uma coisa que apaguei
nao_usar_quando:
  - o ficheiro nunca chegou a ser guardado no histórico do projeto
  - o que se quer é anular alterações e não recuperar um ficheiro, usar DIA-04
  - o ficheiro apagado é gerado automaticamente e volta a nascer sozinho
variaveis:
  - nome: ficheiro
    descricao: nome ou parte do nome do que desapareceu
    obrigatoria: false
    omissao: perguntar, e se não houver nome, procurar o que desapareceu desde o último ponto guardado
encadeia_com: [DIA-04, CTL-03]
---

## Prompt

{{ficheiro}} foi apagado. Vê se está no histórico do projeto.

1. Procura no histórico e diz-me se existe, em que ponto foi visto pela última
   vez, e com que tamanho.
2. Se existirem várias versões, lista-as com a data e deixa-me escolher qual.
3. Mostra-me o que vais restaurar antes de restaurares, e para onde. Se já existir
   um ficheiro com esse nome, não o substituas: avisa-me e pergunta.
4. Só depois do meu OK é que escreves.

Se o ficheiro não estiver no histórico, diz isso e para. Não escrevas uma versão
aproximada nem reconstruas o conteúdo de memória. Um ficheiro inventado com o
nome certo é pior do que nenhum ficheiro, porque parece recuperado.

Se não estiver no histórico, diz-me antes de desistirmos que outros sítios vale a
pena procurar: reciclagem do sistema, cópias do editor, versões de cópia de
segurança automática.

## Porque importa

Quase tudo o que foi guardado alguma vez continua no histórico do projeto, mesmo
depois de apagado do disco. O risco aqui não é não recuperar, é receber uma
reconstrução inventada e só descobrir isso semanas depois.

## Como saber se correu bem

- Foi dito onde e quando o ficheiro foi visto pela última vez
- Havendo várias versões, pude escolher
- Nada foi substituído sem autorização
- Não havendo no histórico, ficou dito com clareza em vez de reconstruído
- O conteúdo restaurado veio do histórico, não da memória do modelo
