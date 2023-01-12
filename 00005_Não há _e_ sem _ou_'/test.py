import pandas as pd

class Test(unittest.TestCase):
  def setUp(self):
    self.resultado = (
      #...content...#
    )
  
  def test_gera_o_DataFrame(self):
    self.assertEquals(type(self.resultado), pd.DataFrame)
    
  def test_contém_apenas_as_árvores_solicitadas(self):
    self.assertEquals(len(self.resultado), 3)
    
    self.assertTrue(8087 in list(self.resultado["tree_id"]), "Deveria ter encontrado a árvore 8087")
    self.assertTrue(142527 in list(self.resultado["tree_id"]), "Deveria ter encontrado a árvore 142527")
    self.assertTrue(182465 in list(self.resultado["tree_id"]), "Deveria ter encontrado a árvore 182465")