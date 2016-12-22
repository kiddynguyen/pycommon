#!/usr/bin/python -tt
from bst_tree import Tree
from bst_tree import Node

def main():
  tree = Tree()  
  tree.insert(5)
  tree.insert(2)
  tree.insert(10)
  tree.insert(1)
  tree.insert(3)
  tree.insert(100)
  tree.insert(50)
  tree.insert(-1)
  tree.inorder_traverse()
  tree.bf_traverse()
  tree.bf_traverse2()
 
if __name__ == '__main__':
  main()
