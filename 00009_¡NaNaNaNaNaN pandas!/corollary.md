¡Bien! :sparkles: Nuevamente, esta información también podríamos haberla obtenido con `info()`...

```python
ム arboles.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 372694 entries, 0 to 372693
Data columns (total 20 columns):
 #   Column         Non-Null Count   Dtype  
---  ------         --------------   -----  
 0   long           372659 non-null  float64
 1   lat            372659 non-null  float64
(...)
 18  num1           372635 non-null  float64
 19  num2           372605 non-null  float64
dtypes: float64(10), object(10)
```

... pero definitivamente fue mucho más directo usar `notna` :sunglasses::


```python
ム len(arboles[arboles["num1"].notna()])
372635
```

 ¿Y qué sucede si queremos eliminar toooodos los `nan`? 
