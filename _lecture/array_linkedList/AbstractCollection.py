from Array import Array

class AbstractCollection:
  """An array-based implementation of BagInterface"""

  def __init__(self):
      # check to make sure source_collection has sortable items
      self._size = 0 #logical size tracker

  def is_empty(self):
      """returns true if the collection is empty, false if not"""
      return len(self) == 0


  def __len__(self):
      """Returns the length of the nuber of items collection"""
      return self._size

  def count(self, item):
      """return number of times item appear in self"""
      appearance = 0
      for i in self:
        if item == i:
          appearance += 1
      return appearance
