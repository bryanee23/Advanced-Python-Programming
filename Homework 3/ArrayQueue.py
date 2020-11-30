from Array import Array
from AbstractCollection import AbstractCollection

class ArrayQueue(AbstractCollection):
  def __init__(self, DEFAULT_CAPACITY=None):
    self._items = Array(DEFAULT_CAPACITY)
    self._front = 0
    self._rear = 0
    AbstractCollection.__init__(self)


  def push(self, item):
    """Adds item to the rear of array"""
    if self._rear == len(self._items):
      self._front = 0
      self._items[self._front] = item
      self._rear = (self._rear + 1) % len(self._items)
    else:
      self._items[self._rear] = item
      self._rear += 1

    self._size += 1

  def pop(self):
    """removes front item from queue
    preconditon: queue isn't empty
    raise value error"""
    if self.is_empty():
      raise ValueError("Queue is empty")

    return_item = self._items[self._front]
    self._front += 1

    if self._front + 1 == len(self._items):
      self._items[self._front-1] = None
      self._size -= 1
    else:
      self._items[self._front -1] = None
      self._size -= 1

    if self._front == len(self._items) and self.is_empty():
      self._front = 0
      self._rear = 0

    return return_item

  @property
  def show_array(self):
    return_array = []
    for i in self._items:
      return_array.append(i)
    return return_array

  @property
  def get_front_value(self):
    return self._front

  @property
  def get_rear_value(self):
    return self._rear