#!/usr/bin/env python3
"""Reconstroi o indice do SKILL.md a partir do frontmatter dos templates.

O indice nunca se escreve a mao. Correr este script sempre que se acrescenta,
remove ou altera um template:

    python ferramentas/gerar_indice.py

Le todos os .md em templates/, extrai id, nome, gatilhos e modo, e reescreve a
tabela entre os marcadores do SKILL.md. Nao toca em mais nada do ficheiro.
"""
import pathlib
import re
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
SKILL = RAIZ / "SKILL.md"
TEMPLATES = RAIZ / "templates"

INICIO = "<!-- INICIO INDICE. Gerado por ferramentas/gerar_indice.py. Nao editar a mao. -->"
FIM_MARCA = "<!-- FIM INDICE -->"

# Ordem das categorias no indice, para as de codigo virem antes das restantes.
ORDEM = ["PLA", "DIA", "SEG", "EXP", "PER", "TES", "DOC", "CTL", "MKT", "EST", "DAD"]


def campo(frontmatter, nome):
    achado = re.search(r"^" + nome + r": (.+)$", frontmatter, re.M)
    return achado.group(1).strip() if achado else ""


def lista(frontmatter, nome, campo_seguinte):
    bloco = frontmatter.split("\n" + nome + ":")[1].split("\n" + campo_seguinte + ":")[0]
    return [l.strip()[2:].strip() for l in bloco.splitlines() if l.strip().startswith("- ")]


def limpar(texto):
    """Barras verticais partiriam a tabela markdown."""
    return texto.replace("|", "/")


def main():
    linhas = []
    for ficheiro in sorted(TEMPLATES.rglob("*.md")):
        texto = ficheiro.read_text(encoding="utf-8")
        if not texto.startswith("---"):
            sys.exit("sem frontmatter: " + str(ficheiro))
        frontmatter = texto.split("---")[1]
        identificador = campo(frontmatter, "id")
        if not identificador:
            sys.exit("sem id: " + str(ficheiro))
        gatilhos = lista(frontmatter, "gatilhos", "nao_usar_quando")
        if not gatilhos:
            sys.exit("sem gatilhos: " + str(ficheiro))
        linhas.append((
            identificador,
            limpar(campo(frontmatter, "nome")),
            "; ".join(limpar(g) for g in gatilhos),
            campo(frontmatter, "modo"),
        ))

    def chave(linha):
        prefixo = linha[0][:3]
        return (ORDEM.index(prefixo) if prefixo in ORDEM else 99, linha[0])

    linhas.sort(key=chave)

    tabela = ["| ID | Nome | Quando usar | Modo |", "|----|------|-------------|------|"]
    tabela += ["| %s | %s | %s | %s |" % linha for linha in linhas]

    texto = SKILL.read_text(encoding="utf-8")
    if INICIO not in texto or FIM_MARCA not in texto:
        sys.exit("marcadores do indice nao encontrados no SKILL.md")

    antes = texto.split(INICIO)[0]
    depois = texto.split(FIM_MARCA)[1]
    SKILL.write_text(
        antes + INICIO + "\n\n" + "\n".join(tabela) + "\n\n" + FIM_MARCA + depois,
        encoding="utf-8",
    )
    print("indice reescrito com %d templates" % len(linhas))


if __name__ == "__main__":
    main()
