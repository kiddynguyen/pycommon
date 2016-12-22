#!/usr/bin/python -tt

class Node:
  def __init__(self, vertex, next=None, weight=0):
    self.vertex = vertex  # vertext pos
    self.next = next      # next node

  def __str__(self):
    return str(self.vertex)

class Graph:
  def __init__(self, nvertices=0, nedges=0, directed=False):
    self.nvertices = nvertices
    self.nedges = nedges
    self.directed = directed
    self.edges = [] # adj list of Nodes
    # init adj list
    for v in range(nvertices):
      self.edges.append(None)

  """ Init graph from a file.
  Graph file format:
    nvertices
    nedges
    v_from1 v_to1
    v_from2 v_to2
    ...
    v_fromn v_ton
  """
  def read_from_file(self, filename):
    file = open(filename, 'r')
    # read nvertices and nedges
    self.nvertices = int(file.readline())
    self.nedges = int(file.readline())

    # init adj list
    for i in range(self.nvertices):
      self.edges.append(None)

    # read edges
    for line in file:
      parts = line.split()
      v1 = int(parts[0])
      v2 = int(parts[1])
      self.add_edge(v1, v2)
      if not self.directed:
        self.add_edge(v2, v1)

    file.close()
      
  def add_edge(self, v1, v2):
    node = Node(v2)
    node.next = self.edges[v1]
    self.edges[v1] = node

  def print_graph(self):
    for v in range(self.nvertices):
      print str(v) + ':\t',
      node = self.edges[v]
      while node:
        print node,
        node = node.next
      print
