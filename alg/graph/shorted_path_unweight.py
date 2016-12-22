#!/usr/bin/python -tt

from graph import Node
from graph import Graph

# breadth first search on 'graph' started from 'root'
# return parents tracer
def bfs(graph, root):
  parents = []
  visited = []
  # init visited & parents lists
  for i in range(graph.nvertices):
    visited.append(False)
    parents.append(-1)

  queue = [root]
  visited[root] = True
  while queue:
    v = queue.pop(0)
    neibor = graph.edges[v]
    while neibor:
      vneibor = neibor.vertex
      if not visited[vneibor]:
        queue.append(vneibor)
        visited[vneibor] = True
        parents[vneibor] = v
      neibor = neibor.next
  return parents

def find_shorted_path(graph, start, end):
  parents = bfs(graph, start)
  return _find_shorted_path(start, end, parents)
  # OR
  # path = []
  # _find_shorted_path_recur(start, end, parents, path)
  # return path

# use stack
def _find_shorted_path(start, end, parents):
  path = []
  path.insert(0, end)
  while end != start:
    end = parents[end]
    path.insert(0, end)
  return path

def _find_shorted_path_recur(start, end, parents, path):
  if end == start:
    path.append(start)
  else:
    parent = parents[end]
    _find_shorted_path_recur(start, parent, parents, path)
    path.append(end)

def main():
  graph = Graph()
  graph.read_from_file('data/tiny_graph.txt')
  graph.print_graph()
  
  print 'SHORTED PATH:'
  path = find_shorted_path(graph, 0, 3)
  print path
if __name__ == '__main__':
  main()


