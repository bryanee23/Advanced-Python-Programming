from Array import Array
from AbstractBag import AbstractBag

class ArrayBag(AbstractBag):
  """An array-based implementation of BagInterface"""

  DEFAULT_CAPACITY = 10
  def __init__(self, source_collection=None):
      self._items = Array(ArrayBag.DEFAULT_CAPACITY)
      AbstractBag.__init__(self, source_collection)

  def add(self, item):
      """Adds item to self"""
      self._items[self._size] = item #adds item via indexing
      self._size += 1

  def clear(self):
      """reset size and create a new array"""
      self._size = 0
      self._items = Array(ArrayBag.DEFAULT_CAPACITY)

  def remove(self,item):
      """
          precondition: Item is in self
          raise conditon: Keyerror if item is not in self
          post condition: a single instance of item is removed from self
      """
      if item not in self:
        raise KeyError("Value is not in the bag")

      target_index = 0
      index_found = False
      while not index_found:
        if self._items[target_index] == item:
          index_found = True
        else:
          target_index += 1

      for target_index in range(target_index, len(self)-1):
        self._items[target_index] = self._items[target_index+1]

      self._size -= 1
      self._items[self._size] = None

  def __iter__(self):
      """supports iteration over a bag"""
      cursor = 0
      while cursor < len(self):
          yield self._items[cursor]
          cursor += 1
