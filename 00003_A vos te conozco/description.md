¡Es hora de combinar herramientas! ➕ 

¿Te acordás que trabajamos con operaciones de strings como `in`, `str.startswith`o `str.endswith`? Estas mismas operaciones las podemos utilizar con nuestros datos pero la sintaxis varía un poco. Antes si queríamos saber si un nombre terminaba con la letra `a` debíamos hacer algo así:

```python
str.endswith(nombre, "a")
```

Mientras que si ahora buscáramos a todas las personas que tengan un nombre terminado con la letra `a` deberíamos hacer 

```python
personas[personas["nombre"].str.endswith("a")]
```

Podrás notar que ahora solo le pasamos el segundo argumento a `str.endswith`. 

> ¡Practiquemos con otra operación! Escribí una expresión que te permita obtener todos los sauces de nuestro `DataFrame` de árboles, y asigná su resultado en `sauces`.
