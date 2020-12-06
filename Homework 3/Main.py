from ArrayQueue import ArrayQueue
import unittest

class Test_Cases_ArraySet(unittest.TestCase):
  def test_initialize(self):
    """create an array w/ default size of 4"""
    test = ArrayQueue()
    self.assertEqual(test.show_array, [None, None, None, None, None, None, None, None, None, None])

  def test_push(self):
    test = ArrayQueue()
    test.push(1)
    self.assertEqual(test.show_array, [1, None, None, None, None, None, None, None, None, None])

  def test_clear(self):
    test = ArrayQueue()
    test.push(1)
    test.push(2)
    test.push(3)
    self.assertEqual(test.show_array, [1, 2, 3, None, None, None, None, None, None, None])
    test.clear()
    self.assertEqual(test.show_array, [None, None, None, None, None, None, None, None, None, None])

  def test_clearPush(self):
    test = ArrayQueue()
    test.push(1)
    test.push(2)
    test.push(3)
    self.assertEqual(test.show_array, [1, 2, 3, None, None, None, None, None, None, None])
    test.clear()
    self.assertEqual(test.show_array, [None, None, None, None, None, None, None, None, None, None])
    test.push('a')
    test.push('b')
    test.pop()
    self.assertEqual(test.show_array, [None, 'b', None, None, None, None, None, None, None, None])

  def test_peek(self):
    test = ArrayQueue()
    test.push(1)
    self.assertEqual(test.peek(), 1)

  def test_pushToCapacity(self):
    """ Fill entire array """
    test = ArrayQueue()
    for i in range(1, 11):
      test.push(i)
    self.assertEqual(test.show_array, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

  def test_pop(self):
    """ pop once """
    test = ArrayQueue()
    test.push(1)
    test.push(2)
    popped = test.pop()
    self.assertEqual(popped, 1)

  def test_popEmpty(self):
    """Try pop on empty array"""
    test = ArrayQueue()
    test.pop()
    self.assertRaises(test.pop(), Exception)

  def test_popAll(self):
    """ pop all elements"""
    test = ArrayQueue()
    test.push(1)
    test.push(2)
    test.push(3)
    test.push(4)
    test.pop()
    test.pop()
    test.pop()
    test.pop()
    self.assertEqual(test.show_array, [None, None, None, None, None, None, None, None, None, None])

  def test_random(self):
    """random push/pops"""
    test = ArrayQueue()
    for i in range(1, 11):
      test.push(i)
    for i in range(1, 11):
      test.pop()
    test.push('a')
    test.push('b')
    self.assertEqual(test.show_array, ['a', 'b', None, None, None, None, None, None, None, None])

  def test_random2(self):
    """random push/pops v.2"""
    test = ArrayQueue()
    test.push(1)
    test.push(2)
    test.push(3)
    test.push(4)
    test.pop()
    test.pop()
    test.pop()
    test.push('a')
    test.push('b')
    self.assertEqual(test.show_array, [None, None, None, 4, 'a', 'b', None, None, None, None])

  def test_randomForFun(self):
    """random push/pops v.3, just making sure"""
    test = ArrayQueue()
    for i in range(1, 11):
      test.push(i)
    test.pop()
    test.pop()
    test.push('a')
    self.assertEqual(test.show_array, ['a', None, 3, 4, 5, 6, 7, 8, 9, 10])

  def test_expandWhenFull(self):
    """when size of array is at capacity, double array"""
    test = ArrayQueue()
    for i in range(1, 11):
      test.push(i)
    self.assertEqual(test.show_array, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    test.push(11)
    self.assertEqual(test.show_array, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, None, None, None, None, None, None, None, None, None])

if __name__ == '__main__':
    unittest.main()