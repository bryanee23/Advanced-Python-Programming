from AbstractCollection import AbstractCollection
from BinaryNode import BindaryNode

class LinkedBST(AbstractCollection):
  """ a linked version of a binary tree"""
  def __init__(self):
    self._root = None
    AbstractCollection.__init__(self)

  def add(self, item):
    # """ adds item to teh bst"""
    def recurse(node):
      # """ inner function to find a new it'sm locaiton in the tree"""
      if item < node.data:
        if node._left is None:
          node._left = BindaryNode(item)
        else:
          recurse(node._left)
      elif item >= node.data:
        if node._right is None:
          node._right = BindaryNode(item)
        else:
          recurse(node._right)
    if self.is_empty():
      self._root = BindaryNode(item)
    else:
      recurse(self._root)

    self._size += 1


  def find(self, item):
    def recurse(node):
      #base cases
      if node is None:
        return None
      elif node.data == item:
        return node.data
      #recursive cases
      elif item < node.data:
        return recurse(node._left)
      else:
        return recurse(node._right)


    return recurse(self._root)

  # def inorder(self):
  #   def recurse(node):
  #     recurse