from AbstractSet import AbstractSet
from Node import Node

class LinkedSet(AbstractSet):
  """An Linked-based implementation of BagInterface"""

  def __init__(self, source_collection=None):
      self._items = None
      AbstractSet.__init__(self, source_collection)

      if source_collection is not None:
        for element in source_collection:
          self.add(element)


  def __iter__(self):
      """supports iteration over a bag"""
      probe = self._items
      while probe is not None:
          yield probe.data
          probe = probe.next


  def add(self, item):
      """Adds item to self"""
      if item in self:
        pass
      else:
        self._items = Node(item, self._items)
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