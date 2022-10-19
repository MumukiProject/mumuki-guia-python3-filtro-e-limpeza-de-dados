`notna`é a operação inversa de `isna`, então você deveria fazer algo semelhante ao exercício anterior...

```python
arvores[arvores["street"].isna()]
```

...mas desta vez obtendo as linhas que não tenham `nan` na `rua`.
