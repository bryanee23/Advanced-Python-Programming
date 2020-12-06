from ArrayQueue import ArrayQueue
import unittest

class Test_Cases_ArraySet(unittest.TestCase):
  def test_initialize(self):
    "create an array w/ default size of 4"
    test = ArrayQueue(4)
    self.assertEqual(test.show_array, [None, None, None, None])

  def test_pushTest(self):
    test = ArrayQueue(4)
    test.push(1)
    self.assertEqual(test.show_array, [1, None, None, None])

  def test_pushCapacity(self):
    """ Fill entire array """
    test = ArrayQueue(4)
    test.push(1)
    test.push(2)
    test.push(3)
    test.push(4)
    self.assertEqual(test.show_array, [1, 2, 3, 4])

  def test_pushFull(self):
    """ Can't fill a full array """
    test = ArrayQueue(4)
    test.push(1)
    test.push(2)
    test.push(3)
    test.push(4)
    self.assertRaises(test.push(5), Exception)

  def test_pop(self):
    """ pop once """
    test = ArrayQueue(4)
    test.push(1)
    test.push(2)
    test.push(3)
    test.push(4)
    popped = test.pop()
    self.assertEqual(popped, 1)

  def test_popEmpty(self):
    """ Can't pop when array is empty"""
    test = ArrayQueue(4)
    test.pop()
    self.assertRaises(test.pop(), Exception)

  def test_popAll(self):
    """ pop all """
    test = ArrayQueue(4)
    test.push(1)
    test.push(2)
    test.push(3)
    test.push(4)
    test.pop()
    test.pop()
    test.pop()
    test.pop()
    self.assertEqual(test.show_array, [None, None, None, None])

  def test_random(self):
    test = ArrayQueue(4)
    test.push(1)
    test.push(2)
    test.push(3)
    test.push(4)
    test.pop()
    test.pop()
    test.pop()
    test.pop()
    test.push('a')
    test.push('b')
    self.assertEqual(test.show_array, ['a', 'b', None, None])

  def test_random2(self):
    test = ArrayQueue(4)
    test.push(1)
    test.push(2)
    test.push(3)
    test.push(4)
    test.pop()
    test.pop()
    test.pop()
    test.push('a')
    test.push('b')
    self.assertEqual(test.show_array, ['a', 'b', None, 4])

  def test_randomForFun(self):
    test = ArrayQueue(4)
    test.push(1)
    test.push(2)
    test.push(3)
    test.pop()
    test.pop()
    test.push('a')
    test.push('b')
    self.assertEqual(test.show_array, ['b', None, 3, 'a'])

if __name__ == '__main__':
    unittest.main()