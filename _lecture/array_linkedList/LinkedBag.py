from Node import Node
from AbstractBag import AbstractBag

class LinkedBag(AbstractBag):
  """An Linked-based implementation of BagInterface"""

  def __init__(self, source_collection=None):
      self._items = None
      AbstractBag.__init__(self, source_collection)


  def __eq__(self, other):
      """Overloads = operator"""
      if self is other:
        return True
      if len(self) != len(other):
        return False
      for item in self:
        if self.count(item) != other.count(item):
          return False
      return True


  def __iter__(self):
      """supports iteration over a bag"""
      probe = self._items
      while probe is not None:
          yield probe.data
          probe = probe.next

  def clear(self):
      """reset size and create a new array"""
      self._size = 0
      self._items = None



  def add(self, item):
      """Adds item to self"""
      self._items = Node(item, self._items) #Node(value, next item)
      self._size += 1


  def remove(self,item):
      """
          precondition: Item is in self
          raise conditon: Keyerror if item is not in self
          post condition: a single instance of item is removed from self
      """
      if item not in self:
        raise KeyError("Value is not in the bag")

      probe = self._items
      trailer = None
      for i in self:
          if i == item:
              break
          trailer = probe
          probe = probe.next

      if probe == self._items:
          self._items = self._items.next
      else:
        trailer.next = probe.next

      self._size -= 1


