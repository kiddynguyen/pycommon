#!/usr/bin/python -tt
from graph import Node
from graph import Graph

# breadth first search  
def bfs(graph):
  visited = []
  for v in range(graph.nvertices):
    visited.append(False)

  vroot = 0
  queue = [vroot]
  visited[vroot] = True

  while queue:
    v = queue.pop(0)
    print v,
    neibor_node = graph.edges[v]
    while neibor_node:
      vneibor = neibor_node.vertex
      if not visited[vneibor]:
        queue.append(vneibor)
        visited[vneibor] = True
      neibor_node = neibor_node.next
  print

## main program
def main():
  graph = Graph()
  graph.read_from_file('data/tiny_graph.txt')

  graph.print_graph()

  print "\n---Breadth first search order:"
  bfs(graph)

if __name__ == '__main__':
  main()

