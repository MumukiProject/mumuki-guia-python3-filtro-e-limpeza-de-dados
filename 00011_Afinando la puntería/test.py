import pandas as pd

class Test(unittest.TestCase):
  def setUp(self):
    self.resultado = (
      #...content...#
    )
  
  def test_genera_un_dataframe(self):
    self.assertEquals(type(self.resultado), pd.DataFrame)
    
  def test_contiene_menos_arboles(self):
    self.assertTrue(len(self.resultado) == 6)
    
  def test_no_contiene_arboles_sin_latitud(self):
    indexado = self.resultado.set_index("tree_id")
    self.assertTrue(142527 not in indexado)
    self.assertTrue(8087 not in indexado)
    self.assertTrue(39000768 not in indexado)

  def test_no_contiene_arboles_sin_longitud(self):
    indexado = self.resultado.set_index("tree_id")
    self.assertTrue(4101876 not in indexado)
    self.assertTrue(8087 not in indexado)

    