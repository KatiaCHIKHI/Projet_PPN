
#calculer les cliques maximales d'un graphe
#en utilisant l'algorithme du bron kerbosch


def find_cliques(graph):
  p = set(graph.gdict.keys())
  r = set()
  x = set()
  cliques = []
  for v in graph.degeneracy_ordering():
    neighs = graph.gdict[v]
    find_cliques_pivot(graph.gdict, r.union([v]), p.intersection(neighs), x.intersection(neighs), cliques)
    p.remove(v)
    x.add(v)
  return sorted(cliques, key= lambda x: len(x))


def find_cliques_pivot(graph, r, p, x, cliques):
  if len(p) == 0 and len(x) == 0:
    cliques.append(r)
  else:
    u = iter(p.union(x)).__next__()
    for v in p.difference(graph[u]):
      neighs = graph[v]
      find_cliques_pivot(graph, r.union([v]), p.intersection(neighs), x.intersection(neighs), cliques)
      p.remove(v)
      x.add(v)
