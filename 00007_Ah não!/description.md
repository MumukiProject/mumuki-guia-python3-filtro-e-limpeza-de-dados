A última operação lógica que veremos para usar em nossas colunas de booleanos é a famosíssima negação.

Como `not` trabalha com booleanos negando seu valor de verdade, a maneira de operar em uma `Series` de booleanos é com o operador `~`.

Por exemplo, se quiséssemos conhecer todas as pessoas cujo sobrenome *não* termina com z, poderíamos obtê-las fazendo `pessoas[~pessoas["sobrenome"].str.endswith("z")]`.

> Agora é a sua vez! Usando `~` obtenha todas as árvores que não sejam árvores de freixo (_fresno_), ou seja, cujo nome não comece com `"Fresno"`.
