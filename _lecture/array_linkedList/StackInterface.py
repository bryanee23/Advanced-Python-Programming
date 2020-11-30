class StackInterface:
  """interface for all stack types"""

  # constructor
  def __init__(self, source_collection=None):
      pass

  def is_empty(self):
      """returns true if the bag is empty, false if not"""
      return False # returns a boolean

  def __str__(self):
      """Returns ta string represenation of self"""
      return "" #returns a string

  def clear(self):
      """Makes self empty"""
      pass

  def pop(self):
      """
      Pre-condition: if empty, throw error
      Post-condition: Top item of stack is removed, stack has less item
      remove and return top item from stack
      """
      return None

  def peek(self):
      """
      Pre-condition: if empty, throw error
      Post-condition: Top item of stack is removed, stack has less item
      Return the top item from statck
      """
      return None

  def push(self):
    """
    adds item on el top
    """
    pass