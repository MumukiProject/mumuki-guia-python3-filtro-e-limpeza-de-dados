Otra de las soluciones posibles para el tratamiento de los datos faltantes es eliminar toda las filas que contengan algún dato faltante 🗑️. Esto lo podemos hacer utilizando `dropna` de la siguiente forma:

```python
tabla.dropna()
```
Incluso podríamos eliminar aquellas filas que tengan más de un dato faltante  haciendo:

```python
# elimina todas las filas que tengan 2 o más columnas con nan
tabla.dropna(thresh=2) 
```

A diferencia de los filtrados anteriores, con `dropna` podemos eliminar estas filas en nuestra tabla original utilizando `inplace=True` como argumento:

```python
tabla.dropna(inplace=True)
# o combinando ambos parámetros
tabla.dropna(thresh=2, inplace=True)
```

👀 ¡Ojo! Esta operación modifica la tabla y si borramos cosas que no debíamos, ¡las perdemos para siempre! Tené especial cuidado antes de ejecutarla. 🥺 

> ¡Vamos a probarlo! Eliminá del `DataFrame` `arboles` todas las filas que tengan algún valor nulo. 
