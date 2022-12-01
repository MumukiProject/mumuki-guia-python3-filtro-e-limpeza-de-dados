Uma última alternativa para manipular dados faltantes é substituí-los. Embora possamos fazer isso com um valor fixo, é uma boa ideia usar valores calculados que façam sentido para seu conjunto de dados. Por exemplo, podemos _preenchê-los_ com a média obtida a partir dos outros valores dessa variável:


```python
tabela["coluna_com_faltantes"].fillna(tabela["coluna_com_faltantes"].mean())
```

Esta expressão retorna um novo `Series` com as substituições, embora possamos substituí-las diretamente em nosso `DataFrame` fazendo:


```python
tabela["coluna_com_faltantes"].fillna(tabela["coluna_com_faltantes"].mean(), inplace=True)
```

> Vamos testar! Substitua em `arvores` todas as inclinações faltantes pela média dessa coluna. 
