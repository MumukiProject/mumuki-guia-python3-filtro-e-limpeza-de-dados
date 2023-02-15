Com `isna` (que é o mesmo que seu sinônimo `isnull`) podemos obter todas as árvores cuja rua não sabemos. No nosso caso vemos que em 12 linhas esta informação está ausente, o que é compatível com o que `info` retorna:

```python
ムarvores.info()
# <class 'pandas.core.frame.DataFrame'>
RangeIndex: 372694 entries, 0 to 372693
Data colunas (total 20 colunas):
 #   Column         Non-Null Count   Dtype  
---  ------         --------------   -----  
 0   long           372659 non-null  float64
 1   lat            372659 non-null  float64
 2   site_type      372694 non-null  object
 3   tree_id        372694 non-null  float64
 (...)
 17  street         372682 non-null  object
 18  num1           372635 non-null  float64
 19  num2           372605 non-null  float64
dtypes: float64(10), object(10)
ムlen(arvores) - 372682
12
```

Mas a grande questão é o que fazemos agora que sabemos que faltam dados? 😰
