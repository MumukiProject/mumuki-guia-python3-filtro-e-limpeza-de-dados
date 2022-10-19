Se quiséssemos substituir as alturas  faltantes pela mediana dessa coluna, faríamos:


```python
arvores["height"].fillna(arvores["height"].median(), inplace=True)
```

Mas o que queremos fazer é substituir as inclinações que faltam pela média. :wink:
