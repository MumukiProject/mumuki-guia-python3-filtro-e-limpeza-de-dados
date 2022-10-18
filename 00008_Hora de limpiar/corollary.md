Con `isna` (o lo que es lo mismo, con su sinónimo `isnull`) podemos  obtener todos los árboles de los cuáles no sabemos su calle. En nuestro caso vemos que en 12 filas esta información está ausente, lo cual es compatible con lo que nos devuelve `info`:

```python
ム arboles.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 372694 entries, 0 to 372693
Data columns (total 20 columns):
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
ム len(arboles) - 372682
12
```

Pero la gran pregunta es ¿qué hacemos ahora que sabemos que nos faltan datos? 😰
