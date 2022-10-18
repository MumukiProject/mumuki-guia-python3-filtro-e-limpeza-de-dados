A la hora de limpiar nuestros datos no solamente vamos a querer remover los valores nulos sino también aquellos que sean atípicos. Este tipo de valores, también conocidos como fuera de serie (o, en inglés, _outliers_), no necesariamente son un error de carga pero aún así los limpiaremos por no ser representativos de nuestra muestra 🧹. 

Observemos por ejemplo la altura de nuestros árboles 🌲...

```python
ム arboles["height"].max()
60.0
```

...y comparémoslos con su mediana:

```python
ム arboles["height"].median()
8
```

¡Hay mucha diferencia! Esto podría ser correcto, pero por las dudas verifiquemos qué sucede si quitamos, por ejemplo, el 2% más alto utilizando `quantile`:  

```python
ム arboles["height"].quantile(0.98)
20
```

¡Wow! ¡Cuánto cambió! Todo parece indicar que los árboles más altos están _fuera de serie_ y presentan una altura _desproporcionada_, que excede ampliamente la de los demás.  De hecho, si realizáramos un gráfico de caja de estas dos variables observaríamos a estos valores extremos como puntos por encima del bigote superior:

<img src="https://raw.githubusercontent.com/MumukiProject/mumuki-guia-python3-filtrado-y-limpieza-de-datos/master/assets/boxplot_2_1665547665355.png" alt="boxplot_2_1665547665355.png" width="auto" height="auto">


Cuando estamos ante esta situación, usualmente también optaremos por quitar a estos escasos valores poco representativos del conjunto de datos.

> Parece que tenemos que pasar la tijera por acá ✂️. Remové de `arboles` aquellos que estén dentro del 98% más bajo **y de menor diámetro**.
