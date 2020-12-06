from Array import Array
from AbstractCollection import AbstractCollection

class ArrayQueue(AbstractCollection):
  def __init__(self, DEFAULT_CAPACITY=None):
    self._items = Array(DEFAULT_CAPACITY)
    self._front = self._rear = self._size = 0
    AbstractCollection.__init__(self)

  def push(self, item):
    """handles the following conditions:
      - empty array
      - full array
      - all other options array
    """
    if self._size == 0:
      self._items[self._rear] = item
      self._rear += 1
      self._size += 1

    elif self._size == len(self._items):
      raise IndexError("Queue is full.")

    else:
      next_rear = self._rear + 1
      if next_rear % len(self._items) == 0:
        self._items[self._rear] = item
        self._rear = next_rear % len(self._items)
      else:
        self._items[self._rear] = item
        self._rear += 1

      self._size += 1

  def pop(self):
    """ handles the following conditions:
      - empty array
      - all other options array
      return popped item
    """
    if self._size == 0:
      raise IndexError("Queue is empty")
    else:
      return_item = self._items[self._front]
      self._items[self._front] = None
      self._front += 1
    self._size -= 1
    return return_item

  def peek(self):
    """ handles the following conditions:
      - empty array
      - all other options array
      returns first item in array
    """
    if self._size == 0:
      raise IndexError("Queue is empty")
    else:
      return self._items[0]


# for testing only
  @property
  def show_array(self):
    return_array = []
    for i in self._items:
      return_array.append(i)
    return return_array