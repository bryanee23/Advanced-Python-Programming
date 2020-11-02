from Array import Array
from AbstractSet import AbstractSet

class ArraySet(AbstractSet):
  """
  Methods from AbstractSet: __str__, is_empty, _len__
  """
  DEFAULT_CAPACITY = 10
  def __init__(self, source_collection=None):
      self._items = Array(ArraySet.DEFAULT_CAPACITY)
      AbstractSet.__init__(self, source_collection)

      if source_collection is not None:
        for element in source_collection:
          self.add(element)
          

  def add(self, item):
      """Adds item to ._items array"""
      if item in self:
        print('Duplicate item, item not added')
        pass

      else:
        self._items[self._size] = item
        self._size += 1


  def __iter__(self):
      """Supports iteration over set"""
      cursor = 0
      while cursor < len(self):
          yield self._items[cursor]
          cursor += 1


  def remove(self,item):
      """
          precondition: Item is in self
          raise conditon: Keyerror if item is not in self
          post condition: a single instance of item is removed from self
      """
      if item not in self:
        raise KeyError("Item not in set")

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