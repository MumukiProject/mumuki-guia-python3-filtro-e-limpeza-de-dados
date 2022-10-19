No exercício anterior obtivemos aquelas linhas que têm `nan` na coluna `rua`. `nan` (devido as siglas de _Not a Number_ em inglês) é um valor que costuma ser usado para representar a ausência dos dados (também conhecida em inglês como _Not Available_ ou _NA_) 🕳. O que fazemos nesses casos?

Para falar a verdade, não existe uma resposta única: dependendo do nosso lote de dados e da variável em questão, teremos que tomar decisões diferentes. Por exemplo, uma coisa que podemos fazer é remover aquelas linhas que possuem um valor `nan` em uma coluna específica usando `notna` ✂️. `notna` funciona ao contrário de `isna` e retorna verdadeiro quando o valor não é nulo.

> Agora tente em seu caderno obter apenas aquelas árvores que tenham preenchido seu número (altura) de rua (coluna `num1`). Quantos são?
