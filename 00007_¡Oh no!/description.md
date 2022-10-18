La última operación lógica que veremos para utilizar en nuestras columnas de booleanos es la famosísima negación :person_gesturing_no:. 

Dado que `not` trabaja con booleanos negando su valor de verdad, la forma de operar en un `Series` de booleanos es con el operador `~`. Por ejemplo, si quisiéramos saber todas las personas cuyo apellido *no* termine con z podríamos obtenerlas así:

```python
personas[~personas["apellido"].str.endswith("z")]
```

> ¡Ahora te toca a vos! Utilizando `~` escribí una **única expresión** que obtenga todos los árboles que no sean Fresnos, es decir, que su nombre no comience con "Fresno". 
