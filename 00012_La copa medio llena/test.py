class Test(unittest.TestCase):

  def test_no_se_elimina_ningun_arbol(self):
    self.assertTrue(len(arboles) == 10)
    
  def test_no_quedan_inclinaciones_en_nan(self):
    self.assertTrue(arboles["inclination"].count() == 10)  
    
  def test_la_inclinacion_se_llena_con_el_promedio(self):
    self.assertTrue(arboles["inclination"].mean() == 2.142857142857143)      