class Test(unittest.TestCase):

  def test_as_árvores_com_colunas_NAN_são_removidas(self):
    self.assertTrue(len(arvores) == 7, "todas as árvores com valores nan deveriam ter sido removidas")
    
    indexado = arvores.set_index("tree_id")
    
    self.assertTrue(4101876 not in indexado, "todas as árvores com valores nan deveriam ter sido removidas")
    self.assertTrue(4101166 not in indexado, "todas as árvores com valores nan deveriam ter sido removidas")
    self.assertTrue(24002305 not in indexado, "todas as árvores com valores nan deveriam ter sido removidas")    
 

        