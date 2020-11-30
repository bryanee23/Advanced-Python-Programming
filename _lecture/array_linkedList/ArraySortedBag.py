from Array import Array
from ArrayBag import ArrayBag

class ArraySortedBag(ArrayBag):
  """An array-based implementation of BagInterface"""

  def __init__(self, source_collection=None):
      # check to make sure source_collection has sortable items
      ArrayBag.__init__(self, source_collection)


  def add(self, item):
      """
      Adds item to self in acesending order
      Loop from end of array, shifting everything from final valid index
      to target index one indext to the right
      Place item in target index (and increase self._size)
      """
      if self.is_empty() or (self._items[len(self) -1] <= item):
        ArrayBag.add(self, item)
        return

      target_index = 0
      for i in range(len(self)):
        if self._items[i] > item:
          target_index = i
          break

      for i in range(len(self)-1, target_index-1, -1):
        self._items[i + 1] = self._items[i]

      self._items[target_index] = item
      self._size += 1

