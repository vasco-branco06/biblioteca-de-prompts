---
id: EXP-07
nome: Auditoria de acessibilidade
categoria: experiencia
nivel: situacional
modo: diagnostico
origem: ccp-62
gatilhos:
  - isto é acessível
  - uma pessoa que não veja consegue usar isto
  - o texto está muito claro e não se lê
  - só se consegue usar com rato
  - preciso de cumprir as regras de acessibilidade
nao_usar_quando:
  - o problema é a legibilidade estética e não a acessibilidade, usar EXP-02
  - a interface ainda está em rascunho e vai mudar toda
variaveis:
  - nome: nivel
    descricao: o nível das normas a exigir
    obrigatoria: false
    omissao: usar WCAG 2.2 nível AA, que é o exigido na maioria dos contextos
  - nome: alvo
    descricao: páginas ou componentes a auditar
    obrigatoria: false
    omissao: auditar o percurso principal e todos os formulários
encadeia_com: [EXP-02, EXP-04, EXP-08]
---

## Prompt

Só diagnóstico. Audita {{alvo}} segundo {{nivel}} e reporta cada problema com o
ficheiro e a linha.

1. **Contraste.** Lista cada par de cor de texto e fundo que falha o rácio
   mínimo, e o mesmo para elementos com que se interage. Dá o valor atual e uma
   cor corrigida que mantenha a aparência o mais próxima possível.
2. **Teclado.** Consegue chegar-se a tudo com a tecla de tabulação, a ordem é
   lógica, e vê-se onde está o foco em cada momento. Marca qualquer sítio onde o
   foco fique invisível ou preso.
3. **Leitura em voz alta.** Imagens sem descrição alternativa, botões e ícones
   sem texto legível por um leitor de ecrã, campos sem etiqueta associada, avisos
   que aparecem sem serem anunciados.
4. **Estrutura.** Os títulos seguem uma hierarquia sem saltos, e as zonas da
   página estão identificadas.
5. **Cor sozinha.** Alguma informação é transmitida apenas pela cor, sem texto
   nem símbolo que a acompanhe.
6. **Movimento.** Existe animação que não pode ser desligada por quem tem essa
   preferência configurada.

Entrega uma tabela: problema | ficheiro e linha | critério | correção.

Não alteres nada. Marca à parte os problemas que precisam de decisão de desenho e
não têm correção mecânica.

## Porque importa

Acessibilidade é o que decide se uma parte das pessoas consegue ou não usar o
site: quem vê mal, quem não distingue cores, quem não usa rato. Em muitos
contextos é também obrigação legal. E quase tudo o que se corrige aqui melhora a
experiência de toda a gente.

## Como saber se correu bem

- Cada problema tem ficheiro e linha, e não um aviso genérico
- Os contrastes falhados vêm com o valor atual e a cor corrigida
- A navegação por teclado foi percorrida de facto e não presumida
- Os problemas que exigem decisão de desenho estão separados
- Nada foi alterado
