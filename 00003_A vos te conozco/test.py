import pandas as pd

class Test(unittest.TestCase):
  def test_genera_un_dataframe(self):
    self.assertEquals(type(sauces), pd.DataFrame)
    
  def test_sauces_solo_contiene_sauces(self):
    self.assertEquals(len(sauces), 1)
    self.assertEquals(sauces.iloc[0]["tree_id"], 13003665, "Debería haber encontrado al árbol 13003665")
    
    