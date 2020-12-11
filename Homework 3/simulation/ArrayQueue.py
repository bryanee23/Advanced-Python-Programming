from Array import Array
from AbstractCollection import AbstractCollection

class ArrayQueue(AbstractCollection):

  DEFAULT_CAPACITY = 10
  def __init__(self):
    self._items = Array(self.DEFAULT_CAPACITY)
    self._front = self._rear = self._size = 0
    AbstractCollection.__init__(self)

  def clear(self):
    """ clear array """
    self._items = Array(self.DEFAULT_CAPACITY)
    self._front = self._rear = self._size = 0


  def _expand(self):
    return_array = []
    for i in self._items:
      return_array.append(i)

    double_size = self._size * 2
    for i in range(self._size, double_size):
      return_array.append(None)

    print("Queue is full, array capacity doubled to {}".format(self._size*2))
    return return_array

  def add(self, item):
    """handles the following conditions:
      - empty array
      - full array
      - all other options array
    """
    next_rear = self._rear + 1

    if self._size == 0:
      self._items[self._rear] = item
      self._rear += 1
      self._size += 1

    elif self._size == self.DEFAULT_CAPACITY:
      self._items = self._expand()

      self._rear = self._size
      self._items[self._rear] = item

      self._size += 1
      self._rear += 1

    else:
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

  def __str__(self):
      """Returns ta string represenation of self._items"""
      return "{" + ", ".join(map(str, self._items)) + "}"


# for testing only
  @property
  def show_array(self):
    return_array = []
    for i in self._items:
      return_array.append(i)
    return return_array