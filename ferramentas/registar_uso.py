#!/usr/bin/env python3
"""Acrescenta uma linha ao registo de utilizacoes.

    python ferramentas/registar_uso.py SEG-10 --resumo "auditoria ao formulario" --resultado bom

Acrescenta sempre, nunca reescreve o ficheiro. Escreve com o marcador de
codificacao a primeira vez, para o registo abrir no Excel com os acentos certos
e sem tratamento nenhum.
"""
import argparse
import csv
import datetime
import pathlib
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
REGISTO = RAIZ / "registo" / "uso.csv"
TEMPLATES = RAIZ / "templates"

CABECALHO = ["data_hora", "id_template", "superficie", "projeto", "pedido_resumo", "resultado"]
SUPERFICIES = ["claude-code", "cowork"]
RESULTADOS = ["bom", "mau", "nao_avaliado"]


def ids_conhecidos():
    """Os ids vem do inicio do nome do ficheiro, que e igual ao campo id."""
    return {"-".join(f.stem.split("-")[:2]) for f in TEMPLATES.rglob("*.md")}


def main():
    parser = argparse.ArgumentParser(description="Acrescenta uma linha ao registo de utilizacoes.")
    parser.add_argument("id_template", help="ID do template usado, por exemplo SEG-10")
    parser.add_argument("--resumo", default="", help="o pedido em poucas palavras")
    parser.add_argument("--projeto", default=pathlib.Path.cwd().name, help="onde foi usado")
    parser.add_argument("--superficie", default="claude-code", choices=SUPERFICIES)
    parser.add_argument("--resultado", default="nao_avaliado", choices=RESULTADOS)
    parser.add_argument("--data", default=None, help="ISO 8601; por omissao, agora")
    parser.add_argument("--ficheiro", default=None, help="outro registo, para testes")
    args = parser.parse_args()

    identificador = args.id_template.upper()
    conhecidos = ids_conhecidos()
    if identificador not in conhecidos:
        mesma_categoria = sorted(i for i in conhecidos if i[:3] == identificador[:3])
        sys.exit(
            "id desconhecido: %s\nna categoria %s existem: %s"
            % (identificador, identificador[:3], ", ".join(mesma_categoria) or "nenhum")
        )

    data = args.data or datetime.datetime.now().isoformat(timespec="seconds")
    destino = pathlib.Path(args.ficheiro) if args.ficheiro else REGISTO
    destino.parent.mkdir(parents=True, exist_ok=True)

    primeira_vez = not destino.exists() or destino.stat().st_size == 0
    codificacao = "utf-8-sig" if primeira_vez else "utf-8"

    with open(destino, "a", newline="", encoding=codificacao) as ficheiro:
        escritor = csv.writer(ficheiro)
        if primeira_vez:
            escritor.writerow(CABECALHO)
        escritor.writerow([data, identificador, args.superficie, args.projeto, args.resumo, args.resultado])

    print("registado: %s em %s (%s)" % (identificador, args.projeto, args.resultado))


if __name__ == "__main__":
    main()
