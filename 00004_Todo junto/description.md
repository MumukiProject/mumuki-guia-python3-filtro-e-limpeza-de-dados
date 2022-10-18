Ya obtuvimos todos los árboles de Palermo y también todos los sauces, ¿se te ocurre cómo podemos obtener todos los sauces de Palermo? Te proponemos algunas alternativas:

Si necesitamos los árboles de Palermo en general, y además los sauces en particular podríamos encadenar nuestros filtrados de la siguiente manera:

```python
arboles_de_palermo =  arboles[arboles["neighbourhood"] == "PALERMO"]
sauces_de_palermo = arboles_de_palermo[arboles_de_palermo["comm_name"].str.startswith('Sauce')]
```

De esta forma, contaremos con dos `DataFrame`s, que podemos usar según los necesitemos. Si, en cambio, lo que necesitamos son los sauces en general y los de Palermo en particular ↔️ podríamos invertir las condiciones anteriores así:

```python
sauces =  arboles[arboles["comm_name"].str.startswith('Sauce')]
sauces_de_palermo =  sauces[sauces["neighbourhood"] == "PALERMO"]
```

Peeeero, si lo que realmente nos interesa son solamente los sauces de Palermo podemos filtrar las dos condiciones al mismo tiempo utilizando la conjunción lógica ✌️:

```python
arboles[(arboles["neighbourhood"] == "PALERMO") & arboles["comm_name"].str.startswith("Sauce")]
```

> ¡Veamos si se entendió!  Usando todo lo visto, escribí una **única expresión** aquellos árboles que se encuentren en la comuna 10 y que sean de la familia de las Oleáceas.
