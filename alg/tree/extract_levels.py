#!/usr/bin/python -tt

from bst_tree import Tree
from minimal_tree import build_minimal_tree

""" Return a list of lists which each contains nodes in each level of a binary tree
"""
def extract_levels(tree):
  levels = []
  curlevel = [tree.root]
  levels.append(curlevel[0:])

  nextlevel = []
  while curlevel:
    node = curlevel.pop(0)
    if node.left:
      nextlevel.append(node.left)
    if node.right:
      nextlevel.append(node.right)
    
    if not curlevel:
      curlevel = nextlevel
      levels.append(curlevel[0:])
      nextlevel = []

  return levels

def main():
  list = range(31)
  tree = Tree()
  build_minimal_tree(list, tree)
  print 'inorder traversal of tree'
  tree.inorder_traverse()

  levels = extract_levels(tree)
  print 'tree levels'
  for level in levels:
    for node in level:
      print node.key,
    print
  
if __name__ == '__main__':
  main()
