import pandas as pd

class Test(unittest.TestCase):
  def setUp(self):
    self.resultado = (
      #...content...#
    )

  def test_gera_um_DataFrame(self):
    self.assertEquals(type(self.resultado), pd.DataFrame)
    
  def test_não_retorna_todas_as_árvores(self):
    self.assertEquals(len(self.resultado), 1)
    
  def test_retorna_apenas_árvores_de_palermo(self):
    self.assertEquals(list(self.resultado["neighbourhood"].unique()), ["PALERMO"])    