#!/usr/bin/python -tt

class Node:

  def __init__(self, data = None, left = None, right = None):
    self.data = data
    self.left = left
    self.right = right

  def __str__(self):
    return str(self.data)

  def __cmp__(self, other):
    if self.data == other.data:
      return 0
    return -1 if self.data < other.data else 1

class BstTree:

  def __init__(self, root = None, size = 0):
    self.root = root
    self.size = size

  def __height(self, node):
    if node is None:
      return 0
    hleft = self.__height(node.left)
    hright = self.__height(node.right)
    return hleft + 1 if hleft > hright else hright + 1

  def height(self):
    return self.__height(self.root)

  def __leaves(self, node):
    if node is None:
      return 0
    if node.left is None and node.right is None:
      return 1
    return self.__leaves(node.left) + self.__leaves(node.right)

  def leaves(self):
    return self.__leaves(self.root)

  def __search(self, node, data):
    if node is None:
      return False
    if node.data == data:
      return True
    elif data < node.data:
      return self.__search(node.left, data)
    else:
      return self.__search(node.right, data)

  def search(self, data):
    return self.__search(self.root, data)

  def __insert(self, node, data):
    if data <= node.data:
      if node.left is None:
        node.left = Node(data)
      else:
        self.__insert(node.left, data)
    else:
      if node.right is None:
        node.right = Node(data)
      else:
        self.__insert(node.right, data)

  def insert(self, data):
    if self.root is None:
      self.root = Node(data)
      return
    self.__insert(self.root, data)
    self.size += 1

  def remove(self, data):
    return None

  ## private method
  def __inorder_traverse(self, node):
    if node is None:
      return
    self.__inorder_traverse(node.left)
    print node
    self.__inorder_traverse(node.right)
  
  def inorder_traverse(self):
    self.__inorder_traverse(self.root)
    
  ## private method
  def __preorder_traverse(self, node):
    if node is None:
      return
    print node
    self.__preorder_traverse(node.left)
    self.__preorder_traverse(node.right)

  def print_visual(self):
    print 'TODO'
