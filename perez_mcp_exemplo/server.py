"""Servidor MCP pequeno: três tools sem rede e sem estado, para exercitar o painel."""

from typing import Literal

from fastmcp import FastMCP

mcp = FastMCP("perez-mcp-exemplo")


@mcp.tool
def somar(a: int, b: int) -> int:
    """Soma dois números inteiros."""
    return a + b


@mcp.tool
def saudar(nome: str, estilo: Literal["simples", "formal", "animado"] = "simples") -> str:
    """Escreve uma saudação para alguém, no estilo escolhido."""
    if estilo == "formal":
        return f"Prezado(a) {nome}, seja bem-vindo(a)."
    if estilo == "animado":
        return f"Oi, {nome}!!! Que bom te ver!"
    return f"Olá, {nome}."


@mcp.tool
def contar_palavras(texto: str, ignorar_vazias: bool = True) -> dict:
    """Conta as palavras de um texto e devolve o total e as cinco mais frequentes."""
    palavras = [p.strip(".,;:!?()[]\"'").lower() for p in texto.split()]
    if ignorar_vazias:
        palavras = [p for p in palavras if p]
    frequencias: dict[str, int] = {}
    for palavra in palavras:
        frequencias[palavra] = frequencias.get(palavra, 0) + 1
    top = sorted(frequencias.items(), key=lambda item: (-item[1], item[0]))[:5]
    return {"total": len(palavras), "distintas": len(frequencias), "mais_frequentes": dict(top)}


def main() -> None:
    """Sobe o servidor falando MCP pelo stdio (o transporte que o Perez OS usa)."""
    mcp.run()


if __name__ == "__main__":
    main()
