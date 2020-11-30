from LinkedQueue import LinkedQueue
from Node import Node

class LinkedPriorityQueue(LinkedQueue):
  def __init__(self):
    LinkedQueue.__init__(self)

  def add(self, item):

    if self.is_empty() or self._rear.data <= item:
      LinkedQueue.add(self, item)

    else:
      probe = self._front
      while probe.data < item:
        trailer = probe
        probe = probe.next

      new_node = Node(item, probe)
      if probe == self._front:
        self._front = new_node
      else:
        trailer.next = new_node

    self._size += 1
