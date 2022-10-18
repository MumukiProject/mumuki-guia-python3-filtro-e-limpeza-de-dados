`notna` es la operación inversa a `isna` por lo que deberías hacer algo parecido al ejercicio anterior...

```python
arboles[arboles["street"].isna()]
```

...pero esta vez obteniendo las filas que **no tengan** `nan` en su `calle`. 