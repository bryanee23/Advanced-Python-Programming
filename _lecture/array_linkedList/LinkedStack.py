from Node import Node
from AbstractStack import AbstractStack

class LinkedStack(AbstractStack):
  def __init__(self):
    self._items = None
    self._size = 0
    AbstractStack.__init__(self)

  def clear(self):
    """empty the stack"""
    self._items = None
    self._size = 0

  def push(self, item):
    """add to the head of stack"""
    self._items = Node(item, self._items)
    self._size += 1

  def peek(self):
    """
    Sess item at top of stack
    """
    if self.is_empty():
      raise KeyError ("Stack is empty")
    return self._items.data

  def pop(self):
    if self.is_empty():
      raise KeyError ("Stack is empty")
    return_item = self._items.data
    self._items = self._items.next
    self._size -= 1
    return return_item