class Test(unittest.TestCase):

  def test_los_arboles_con_columnas_na_son_eliminados(self):
    self.assertTrue(len(arboles) == 7, "se deberían haber eliminado todos los árboles con valores nan")
    
    indexado = arboles.set_index("tree_id")
    
    self.assertTrue(4101876 not in indexado, "se deberían haber eliminado todos los árboles con valores nan")
    self.assertTrue(4101166 not in indexado, "se deberían haber eliminado todos los árboles con valores nan")
    self.assertTrue(24002305 not in indexado, "se deberían haber eliminado todos los árboles con valores nan")