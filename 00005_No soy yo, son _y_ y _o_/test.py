import pandas as pd

class Test(unittest.TestCase):
  def setUp(self):
    self.resultado = (
      #...content...#
    )
  
  def test_genera_un_dataframe(self):
    self.assertEquals(type(self.resultado), pd.DataFrame)
    
  def test_sauces_solo_contiene_sauces(self):
    self.assertEquals(len(self.resultado), 3)
    
    self.assertTrue(8087 in list(self.resultado["tree_id"]), "Debería haber encontrado al árbol 8087")
    self.assertTrue(142527 in list(self.resultado["tree_id"]), "Debería haber encontrado al árbol 142527")
    self.assertTrue(182465 in list(self.resultado["tree_id"]), "Debería haber encontrado al árbol 182465")
    