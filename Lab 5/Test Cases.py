from LinkedStack import LinkedStack
import unittest

class test_method:
  # self parameter needed for testing code
  def check_palindrome(self, input_string):
    stack = LinkedStack()
    end = len(input_string)
    mid_point = len(input_string) // 2
    even_number = 0

    for i in range(0, mid_point):
      stack.push(input_string[i])

    if len(input_string)%2 == even_number:
      for i in range(mid_point, end):
        if input_string[i] != stack.pop():
          return False
    else:
      for i in range(mid_point + 1, end):
        if input_string[i] != stack.pop():
          return False

    return True

class Test_Cases_ArraySet(unittest.TestCase):
    def test_1(self):
      """
      Test to verify working check_palindrome method
      """
      test = test_method()
      input_str = 'test'
      self.assertEqual(test.check_palindrome(input_str), False)

    def test_2(self):
      """
      Test to verify working check_palindrome method
      """
      test = test_method()
      input_str = 'racecar'
      self.assertEqual(test.check_palindrome(input_str), True)

    def test_3(self):
      """
      Test to verify working check_palindrome method
      """
      test = test_method()
      input_str = 'deed'
      self.assertEqual(test.check_palindrome(input_str), True)

    def test_4(self):
      """
      Test to verify working check_palindrome method
      """
      test = test_method()
      input_str = 'level'
      self.assertEqual(test.check_palindrome(input_str), True)

    def test_5(self):
      """
      Test to verify working check_palindrome method
      """
      test = test_method()
      input_str = 'anna'
      self.assertEqual(test.check_palindrome(input_str), True)

if __name__ == "__main__":
  unittest.main()