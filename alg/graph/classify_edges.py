#!/usr/bin/python -tt
from graph import Graph

""" 
Classify edges for directed graph. There are 4 classes:
  - Tree edge
  - Forward edge
  - Back edge
  - Cross edge
Use Depth First Search
"""

# Edge classes
TREE_EDGE 	= 'TREE_EDGE'
FORWARD_EDGE 	= 'FORWARD_EDGE'
BACK_EDGE 	= 'BACK_EDGE'
CROSS_EDGE 	= 'CROSS_EDGE'

# use dict instead of array for more convinient
discovered = {}  # track which node is discovered
parent = {}      # track parent of nodes in discovered order
entry = {}       # track time a node start to be processed
exit = {}        # track time a node finish processed

def classify_edge(graph, vfrom, vto):
  # do DFS first
  dfs(graph)

  if parent[vto] == vfrom:
    return TREE_EDGE
  if entry[vfrom] < entry[vto] and exit[vfrom] > exit[vto]:
    return FORWARD_EDGE
  if entry[vfrom] > entry[vto] and exit[vfrom] < exit[vto]:
    return BACK_EDGE
  return CROSS_EDGE

def dfs(graph):
  for v in range(graph.nvertices):
    discovered[v] = False
    parent[v] = None
  for v in range(graph.nvertices):
    if not discovered[v]:
      dfs_visit(graph, v)
  print

time = 0 # time clock used in entry and exit

def dfs_visit(graph, v):
  global time
  process_vertex(v)
  discovered[v] = True
  time += 1
  entry[v] = time
  neibors = graph.edges[v]
  while neibors:
    vneibor = neibors.vertex
    if not discovered[vneibor]:
      parent[vneibor] = v
      dfs_visit(graph, vneibor)
    neibors = neibors.next
  time += 1
  exit[v] = time

def process_vertex(v):
  print v,

def main():
  graph = Graph(0,0,True)
  graph.read_from_file('data/tiny_graph.txt')
  graph.print_graph()

  #print 'DFS:'
  #dfs(graph)
  # test classify edge
  vfrom = 9
  vto = 12
  edge_class = classify_edge(graph, vfrom, vto)
  print 'Edge %d-%d is'%(vfrom,vto), edge_class

if __name__ == '__main__':
  main()
