from AbstractStack import AbstractStack
from Array import Array

class ArrayStack(AbstractStack):
    DEFAULT_CAPACITY = 10

    def __init__(self):
      self._items = Array(self.DEFAULT_CAPACITY)
      AbstractStack.__init__(self)

    def peek(self):
      """
      Sess item at top of stack
      """
      if self.is_empty():
        raise KeyError ("Stack is empty")
      return self._items[self._size -1]

    def push(self, item):
      """Adds item to top of stack"""
      self._items[self._size] = item
      self._size += 1

    def clear(self):
      """clear stack"""
      self._items = Array(self.DEFAULT_CAPACITY)
      self._size = 0


    def pop(self):
      """
      remove and return top element from stack
      Precondition: stack is not empty
      Raises: keyerror if stack is empty
      postcondition: stack is on item shorter
      """
      if self.is_empty():
        raise KeyError("Stack is empty")
      return_item = self._items[self._size -1]
      self._items[self._size -1] = None
      self._size -= 1
      return return_item