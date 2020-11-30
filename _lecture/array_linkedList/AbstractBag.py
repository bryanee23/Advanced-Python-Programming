from Array import Array
from AbstractCollection import AbstractCollection

class AbstractBag(AbstractCollection):

  def __init__(self, source_collection=None):
      AbstractCollection.__init__(self)
      # if source_collection exists
      if source_collection is not None:
        for item in source_collection:
          self.add(item)

  def __str__(self):
      """Returns ta string represenation of self"""
      return "{" + ", ".join(map(str, self)) + "}"

  def __add__(self, other):
      """Over loads + operator, creates and returns new bag with errthang"""
      return_bag = type(self)(self)
      #evaluates type then calls it w/self as a param linkedbag(self)
      for i in other:
        return_bag.add(i)
      return return_bag #returns an object

  def __eq__(self, other):
      """Overloads = operator"""
      if self is other:
        return True
      if len(self) != len(other):
        return False
      for i in self:
        if self.count(i) != other.count(i):
          return False
      return True
