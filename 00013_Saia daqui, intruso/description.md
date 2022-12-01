Ao limpar nossos dados, não queremos apenas remover valores nulos, mas também aqueles que sejam atípicos. Esses tipos de valores, também conhecidos como fora de série (ou, em inglês, _outliers_), não são necessariamente um erro, mas ainda vamos limpá-los porque não são representativos da nossa amostra🧹. 

Vamos observar por exemplo a altura das nossas árvores 🌲...

```python
ム arvores["height"].max()
60.0
```

...e vamos comparar com a mediana:

```python
ム arvores["height"].median()
8
```

Há muita diferença! Isso poderia estar correto, mas por via das dúvidas, vamos verificar o que acontece se removermos, por exemplo, 2% das árvores mais altas usando `quantil`:  

```python
ム arvores["height"].quantile(0.98)
20
```

Wow! Quanta mudança! Tudo parece indicar que as árvores mais altas estão _fora de série_ e têm uma altura _desproporcional_, que supera em muito a das demais. De fato, se fizéssemos  um gráfico de caixa dessas duas variáveis, observaríamos esses valores extremos como pontos acima do bigode superior:

<img src="https://raw.githubusercontent.com/MumukiProject/mumuki-guia-python3-filtrado-y-limpieza-de-datos/master/assets/boxplot_2_1665547665355.png" alt="boxplot_2_1665547665355.png" width="auto" height="auto">

Quando nos deparamos com essa situação, geralmente também optamos por remover estes escassos valores pouco representativos do conjunto de dados.

> Parece que temos que passar a tesoura por aqui ✂️. Mantenha apenas as árvores que estão dentro dos 98% das árvores mais baixas **e de menor diâmetro**.

