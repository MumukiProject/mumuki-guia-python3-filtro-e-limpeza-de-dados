Uh, mas como sabemos quais colunas são relevantes quando se trata de remover duplicatas? 😟 Não existe uma resposta única e depende muito dos dados com os quais estamos trabalhando. 😭 Mas podemos aplicar algumas _intuições_! Por exemplo, sabemos que as colunas de `arvores` são estas:

* `long`
* `lat`
* `site_type`
* `tree_id`
* `height`
* `diameter`
* ...

Poderia `long` ser uma coluna relevante? Claro! Afinal, existem muitas árvores com o mesmo valor `long`:

```python
ム len(arvores) - arvores["long"].nunique()
# > 1000 experimente!
```

* `long` :white_check_mark:
* `lat`
* `site_type`
* `tree_id`
* `height`
* `diameter`
* ...


⚠️ Mas cuidado, porque também pode haver duas árvores no mesmo `long` mas diferentes `lat`. Na verdade, `lat` também é relevante, porque você encontrará árvores no mesmo local aproximado (mesmo `lat` e `long`)...

```python
ム len(arvores) - len(arvores.drop_duplicates(subset=["long", 'lat']))
# tente!
```

* `long` :white_check_mark:
* `lat` :white_check_mark:
* `site_type`
* `tree_id`
* `height`
* `diameter`
* ...


...mas talvez um tipo ou altura diferente, então precisamos continuar olhando para as outras colunas 🤷. E poderia `site_type` ser uma coluna relevante?

Não, porque se virmos o seu número de valores únicos veremos que existe apenas um...

```python
ム list(arvores["site_type"].unique())
['Árbol']
```

...e, portanto, não nos fornece nenhuma informação e não é relevante.

* `long` :white_check_mark:
* `lat` :white_check_mark:
* `site_type` :negative_squared_cross_mark:
* `tree_id`
* `height`
* `diameter`
* ...


O resto é com você!