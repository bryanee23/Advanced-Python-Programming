# rear = (rear + 1)% len(items)
# array is full? self._size == len(array)
#size and length are the same
#how to write a function to iterate over the ar

self.front = 0
self.rear =
def pop(self):
  # increment front


  We need to increment rear in the add method and
  front in the pop method

  class test:
  def __init__(self):
    self.front = 0
    self.rear = self.front + 1
    self.array = []

  def add(self, value):
    self.array.append(value)

    if self.rear == len(self.array):
      self.rear = (self.rear + 1) % len(self.array)
    else:
      self.rear += 1

    print("array: {}, rear: {}, length: {}".format(self.array, self.rear, len(self.array)))

a = test()
a.add(1)
a.add(1)
a.add(1)