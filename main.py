from collections import defaultdict

class Graphe:


    def __init__(self,gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict

# Get les sommets du graphe
    def getSommets(self):
        return list(self.gdict.keys())



# Ajouter un sommet
    def addSommet(self, somm):
        if somm not in self.gdict:
            self.gdict[somm] = []

    def addArc(self,arc):
        arc = set(arc)
        (somm1, somm2) = tuple(arc)
        if somm1 in self.gdict:
            self.gdict[somm1].add(somm2)
        else:
            self.gdict[somm1] = set(somm2)
        if somm2 in self.gdict:
            self.gdict[somm2].add(somm1)
        else:
            self.gdict[somm2] = set(somm1)


# Get les arcs du graphe
    def getArcs(self):
        arcs = []
        for somm in self.gdict:
            for nxtsomm in self.gdict[somm]:
                if {nxtsomm, somm} not in arcs:
                 arcs.append({somm, nxtsomm})
        return arcs




# Calculer les degrés des sommets
    def calculate_degrees(self):
        degrees = defaultdict(int)
        for somm in self.gdict:
            for neighbor in self.gdict[somm]:
                degrees[somm] += 1
              
        return degrees

# Calculer l'ordre de dégenerescence


    def degeneracy_ordering(self):
        ordering = []
        degrees = self.calculate_degrees()
        sorted_vertices = sorted(degrees, key=lambda x: degrees[x], reverse=False)


        while len(sorted_vertices) > 0:
   
            somm = sorted_vertices.pop(0)   # Enlever le premier noeud de la queue(celui qui a le plus petit degré)
            
    
            ordering.append(somm)           # Ajouter ce noeud a  ordering
    
            for u in self.gdict:

                degrees[u] -= 1                 
                
        
        return ordering


# Calculer degeneracy

    def degeneracy(self):

        degrees = self.calculate_degrees()
        sorted_vertices = sorted(degrees, key=lambda x: degrees[x], reverse=False)
        k = 0

        
        for vertex in sorted_vertices:
            if degrees[vertex] > k:
                k += 1
            else:
                break
        print("the degeneracy of the graph is : ",k)

#########################################################################################################

# Graph
                 
graph_elements = { 
   "1" : ["2","3"],
   "2" : ["1","3"],
   "3" : ["1","2","4"],
   "4" : ["3"]

  
}


# Instanciation
g = Graphe(graph_elements)


#Tests

print("Degrees of nodes :",g.calculate_degrees())
o=g.degeneracy_ordering()

print("order of degeneracy is ",o)
g.degeneracy()







