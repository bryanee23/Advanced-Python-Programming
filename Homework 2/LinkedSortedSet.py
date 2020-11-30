from LinkedSet import LinkedSet
from Node import Node

class LinkedSortedSet(LinkedSet):
  def __init__(self, source_collection=None):
      LinkedSet.__init__(self, source_collection)


  def add(self, item):
      """Adds item to self"""
      if self.is_empty():
        self._items = Node(item, self._items)
        self._size += 1

      if item in self:
        pass
      else:
        probe = self._items
        trailer = None

        while probe.next is not None:
  
          if item > probe.data:
            if trailer is not None:
              trailer.next = Node(item, self._items)
              trailer.next.next = probe
              self._items = trailer
              self._size += 1
              break
            else:
              trailer = Node(item, self._items)
              self._items = trailer
              self._size += 1
              break

          trailer = probe
          probe = probe.next

        if probe.next == None and item < probe.data:
          trailer = probe
          probe.next = Node(item, self._items)
          probe.next.next = None
          self._size += 1

        if probe.next == None and item > probe.data:
          probe = Node(item, self._items)
          self._items = probe
          self._size += 1

