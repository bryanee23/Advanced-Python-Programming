import unittest, random
from LinkedQueue import LinkedQueue
from LinkedBST import LinkedBST

class Test(unittest.TestCase):
  def test_1(self):
    tree = LinkedBST()


# replace Test() w/ Test(unittest.TestCase) to run
class Test():
  def test_1(self):
    """ test connection """
    tree = LinkedBST()
    self.assertEqual(tree.is_empty(), True)
    tree.add(random.randrange(5,6))
    tree.add(random.randrange(3,5))
    tree.add(random.randrange(4,7))
    tree.inorder()
    self.assertEqual(len(tree), 3)

  def test_2(self):
    """ local test """
    tree = LinkedBST()
    tree.add(4)
    tree.add(3)
    tree.add(4)
    tree.add(2)
    tree.add(5)
    tree.preorder()
    tree.find(5) # prints 1 node visited
    tree.find(2) # prints 2 node visited
    tree.find(0) # prints 2 node visited

  def test_2(self):
    """ ran random test then replaced for local test """
    tree = LinkedBST()
    # tree.add(random.randrange(3,6))
    # tree.add(random.randrange(3,5))
    # tree.add(random.randrange(1,3))
    # tree.add(random.randrange(4,7))
    # tree.add(random.randrange(0,9))
    tree.add(5)
    tree.add(3)
    tree.add(1)
    tree.add(1)
    tree.add(6)
    tree.preorder()
    tree.find(5) # prints 0 node visited
    tree.find(1) # prints 2 node visited
    tree.find(0) # prints 3 node visited
    tree.find(6) # prints 1 node visited









if __name__ == "__main__":
  unittest.main()