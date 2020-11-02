def test():
  """
  Implement the following methods:
  add (sub class)
  remove (sub class)
  __str__,
  is_empty,
  __len__
  """
  pass

class AbstractSet:
    """Superclass for ArraySet and LinkedSet"""

    def __init__(self, source_collection=None):
        self._size = 0 #logical size


    def __str__(self):
        """Returns ta string represenation of self"""
        return "{" + ", ".join(map(str, self)) + "}"


    def is_empty(self):
        """returns true if the collection is empty, false if not"""
        return len(self) == 0


    def __len__(self):
        """Returns the length of the nuber of items collection"""
        return self._size


