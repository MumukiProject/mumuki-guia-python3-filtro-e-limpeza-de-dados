Para obter todos os salgueiros, devemos nos certificar de que o nome _comum_ (`comm_name`) da nossa árvore comece com a string `"Sauce"`. Tenha cuidado com a sintaxe específica desta expressão:

```python
tabela[tabela[coluna].str.startswith(string_começo)]
```
