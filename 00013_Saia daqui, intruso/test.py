class Test(unittest.TestCase):

  def test_arvores_agora_devem_ter_menos_linhas(self):
    self.assertTrue(len(arvores) == 9, "Deve haver menos árvores no DataFrame original")
    
  def test_árvores_muito_altas_e_largas_deveriam_ter_sido_removidas(self):
    self.assertTrue(182465 not in arvores.set_index("tree_id").index)
      
