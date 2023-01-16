Se quiséssemos saber quais as árvores que estão nos bairros Floresta e Recoleta, poderíamos tentar fazer:

```python
arvores[(arvores["neighbourhood"] == "FLORESTA") | (arvores["neighbourhood"] == "RECOLETA")]
```

E talvez não pareça tão sério. Mas o que acontece se queremos as árvores da Floresta, Recoleta, Belgrano e Nuñez? Embora poderíamos fazer isso...


```python
arvores[
  (arvores["neighbourhood"] == "FLORESTA") | 
  (arvores["neighbourhood"] == "RECOLETA") | 
  (arvores["neighbourhood"] == "BELGRANO") | 
  (arvores["neighbourhood"] == "NUÑEZ")
]
```

... não parece o melhor caminho, não é? 🙄

Felizmente, existe o `isin` que pode nos poupar muito tempo ⌚. Para obter o resultado anterior, poderíamos simplesmente fazer:


```python
arvores[arvores["neighbourhood"].isin(["FLORESTA", "RECOLETA", "BELGRANO", "NUÑEZ"])]
```

> Não acredita? Verifique em seu caderno que as seguintes expressões retornam os mesmos resultados...
>
> ```python
> arvores[(arvores["neighbourhood"] == "FLORESTA") | (arvores["neighbourhood"] == "RECOLETA") | (arvores["neighbourhood"] == "BELGRANO") | (arvores["neighbourhood"] == "NUÑEZ")]
> arvores[arvores["neighbourhood"].isin(["FLORESTA", "RECOLETA", "BELGRANO", "NUÑEZ"])]
> ```
> ... e responda: quantas árvores atendem a essa condição?
