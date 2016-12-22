#!/usr/bin/python -tt

from graph import Graph

discovered = []

def dfs_visit(graph, vertex):
  stack = [vertex]
  discovered[vertex] = True
  while stack:
    v = stack.pop(0)
    process_vertex(v)
    neibors = graph.edges[v]
    while neibors:
      vneibor = neibors.vertex
      if not discovered[vneibor]:
        stack.insert(0, vneibor)
        discovered[vneibor] = True
      neibors = neibors.next 

def dfs(graph):
  for v in range(graph.nvertices):
    discovered.append(False)
  # loop over all vertice and call dfs_visit to make sure
  # not missing unconnected vertices
  for v in range(graph.nvertices):
    if not discovered[v]:
      dfs_visit(graph, v)

def process_vertex(vertex):
  print vertex,

def main():
  graph = Graph()
  graph.read_from_file('data/tiny_graph.txt')
  graph.print_graph()

  print '\n --- DFS using Stack'
  dfs(graph)

if __name__ == '__main__':
  main()
