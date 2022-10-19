import pandas as pd

class Test(unittest.TestCase):
  def setUp(self):
    self.resultado = (
      #...content...#
    )
  
  def test_gera_o_DataFrame(self):
    self.assertEquals(type(self.resultado), pd.DataFrame)
    
  def test_retorna_apenas_oleaceas_comuna_10(self):
    self.assertEquals(len(self.resultado), 1)
    self.assertEquals(self.resultado.iloc[0]["tree_id"], 182465, "Deveria ter encontrado a árvore 182465")
    
    