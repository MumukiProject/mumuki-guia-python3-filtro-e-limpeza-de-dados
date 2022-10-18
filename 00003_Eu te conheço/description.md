É hora de combinar ferramentas! ➕ 

Você se lembra que trabalhamos com operações de string como `in`, `str.startswith`ou `str.endswith`? Podemos usar essas mesmas operações com nossos dados, mas a sintaxe varia um pouco. Antes, se quiséssemos saber se um nome terminava com a letra `a`, tínhamos que fazer algo assim:

```python
str.endswith(nome, "a")
```

Considerando que se fôssemos agora procurar por todas as pessoas que têm um nome que termina com a letra 'a', deveríamos fazer

```python
pessoas[pessoas["nome"].str.endswith("a")]
```

Você notará que agora só passamos o segundo argumento para `str.endswith`. 

> Vamos praticar com outra operação! Escreva uma expressão para obter todas as árvores do tipo salgueiro (_sauce_) do nosso `DataFrame` de árvores e defina seu resultado como `salgueiros`.
