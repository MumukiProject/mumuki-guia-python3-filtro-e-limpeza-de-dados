En este ejercicio te puede ser útil utilizar el operador `<=` y `&` para que se cumplan ambas condiciones **al mismo tiempo**. :wink: 

💡 Además, antes de remover los valores fuera de serie del diámetro, te puede resultar interesante realizar un gráfico de caja. Para ello contamos con `plot.blox`, que nos permite realizar diagramas como el anterior: 

```python
arboles["height"].plot.box(grid=True, vert=False)
```
