from ArrayQueue import ArrayQueue
import unittest

class Test_Cases_ArraySet(unittest.TestCase):
  def test_initialize(self):
    "create an array w/ default size of 4"
    test = ArrayQueue(4)
    self.assertEqual(test.get_front_value, 0)
    self.assertEqual(test.get_rear_value, 0)
    self.assertEqual(test.show_array, [None, None, None, None])

  def test_push1(self):
    test = ArrayQueue(4)
    test.push(1)
    self.assertEqual(test.show_array, [1, None, None, None])

  def test_push4(self):
    "fill entire array"
    test = ArrayQueue(4)
    test.push(1)
    test.push(2)
    test.push(3)
    test.push(4)
    self.assertEqual(test.get_front_value, 0)
    self.assertEqual(test.get_rear_value, 4)
    self.assertEqual(test.show_array, [1, 2, 3, 4])

  def test_push5(self):
    "test circular push"
    test = ArrayQueue(4)
    test.push(1)
    test.push(2)
    test.push(3)
    test.push(4)
    test.push('a')
    self.assertEqual(test.get_front_value, 0)
    self.assertEqual(test.get_rear_value, 1)
    self.assertEqual(test.show_array, ['a', 2, 3, 4])

  def test_pop(self):
    "remove from front, increment front pointer"
    test = ArrayQueue(4)
    test.push(1)
    test.push(2)
    test.push(3)
    test.push(4)
    popped = test.pop()
    self.assertEqual(popped, 1)
    self.assertEqual(test.get_front_value, 1)
    self.assertEqual(test.get_rear_value, 4)
    self.assertEqual(test.show_array, [None, 2, 3, 4])

  def test_pop(self):
    "remove from front, increment front pointer"
    test = ArrayQueue(4)
    test.push(1)
    test.push(2)
    test.push(3)
    test.push(4)
    test.pop()
    test.pop()
    test.pop()
    popped = test.pop()
    self.assertEqual(popped, 4)
    self.assertEqual(test.get_front_value, 0)
    self.assertEqual(test.get_rear_value, 0)
    self.assertEqual(test.show_array, [None, None, None, None])

  def test_combo_pushpop(self):
    "random push and pop"
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

  def test_combo_pushpop2(self):
    "random push and pop"
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
    test.pop()
    self.assertEqual(test.show_array, [None, 'b', None, 4])

  def test_combo_pushpop3(self):
    "random push and pop"
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
    test.pop()
    test.push(1)
    self.assertEqual(test.show_array, [None, 'b', 1, 4])

  def test_combo_pushpop4(self):
    "random push and pop"
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

  def test_combo_pushpop5(self):
    "logic fails on last push, replaces last index"
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
    test.pop()
    test.push(1)
    test.push(2)
    self.assertEqual(test.show_array, [2, 'b', 1, 4])



if __name__ == '__main__':
    unittest.main()