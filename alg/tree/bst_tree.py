#!/usr/bin/python -tt

class Node:

  def __init__(self, key = None, left = None, right = None):
    self.key = key
    self.left = left
    self.right = right

  def __str__(self):
    return str(self.key)

  def __cmp__(self, other):
    if self.key == other.key:
      return 0
    return -1 if self.key < other.key else 1

class Tree:

  def __init__(self, root = None, size = 0):
    self.root = root
    self.size = size

  ## calculate height recursively on node
  def __height(self, node):
    if node is None:
      return 0
    hleft = self.__height(node.left)
    hright = self.__height(node.right)
    return hleft + 1 if hleft > hright else hright + 1

  ## calculate height of tree
  def height(self):
    return self.__height(self.root)

  ## count leaves recursively on node
  def __leaves(self, node):
    if node is None:
      return 0
    if node.left is None and node.right is None:
      return 1
    return self.__leaves(node.left) + self.__leaves(node.right)

  ## count leaves of tree
  def leaves(self):
    return self.__leaves(self.root)

  ## search a key recursively on node
  def __search(self, node, key):
    if node is None:
      return False
    if node.key == key:
      return True
    elif key < node.key:
      return self.__search(node.left, key)
    else:
      return self.__search(node.right, key)

  ## search a key
  def search(self, key):
    return self.__search(self.root, key)

  ## insert a node recursive on node
  def __insert(self, node, key):
    if key <= node.key:
      if node.left is None:
        node.left = Node(key)
      else:
        self.__insert(node.left, key)
    else:
      if node.right is None:
        node.right = Node(key)
      else:
        self.__insert(node.right, key)

  ## insert node to tree
  def insert(self, key):
    if self.root is None:
      self.root = Node(key)
      return
    self.__insert(self.root, key)
    self.size += 1

  def remove(self, key):
    return None

  ## private method
  def __inorder_traverse(self, node):
    if node is None:
      return
    self.__inorder_traverse(node.left)
    print node,
    self.__inorder_traverse(node.right)
  
  def inorder_traverse(self):
    self.__inorder_traverse(self.root)
    print
    
  ## private method
  def __preorder_traverse(self, node):
    if node is None:
      return
    print node
    self.__preorder_traverse(node.left)
    self.__preorder_traverse(node.right)

  ## print tree level by level in one line
  def bf_traverse(self):
    queue = [self.root]
    while len(queue) > 0:
      node = queue.pop(0)
      if node.left:
        queue.append(node.left)
      if node.right:
        queue.append(node.right)
      print node,
    print

  ## print tree level by level
  ## new line for each level
  def bf_traverse2(self):
    curlevel = [self.root]
    nextlevel = []
    while len(curlevel) > 0:
      node = curlevel.pop(0)
      print node,
      if node.left:
        nextlevel.append(node.left)
      if node.right:
        nextlevel.append(node.right)
      # start new level
      if len(curlevel) == 0:
        curlevel = nextlevel
        nextlevel = []
        print

  def print_visual(self):
    print 'TODO'




