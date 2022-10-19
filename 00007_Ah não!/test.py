import pandas as pd

class Test(unittest.TestCase):
  def setUp(self):
    self.resultado = (
      #...content...#
    )  
  
  def test_gera_o_DataFrame(self):
    self.assertEquals(type(self.resultado), pd.DataFrame)
    
  def test_não_contém_freixos(self):
    tree_ids = list(self.resultado["tree_id"])
 
    self.assertEquals(len(self.resultado), 5)
    self.assertTrue(142527 in tree_ids, "Deveria ter encontrado a árvore 142527")
    self.assertTrue(24002305 in tree_ids, "Deveria ter encontrado a árvore 24002305")
    self.assertTrue(2003708 in tree_ids, "Deveria ter encontrado a árvore 2003708")
    self.assertTrue(13003665 in tree_ids, "Deveria ter encontrado a árvore 13003665")    
