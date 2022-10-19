import pandas as pd

class Test(unittest.TestCase):
  def setUp(self):
    self.resultado = (
      #...content...#
    )
  
  def test_gera_um_DataFrame(self):
    self.assertEquals(type(self.resultado), pd.DataFrame)
    
  def test_contem_menos_árvores(self):
    self.assertTrue(len(self.resultado) == 6)
    
  def test_não_contém_arvores_sem_latitude(self):
    indexado = self.resultado.set_index("tree_id")
    self.assertTrue(142527 not in indexado)
    self.assertTrue(8087 not in indexado)
    self.assertTrue(39000768 not in indexado)

  def test_não_contém_arvores_sem_longitude(self):
    indexado = self.resultado.set_index("tree_id")
    self.assertTrue(4101876 not in indexado)
    self.assertTrue(8087 not in indexado)

            