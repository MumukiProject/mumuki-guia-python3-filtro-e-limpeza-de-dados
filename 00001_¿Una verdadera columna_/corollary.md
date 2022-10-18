¡Obtuvimos un `Series` de booleanos! :sunglasses:

```
0          True
1          True
2         False
3          True
4         False
          ...  
372694     True
372695     True
372696     True
372697     True
372698    False
Name: height, Length: 372699, dtype: bool
```

Cada uno de los booleanos de esta columna representan si se cumplió o no la condición por cada valor de la columna original. En este caso particular, si la altura de un árbol era mayor o igual a 7 podremos encontrar en nuestra columna de booleanos en esa posición `True` o `False`, según si se cumple o no esa condición.
