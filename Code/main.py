from Graphe import Graphe
from Bron_kerbosch_function import find_cliques


graph_elements = { 
   "1" : ["2","3"],
   "2" : ["1","3"],
   "3" : ["1","2","4"],
   "4" : ["3"]
}

# Instanciation
g = Graphe(graph_elements)
 
#Tests

#degrés des noeuds
print("Degrees of nodes :",g.calculate_degrees())

#ordre de dégénérescence
o=g.degeneracy_ordering()
print("order of degeneracy is ",o)

#dégénérescence
g.degeneracy()

# Graph Gj
G0 = g.find_Gj(0)
print("graph G0:  ",G0.gdict)

#test de la fonction bron kerbosch
total_cliques = find_cliques(g)
print('Total cliques found:', total_cliques)











