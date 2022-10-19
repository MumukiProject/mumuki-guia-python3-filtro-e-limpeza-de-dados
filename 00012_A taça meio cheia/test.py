class Test(unittest.TestCase):

  def test_nenhuma_árvore_é_removida(self):
    self.assertTrue(len(arvores) == 10)
    
  def test_não_há_mais_inclinações_em_nan(self):
    self.assertTrue(arvores["inclination"].count() == 10)  
    
  def test_a_inclinação_é_preenchida_com_a_média(self):
    self.assertTrue(arvores["inclination"].mean() == 2.142857142857143)                  