Ya estudiamos estrategias para tratar tanto datos faltantes como atípicos. Para finalizar vamos a hablar de otro caso común, ¡los duplicados! 👥 Es frecuente encontrar celdas duplicadas en los lotes, pero la buena noticia es que pueden ser removidas fácilmente de la siguiente forma:

```python
dataset.drop_duplicates(inplace=True)
```

En caso de no querer eliminarlas sino sólo obtener un nuevo `DataFrame` sin duplicados, podemos omitir `inplace=True`. Y al igual que con `dropna`, podemos elegir el subconjunto de columnas que considerará al analizar duplicaciones, usando `subset`: 


```python
tabla.drop_duplicates(subset=["tree_id"])
```

¡A veces no es tan obvio identificar duplicados, porque se pueden confundir fácilmente con datos correctos! 

> En nuestro lote de árboles no hay dos filas idénticas, pero aún así hay entre 120 y 140 árboles **muy** sospechosos y que podrían ser considerados duplicados 🧐. Usando `drop_duplicates`, identificá un conjunto de columnas que permita eliminarlos (¡y que tenga sentido en nuestro problema!). 


