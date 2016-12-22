#!/usr/bin/python -tt

from bst_tree import Tree

tree = Tree()

def build_minimal_tree(sorted_list):
  if not sorted_list:
    return
  mid = len(sorted_list) / 2
  tree.insert(sorted_list[mid])
  if mid > 0:
    build_minimal_tree(sorted_list[:mid])
  if mid < len(sorted_list):
    build_minimal_tree(sorted_list[mid+1:])


def main():
  list = range(20)
  print 'original list'
  print list

  build_minimal_tree(list)
  print 'inorder from bst'
  tree.inorder_traverse()

if __name__ == '__main__':
  main()
