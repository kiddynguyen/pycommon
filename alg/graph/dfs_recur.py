#!/usr/bin/python -tt

from graph import Node
from graph import Graph

discovered = []

def dfs_visit(graph, vertex):
  process_vertex(vertex)
  discovered[vertex] = True

  neibors = graph.edges[vertex]
  while neibors:
    vneibor = neibors.vertex
    if not discovered[vneibor]:
      dfs_visit(graph, vneibor)
    neibors = neibors.next

def dfs(graph):
  for v in range(graph.nvertices):
    discovered.append(False)
  for v in range(graph.nvertices):
    if not discovered[v]:
      dfs_visit(graph, v)

def process_vertex(vertex):
  print vertex,

def process_edge(v1, v2):
  return

def main():
  graph = Graph()
  graph.read_from_file('data/tiny_graph.txt')
  graph.print_graph()
  
  print '\n--- DFS using Recursion'
  dfs(graph)

if __name__ == '__main__':
  main()
