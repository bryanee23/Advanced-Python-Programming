import unittest, random
from LinkedQueue import LinkedQueue
from LinkedBST import LinkedBST
from BinaryNode import BinaryNode


# replace Test_3() w/ Test_3(unittest.TestCase) to run
class Test_3(unittest.TestCase):
  """ unittest.TestCase super class removed to prevent output congestion in terminal"""

  def test_3a(self):
    tree = LinkedBST()
    tree.add(4)
    tree.add(2)
    tree.add(5)
    tree.bfs_akabreakfast()




# replace Test_2() w/ Test_2(unittest.TestCase) to run
class Test_2(unittest.TestCase):
  """ unittest.TestCase super class removed to prevent output congestion in terminal"""

  def test_2a(self):
    """ local tests to node height method """
    tree = LinkedBST()
    tree.add(4)
    tree.add(3)
    self.assertEqual(tree.height_from_node(), 2)
    tree.add(2)
    self.assertEqual(tree.height_from_node(), 3)

  def test_2b(self):
    """ randomized test for verification """
    tree = LinkedBST()
    # tree.add(random.randrange(3,6))
    # tree.add(random.randrange(3,5))
    # tree.add(random.randrange(1,3))
    # tree.add(random.randrange(4,7))
    # tree.add(random.randrange(0,9))
    tree.add(3)
    tree.add(2)
    tree.add(3)
    tree.add(5)
    tree.add(6)
    # tree.preorder()
    self.assertEqual(tree.height_from_node(), 4)


# replace Test_1() w/ Test_1(unittest.TestCase) to run
class Test_1():
  """ unittest.TestCase super class removed to prevent output congestion in terminal"""

  def test_1a(self):
    """ test connection """
    tree = LinkedBST()
    self.assertEqual(tree.is_empty(), True)
    tree.add(random.randrange(5,6))
    tree.add(random.randrange(3,5))
    tree.add(random.randrange(4,7))
    tree.inorder()
    self.assertEqual(len(tree), 3)

  def test_1b(self):
    """ local test """
    tree = LinkedBST()
    tree.add(4)
    tree.add(3)
    tree.add(4)
    tree.add(2)
    tree.add(5)
    print("\n\n Question 1 ")
    tree.preorder()
    tree.find(5) # prints 1 node visited
    tree.find(2) # prints 2 node visited
    tree.find(0) # prints 2 node visited

  def test_1c(self):
    """ ran random numbers then replaced to verify """
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
    # tree.preorder() # test random generated tree
    tree.find(5) # prints 0 node visited
    tree.find(1) # prints 2 node visited
    tree.find(0) # prints 3 node visited
    tree.find(6) # prints 1 node visited


if __name__ == "__main__":
  unittest.main()