# Servidor MCP de exemplo (Perez OS)

Servidor [MCP](https://modelcontextprotocol.io) minúsculo, feito para testar e demonstrar o suporte a MCP do
Perez OS: ao importar este repositório, o painel sobe o servidor num container isolado, lê a lista de tools e
gera um formulário para cada uma.

## Tools

| Tool              | O que faz                                                        |
| ----------------- | ---------------------------------------------------------------- |
| `somar`           | soma dois inteiros                                               |
| `saudar`          | escreve uma saudação (estilo simples, formal ou animado)         |
| `contar_palavras` | conta as palavras de um texto e mostra as cinco mais frequentes  |

## Uso fora do painel

```bash
pip install .
perez-mcp-exemplo   # fala MCP pelo stdio
```
