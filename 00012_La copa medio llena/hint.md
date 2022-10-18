Si quisiéramos reemplazar las alturas faltantes por la mediana de esa columna deberíamos hacer:

```python
arboles["height"].fillna(arboles["height"].median(), inplace=True)
```

Pero lo que queremos hacer es reemplazar las inclinaciones faltantes por su promedio, claro :wink:.
