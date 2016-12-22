#!/usr/bin/python -tt

from graph import Graph

visited = []	# track the visiting state of vertices
topo_order = [] # use this as stack

def dfs(graph):
  for v in graph.nvertices:
    visited.append(False)
  for v in graph.nvertices:
    if not visited[v]:
      dfs_visit(g, v)

def dfs_visit(graph, v):
  process_vertex(v)
  visited[v] = True
  
  neibors = graph.edges[v]
  while neibors:
    vneibor = neibors.vertex
    if not visited[vneibor]:
      dfs_visit(graph, vneibor)
    neibors = neibors.next

  topo_order.insert(0, v)

def process_vertex(v):
  #print v,

def topo_order(graph):
  dfs(graph)
  return topo_order

def main():
  graph = Graph()
  graph.read_from_file('data/tiny_graph.txt')
  graph.print_graph()

  print 'topo order'
  topo_order = topo_order(graph)
  print topo_order

if __name__ == '__main__':
  main()



