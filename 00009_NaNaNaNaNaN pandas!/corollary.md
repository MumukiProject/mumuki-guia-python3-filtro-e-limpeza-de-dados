Muito bem! :sparkles: Novamente, também poderíamos obter esta informação com `info()`...

```python
ムarvores.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 372694 entries, 0 to 372693
Data colunas (total 20 colunas):
 #   Column         Non-Null Count   Dtype  
---  ------         --------------   -----  
 0   long           372659 non-null  float64
 1   lat            372659 non-null  float64
(...)
 18  num1           372635 non-null  float64
 19  num2           372605 non-null  float64
dtypes: float64(10), object(10)
```

... mas foi definitivamente muito mais direto usar `notna` :sunglasses::


```python
ムlen(arvores[arvores["num1"].notna()])
372635
```

E o que acontece se queremos eliminar toooodos os `nan`? 
