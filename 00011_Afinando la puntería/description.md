`dropna` también nos permite decidir sobre qué columnas queremos hacer el filtrado con el argumento opcional `subset` de la siguiente forma:

```python
tabla.dropna(subset=[columna1, columna2,...])
```

Por ejemplo, hacer....

```python
arboles.dropna(subset=["diameter"])
```

... es equivalente a:

```python
arboles[arboles["diameter"].notna()]
```

La ventaja de esta opción es que ahora podemos eliminar filas más selectivamente, conservando aquellas que tengan `nan`s en columnas poco relevantes para nuestro análisis.

> ¡Probalo! ♻️ Volvé a ejecutar la celda donde se carga el `DataFrame` `arboles`, para restaurarlo a su valor original. Luego escribí en una nueva celda una expresión que nos permita obtener los árboles que no tengan `nan` en su latitud ni en su longitud.
