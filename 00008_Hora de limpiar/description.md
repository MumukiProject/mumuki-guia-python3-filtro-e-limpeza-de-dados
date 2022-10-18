Cuando hablamos de limpiar nuestra tabla claro que no vamos a pasarle la escoba para sacarle el polvo 🧹. Limpieza de datos se refiere a corregir y eliminar los datos faltantes, incorrectos o problemáticos.

¡Pero antes tenemos que identificarlos! Por ejemplo, si queremos descubrir datos ausentes, podemos recurrir al conocido `info` y su _Non-Null Count_. Pero vamos a conocer otra manera de hacerlo con `isna`. 

> Probá en tu cuaderno hacer `arboles[arboles["street"].isna()]` y verificá si hay árboles sin información de calle. ¿Cuántos son?
