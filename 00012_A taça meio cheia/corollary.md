Excelente! Nesse caso, substituímos todas as inclinações faltantes pela média desta coluna. Embora pudéssemos ter feito isso por um valor específico, por exemplo 8, fazendo...

```python
arvores["inclination"].fillna(8, inplace=True)
```

...preferimos substituir pela média para tentar minimizar o impacto nas análises estatísticas. Caso contrário, estaríamos distorcendo a verdadeira distribuição da variável.

Também poderíamos ter substituído todos os valores ausentes em nossa tabela já que `fillna` também funciona com `DataFrame`s:

```python
arvores.fillna(arvores["inclination"].median(), inplace=True)
```

Mas fazer isso traz o risco de substituir outros dados  faltantes, como por exemplo alturas, pela média da inclinação.
