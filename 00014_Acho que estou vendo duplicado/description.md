Já estudamos estratégias para lidar com dados faltantes e atípicos. Para finalizar vamos falar de outro caso comum, os duplicados! 👥 É comum encontrar células duplicadas em lotes, mas a boa notícia é que elas podem ser facilmente removidas da seguinte forma:

```python
dataset.drop_duplicates(inplace=True)
```

Caso não queiramos excluir, mas apenas obter um novo `DataFrame` sem duplicados, podemos omitir `inplace=True`. E assim como com `dropna`, podemos escolher o subconjunto de colunas que serão consideradas ao verificar duplicados, usando `subset`:


```python
tabla.drop_duplicates(subset=["tree_id"])
```

Às vezes não é tão óbvio identificar valores duplicados, porque eles podem ser facilmente confundidos com dados corretos!

> Em nosso lote de árvores não existem duas linhas idênticas, mas ainda existem entre 120 e 140 árvores **muito** suspeitas e que podem ser consideradas duplicatas 🧐. Usando `drop_duplicates`, identifique um conjunto de colunas que permita que elas sejam descartadas (e isso faz sentido em nosso problema!).


