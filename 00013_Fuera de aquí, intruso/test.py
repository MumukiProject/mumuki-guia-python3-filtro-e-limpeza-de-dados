class Test(unittest.TestCase):

  def test_arboles_deberia_tener_ahora_menos_filas(self):
    self.assertTrue(len(arboles) == 9, "Debería haber menos árboles en el DataFrame original")
    
  def test_deberian_haberse_ido_arboles_demasiado_altos_y_anchos(self):
    self.assertTrue(182465 not in arboles.set_index("tree_id").index)
      
    