from AbstractCollection import AbstractCollection
from Array import Array

class MinHeap(AbstractCollection):

  DEFAULT_CAPACITY = 10

  def __init__(self):
    self._heap = Array(MinHeap.DEFAULT_CAPACITY)
    AbstractCollection.__init__(self)

  def peek(self):
    """ return the root item, which is smallest item"""
    if self.is_empty():
      raise ValueError("Heap is empty")
    return self._heap[0]

  def add(self, item):
    self._heap[self._size] = item
    #create current index of new item
    curr_index = self._size
    # loop until parent is larger or new item is in root
    while curr_index > 0:
      parent_index = (curr_index - 1) //2
      if self._heap[parent_index] <= item:
        break
      else:
        self._heap[curr_index] = self._heap[parent_index]
        self._heap[parent_index] = item
        curr_index = parent_index
    self._size += 1


  def pop(self):
    if self.is_empty():
      raise ValueError("Heap is empty")

    top_item = self._heap[0]
    bottom_item = self._heap[self._size - 1]
    self._size -= 1

    if self.is_empty():
      return bottom_item

    self._heap[0] = bottom_item

    #create a reference to the last index in the array
    last_index = self._size - 1

    #create a reference to the current index
    curr_index = 0

    # in a loop, move teh item to "reheap" down to its correct location
    while True:
      left_child_index = 2 * curr_index + 1
      right_child_index = 2 * curr_index + 2

      if left_child_index > last_index:
        #there is no left child of the current node (therefore no right node either)
        break

      if right_child_index > last_index:
        #must be a right child
        min_child_index = left_child_index
      else:
        #two children check value of both
        left_child = self._heap[left_child_index]
        right_child = self._heap[right_child_index]
        if left_child < right_child:
          min_child_index = left_child_index
        else:
          min_child_index = right_child_index

      min_child = self._heap[min_child_index]

      if bottom_item <= min_child:
        #node smaller than child
        break
      else:
        #item being moved is larger than the min child, swap and continue
        self._heap[curr_index] = min_child
        self._heap[min_child_index] = bottom_item
        curr_index = min_child_index

    return top_item