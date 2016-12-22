#!/usr/bin/python -tt

from bst_tree import Tree

""" Build a BST with min height from a sorted list
"""
def build_minimal_tree(sorted_list, tree):
  if not sorted_list:
    return
  mid = len(sorted_list) / 2
  tree.insert(sorted_list[mid])
  if mid > 0:
    build_minimal_tree(sorted_list[:mid], tree)
  if mid < len(sorted_list):
    build_minimal_tree(sorted_list[mid+1:], tree)

  return tree

def main():
  list = range(20)
  print 'original list'
  print list

  tree = Tree()
  build_minimal_tree(list, tree)
  print 'inorder from bst'
  tree.inorder_traverse()

if __name__ == '__main__':
  main()
