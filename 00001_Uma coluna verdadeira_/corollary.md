Obtivemos um `Series` de booleanos! :sunglasses:

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

Cada um dos booleanos nesta coluna representam se a condição foi atendida ou não para cada valor da coluna original. Neste caso em particular, se a altura de uma árvore fosse maior ou igual a 7, poderíamos encontrar em nossa coluna booleana nessa posição `True` ou `False`, dependendo se essa condição fosse atendida ou não.
