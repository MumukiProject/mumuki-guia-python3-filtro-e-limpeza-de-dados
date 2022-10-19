Neste exercício pode ser útil usar o operador `<=` e `&` para que ambas as condições sejam atendidas **ao mesmo tempo**. :wink:

💡 Além disso, antes de remover os valores fora de série do diâmetro, você pode achar interessante fazer um gráfico de caixa. Para isso temos `plot.blox`, que  permite fazer diagramas como o anterior:

```python
arvores["height"].plot.box(grid=True, vert=False)
```