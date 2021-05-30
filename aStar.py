class Noeud:
  """
  Classe pour les noeuds du graphe
  """
  def __init__(self, x, y, cout, heuristique):
    self.x = x
    self.y = y
    self.cout = cout
    self.heuristique = heuristique

  def __str__(self) -> str:
    return str(self.x) + " " + str(self.y) + " " + str(self.cout) + " " + str(self.heuristique)

class File:
  """
  Classe pour les files
  """
  def __init__(self):
    

def compare2Noeuds(noeud1, noeud2):
  if(noeud1.heuristique < noeud2.heuristique):
    return 1
  elif(noeud1.heuristique == noeud2.heuristique):
    return 0
  else:
    return -1



depart = Noeud(0, 0, 0, 0)
