from Graphe import Graphe
from Graphe import sort_items
from Graphe import filter_lists
from Bron_kerbosch_function import find_cliques


graph_elements = { 
   "1" : ["2","3"],
   "2" : ["1","3"],
   "3" : ["1","2","4"],
   "4" : ["3"]
}

# Instanciation
g = Graphe(graph_elements)
 
#initialiser une liste vide T
T = []


#Implémentation 
for j in range(0, len(g.getSommets())):
   Gj = g.find_Gj(j)
   cliques = find_cliques(Gj)
   for k in cliques:
      k = sort_items(k,g.degeneracy_ordering())
      for n in k:
         T.append(k)
         T= filter_lists(T)


#affichage des cliques          
print("les cliques maximales du graphe sont:")
for k in T:
   print(k)
      










