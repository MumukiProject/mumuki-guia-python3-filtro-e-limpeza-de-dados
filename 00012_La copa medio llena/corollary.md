¡Excelente! En este caso reemplazamos todas las inclinaciones faltantes por el promedio de esta columna. Si bien podíamos haberlo hecho por un valor concreto, por ejemplo 8, haciendo...

```python
arboles["inclination"].fillna(8, inplace=True)
```

...preferimos reemplazarlo por el promedio para intentar minimizar el impacto en los análisis estadísticos. De lo contrario, estaríamos distorsionando la verdadera distribución de la variable. 

También podríamos haber reemplazado todos los valores ausentes de nuestra tabla dado que `fillna` también funciona con `DataFrame`s:

```python
arboles.fillna(arboles["inclination"].median(), inplace=True)
```

Pero hacer esto implica el riesgo de reemplazar otros datos faltantes, como por ejemplo alturas, por el promedio de la inclinación.
