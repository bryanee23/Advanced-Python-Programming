from AbstractCollection import AbstractCollection
from Node import Node

class LinkedQueue(AbstractCollection):
    def __init__(self):
      self._front = None
      self._rear = None
      AbstractCollection.__init__(self)

    def add(self, item):
      """adds item to back of queue"""
      node = Node(item)
      if self.is_empty():
        self._front = node
        self._rear = node
      else:
        self._rear.next = node

      self._rear = node
      self._size += 1

    def pop(self):
      """removes front item from queue
      preconditon: queue isn't empty
      raise value error"""

      if self.is_empty():
        raise ValueError("Queue is empty")
      return_item = self._front.data
      self._front = self._front.next
      if self._front is None:
        self._rear = None
      self._size -= 1

      return return_item

    def peek(self):
      """look at front"""
      if self.is_empty():
        raise ValueError("Queue is empty")
      return self._front.data

    def clear(self):
      self._front = None
      self._rear = None
      self._size = 0

    def __iter__(self):
      cursor = self._front
      while cursor is not None:
        yield cursor.data
        cursor = cursor.next