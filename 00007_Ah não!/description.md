A última operação lógica que veremos para usar em nossas colunas de booleanos é a famosíssima negação.

Como `not` trabalha com booleanos negando seu valor de verdade, a maneira de operar em uma `Series` de booleanos é com o operador `~`.Por exemplo, se quiséssemos conhecer todas as pessoas cujo sobrenome *não* termina com s, poderíamos obtê-las assim:

```python
pessoas[~pessoas["sobrenome"].str.endswith("s")]
```


> Agora é a sua vez! Usando `~`, escreva uma **expressão** que obtenha todas as árvores que não sejam árvores de freixo (_fresno_), ou seja, cujo nome comum não  (`comm_name`) comece com `"Fresno"`.
