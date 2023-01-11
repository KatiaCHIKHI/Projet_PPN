from collections import defaultdict

class Graphe:


    def __init__(self,gdict=None):
        if gdict is None:
            gdict = {}
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

#graph GJ
    def find_Gj(self,j):
       gj= Graphe()
       list_voisinage = []
       Vi = []
       vertex_order = -1
       # calcul N[vi]
       list_voisinage.append(self.getSommets()[j])
       for s in self.gdict[self.getSommets()[j]]:
        list_voisinage.append(s)
       #calcul Vi
       ordre = self.degeneracy_ordering()
       for i in range(len(self.degeneracy_ordering())):
        if( ordre[i] == self.getSommets()[j]):
            vertex_order = i
        if(vertex_order != -1):
            Vi.append(ordre[i] )
        
        #N[vi] inter Vi
        for v1 in list_voisinage:
            for v2 in Vi:
                if v1 == v2 :
                    gj.addSommet(v1)
        #ajout des arcs reliants            
        for som in gj.getSommets():
            for som_voisin in self.gdict[som]:
                if (som_voisin in gj.getSommets()) and (som_voisin not in gj.gdict[som]):
                    gj.gdict[som].append(som_voisin)
                    
                  
       return gj


#fontion pour le tri d'une liste selon une autre 
def sort_items(items, order):
    return sorted(items, key=lambda x: order.index(x))

#fonction pour le filtrage de T
def filter_lists(lists):
    filtered_lists = []
    for lst in lists:
        include = True
        for lst2 in filtered_lists:
            if set(lst).issubset(set(lst2)):
                include = False
                break
        if include:
            filtered_lists.append(lst)
    return filtered_lists

