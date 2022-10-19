Quando falamos em limpar nossa tabela, claro que não vamos passar a vassoura para tirar o pó 🧹. A limpeza de dados refere-se a corrigir e remover dados faltantes, incorretos ou problemáticos.

Mas primeiro temos que identificá-los! Por exemplo, se quisermos descobrir dados ausentes, podemos recorrer ao conhecido `info` e sua _Non-Null Count_. Mas vamos aprender outra maneira de fazer isso com `isna`.

> Tente em seu caderno fazer `arvores[arvores["street"].isna()]` e verifique se existem árvores sem informação da rua onde estão localizadas. Quantas são?
