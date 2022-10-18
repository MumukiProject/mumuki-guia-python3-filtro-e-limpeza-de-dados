Si quisiéramos saber qué árboles están en los barrios de Floresta y Recoleta nos podríamos tentar a hacer: 

```python
arboles[(arboles["neighbourhood"] == "FLORESTA") | (arboles["neighbourhood"] == "RECOLETA")]
```

Y quizás no parece tan grave. Pero ¿qué sucede si queremos los árboles de Floresta, Recoleta, Belgrano y Nuñez? Si bien podríamos hacer esto…

```python
arboles[(arboles["neighbourhood"] == "FLORESTA") | (arboles["neighbourhood"] == "Recoleta") | (arboles["neighbourhood"] == "BELGRANO") | (arboles["neighbourhood"] == "NUÑEZ")]
```

… no parece lo más cómodo, ¿verdad? 🙄

Por suerte existe `isin` que nos puede ahorrar bastante tiempo ⌚. Para obtener el resultado anterior podríamos hacer simplemente:

```python
arboles[arboles["neighbourhood"].isin(["FLORESTA", "RECOLETA", "BELGRANO", "NUÑEZ"])]
```

> ¿No nos creés? Verificá en tu cuaderno que las siguientes expresiones devuelvan los mismos resultados…
>
> ```python
> ム arboles[
     (arboles["neighbourhood"] == "FLORESTA") 
     | (arboles["neighbourhood"] == "RECOLETA") 
     | (arboles["neighbourhood"] == "BELGRANO")
     | (arboles["neighbourhood"] == "NUÑEZ")]
> ム  arboles[arboles["neighbourhood"].isin(["FLORESTA", "RECOLETA", "BELGRANO", "NUÑEZ"])]
> ```
> ... y respondé: ¿cuántos árboles cumplen esta condición? 
