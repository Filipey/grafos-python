from ..domain.models.Grafo import Grafo
from ..domain.repositories.GrafoRepository import *

g1 = Grafo()
g1.ler_arquivo("grafo1.txt")
print(g1.lista_adj)
print(f"Densidade grafo 1: {g1.densidade()}")

g2 = Grafo()
g2.ler_arquivo("grafo2.txt")
print(g2.lista_adj)
print(f"Densidade do grafo 2: {g2.densidade()}")