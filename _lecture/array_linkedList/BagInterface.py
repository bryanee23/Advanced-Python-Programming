class BagInterface:
  """interface for all bag types"""

  def __init__(self, source_collection=None):
      pass

  def is_empty(self):
      """returns true if the bag is empty, false if not"""
      return False # returns a boolean

  def add(self):
      """Adds item to self"""
      pass

  def clear(self):
      """Makes self empty"""
      pass

  def remove(self):
      """
          precondition: Item is in self
          raise conditon: Keyerror if item is not in self
          post condition: a single instance of item is removed from self
      """
      pass

  def __len__(self):
      """Returns the length of the bag"""
      return 0 #need to return a number

  def __str__(self):
      """Returns ta string represenation of self"""
      return "" #returns a string

  def __iter__(self):
      """supports iteration over a bag"""
      return None #returns an object

  def __add__(self):
      """Over loads + operator, creates and returns new bag with errthang"""
      return None #returns an object

  def __eq__(self):
      """Overloads = operator"""
      return False #returns a boolean

  def count(self):
      """return number of times item appear in self"""
      return 0



my_list = [5,4,3]
b = ArrayBag(my_list)