Já temos todas as árvores de Palermo e também todos os salgueiros. Mas, como podemos obter todos os salgueiros de Palermo? Sugerimos algumas alternativas:

Se precisarmos das árvores de Palermo de maneira geral, e também dos salgueiros em particular, poderíamos associar nossos filtros da seguinte maneira:

```python
arvores_de_palermo =  arvores[arvores["neighbourhood"] == "PALERMO"]

salgueiros_de_palermo = arvores_de_palermo[arvores_de_palermo["comm_name"].str.startswith('Sauce')]
```

Desta forma, teremos dois `DataFrame`s, que podemos usar conforme a necessidade. Se, em vez disso, o que precisamos são os salgueiros em geral e particularmente os de Palermo ↔️ poderíamos inverter as condições anteriores assim:

```python
salgueiros =  arvores[arvores["comm_name"].str.startswith('Sauce')]

salgueiros_de_palermo =  salgueiros[salgueiros["neighbourhood"] == "PALERMO"]
```

Maaaaas, se o que realmente nos interessa são apenas os salgueiros de Palermo, podemos filtrar as duas condições ao mesmo tempo usando a conjunção lógica ✌️:


```python
arvores[(arvores["neighbourhood"] == "PALERMO") & arvores["comm_name"].str.startswith("Sauce")]
```

> Vejamos se ficou claro! Usando tudo o que vimos, escreva uma **única expressão** que retorne aquelas árvores que estão na comuna 10 e que são da família das Oleáceas.
