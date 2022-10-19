import pandas as pd

class Test(unittest.TestCase):
  def test_gera_um_DataFrame(self):
    self.assertEquals(type(salgueiros), pd.DataFrame)
    
  def test_retorna_apenas_salgueiros(self):
    self.assertEquals(len(salgueiros), 1)
    self.assertEquals(salgueiros.iloc[0]["tree_id"], 13003665, "Deveria ter encontrado a árvore 13003665")
    
        