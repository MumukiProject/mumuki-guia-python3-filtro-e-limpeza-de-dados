Outra das soluções possíveis para o tratamento dos dados faltantes é eliminar todas as linhas que tenham algum dado faltante 🗑️. Isso  podemos fazer utilizando `dropna` da seguinte forma:

```python
tabela.dropna()
```

Inclusive poderíamos eliminar aquelas linhas que tenham mais de um dado faltante  fazendo:

```python
# elimina todas as linhas que tenham 2 ou mais colunas com nan
tabela.dropna(thresh=2) 
```

Diferente das filtragens anteriores, com `dropna` podemos eliminar estas linhas em nossa tabela original utilizando `inplace=True` como argumento:

```python
tabela.dropna(inplace=True)
# ou combinando ambos parâmetros
tabela.dropna(thresh=2, inplace=True)
```


👀Atenção! Esta operação modifica a tabela e se deletarmos coisas que não deveríamos, nós as perdemos para sempre! Tenha cuidado especial antes de executá-la 🥺. 

>Vamos tentar! Elimine do `DataFrame` `arvores` todas as linhas que tenham algum valor nulo. 🧼
