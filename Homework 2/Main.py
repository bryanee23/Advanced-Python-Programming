from ArraySet import ArraySet
from LinkedSet import LinkedSet
import unittest

class Test_Cases_ArraySet(unittest.TestCase):

    def test_len(self):
        """
        Test to verify working __len__ method
        """
        result = ArraySet()
        result.add('test')
        self.assertEqual(len(result), 1)

    def test_remove(self):
        """
        Test to verify working remove method
        """
        result = ArraySet()
        result.add('test')
        result.remove('test')
        self.assertEqual(len(result), 0)

    def test_isEmpty(self):
        """
        Test to verify working is_empty
        """
        result = ArraySet()
        result.is_empty()
        self.assertEqual(len(result), 0)

    def test_add_duplicates(self):
        """
        Test to see if duplicate values can be added
        """
        result = ArraySet()
        result.add('test')
        result.add('test')
        result.add('test')

        test_case = []
        for value in result:
          test_case.append(value)

        self.assertEqual(len(result), 1)
        with self.assertRaises(IndexError):
          test_case[1]

    def test_add(self):
        """
        Test to see if duplicate values can be added
        """
        result = ArraySet()
        result.add('test')
        result.add(3)

        test_case = []
        for value in result:
          test_case.append(value)

        self.assertEqual(len(result), 2)
        self.assertEqual(test_case, ["test", 3])

class Test_Cases_LinkedSet(unittest.TestCase):
    def test_len(self):
        """
        Test to verify working __len__ method
        """
        result = LinkedSet()
        result.add('test')
        self.assertEqual(len(result), 1)

    def test_remove(self):
        """
        Test to verify working remove method
        """
        result = LinkedSet()
        result.add('test')
        result.remove('test')
        self.assertEqual(len(result), 0)

    def test_isEmpty(self):
        """
        Test to verify working is_empty
        """
        result = LinkedSet()
        result.is_empty()
        self.assertEqual(len(result), 0)

    def test_add(self):
        """
        Test to see if duplicate values can be added
        """
        result = LinkedSet()
        result.add('test')
        result.add(3)

        test_case = []
        for value in result:
          test_case.append(value)

        self.assertEqual(len(result), 2)
        self.assertEqual(test_case, [3, "test"])


    def test_add_duplicates(self):
        """
        Test to see if duplicate values can be added
        """
        result = LinkedSet()
        result.add('test')
        result.add('test')
        result.add('test')

        test_case = []
        for value in result:
          test_case.append(value)

        self.assertEqual(len(result), 1)
        with self.assertRaises(IndexError):
          test_case[1]

if __name__ == '__main__':
    unittest.main()