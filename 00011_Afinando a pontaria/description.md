:dart: `dropna` também  permite decidir sobre quais colunas queremos fazer a filtragem com o argumento opcional `subset`, da seguinte maneira:

```python
tabela.dropna(subset=[coluna1, coluna2,...])
```

Por exemplo, fazer....

```python
arvores.dropna(subset=["diameter"])
```

... é equivalente a:

```python
arvores[arvores["diameter"].notna()]
```

A vantagem desta opção é que agora podemos eliminar linhas de forma mais seletiva, mantendo aquelas que possuam `nan`s em colunas que não são muito relevantes para nossa análise.

> Teste! ♻️ Volte a executar a célula onde preenchemos o `DataFrame` `arvores`, para restaurá-lo a seu valor original. Em seguida escreva em uma nova célula uma expressão que nos permita obter as  árvores que não tenham `nan` em sua latitude nem em sua longitude.

