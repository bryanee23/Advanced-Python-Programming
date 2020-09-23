"""
1. Add an instance variable named logical_size which track the logical size of the array. A getter method should be written to return this value to the client. Note: The len function should still return the array's physical size.

2. Make the following changes to __setitem__:
  -- If the user tries to update an index further than the first logically empty index of the array, raise an error.

  -- If the user tries to set an index to None, make sure it is the last logically filled index of the array. i.e. if the array has 3 indexes with valid data in them, do not allow the user to say array[1] = None

3. Add the method __eq__ to the Array class. Python runs this method when an Array object appears as the left operand of the == operator. The method returns True
if its argument is also an Array,
it has the same logical size as the left operand, and the
items at each corresponding logical index in both Arrays are equal.
Otherwise it returns False
"""

from array import Array

def problem_1_script():
  DEFAULT_CAPACITY = 10
  logical_size = 0
  a = Array(DEFAULT_CAPACITY)

  a[logical_size] = 88
  logical_size += 1

  a[logical_size] = 3
  logical_size += 1

  a[logical_size] = 'cat'
  logical_size += 1

  a[logical_size] = 'NotCat'
  logical_size += 1

  print("\n\nAnswer to prompt #1")
  print("Array contents: {}".format(a))
  print("Length call: {}, should equal 10".format(len(a)))
  print("Get_local_func: {}, should equal 4".format(a.get_logical_size()))
  print("Length of logical_size: {}, should equal 4".format(len(a.logical_size)))



def problem_2_script():
  print("Answer to prompt #2")
  DEFAULT_CAPACITY = 3
  logical_size = 0
  a = Array(DEFAULT_CAPACITY)

  # valid operations
  a[DEFAULT_CAPACITY - 3] = 88 # output = [88, 'None', 'None']
  a[DEFAULT_CAPACITY - 2] = 4  # output = [88, 4, 'None']
  a[DEFAULT_CAPACITY - 1] = "chair" # [88, 4, 'chair']

  # Invalid Ops
  # a[DEFAULT_CAPACITY + 1] = "book" # index out of range
  # a[DEFAULT_CAPACITY - 1] = None # invalid location of None



def problem_3_script():
  print("Answer to prompt #3")

  # build array A
  DEFAULT_CAPACITY = 2
  logical_size = 0
  a = Array(DEFAULT_CAPACITY)
  a[DEFAULT_CAPACITY - 2] = 1
  a[DEFAULT_CAPACITY - 1] = 'socks'
  print("Array A - get_local_func: {}, should equal 2\n".format(a.get_logical_size()))


  # build array B
  b = Array(DEFAULT_CAPACITY)
  b[DEFAULT_CAPACITY - 2] = 1
  b[DEFAULT_CAPACITY - 1] = 'socks'
  print("Array B - get_local_func: {}, should equal 2\n".format(b.get_logical_size()))

  # build array C
  c = Array(DEFAULT_CAPACITY + 1)
  c[DEFAULT_CAPACITY - 2] = 9999
  c[DEFAULT_CAPACITY - 1] = 'gloves'
  c[DEFAULT_CAPACITY - 0] = 'mittens'
  print("Array C - get_local_func: {}, should equal 3\n".format(c.get_logical_size()))

  # build array D
  d = Array(DEFAULT_CAPACITY)
  d[DEFAULT_CAPACITY - 2] = 1 # [100, None]
  print("Array D - get_local_func: {}, should equal 2\n".format(d.get_logical_size()))

  e = list([1, 'socks'])

  # Overloading equals}
  print('Is {} equal to {}? Answer: {}'.format(a, b, a == b)) # Equals True
  print('Is {} or {} equal to {}? Answer: {}'.format(a, b, c, a == c, b == c)) # Equals False
  print('Is {} equal to {}? Answer: {}'.format(b, d, b == d)) # Equals False
  print('Is {} equal to {}? Answer: {}'.format(type(a), type(e), a == e)) # Equals False



#################################
###### Run scripts
#################################
problem_1_script()
problem_2_script()
problem_3_script()