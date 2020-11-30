from LinkedSortedSet import LinkedSortedSet
import unittest

class Test_Cases_LinkedSortedSet(unittest.TestCase):
    def test_len(self):
        """
        Test to verify working __len__ method
        """
        result = LinkedSortedSet()
        result.add(99)
        self.assertEqual(len(result), 1)

    def test_remove(self):
        """
        Test to verify working remove method
        """
        result = LinkedSortedSet()
        result.add(99)
        result.remove(99)
        self.assertEqual(len(result), 0)

    def test_isEmpty(self):
        """
        Test to verify working is_empty
        """
        result = LinkedSortedSet()
        result.is_empty()
        self.assertEqual(len(result), 0)

    def test_add_duplicates(self):
        """
        Test to see if duplicate values can be added
        """
        result = LinkedSortedSet()
        result.add(99)
        result.add(99)
        result.add(99)

        test_case = []
        for value in result:
          test_case.append(value)

        self.assertEqual(len(result), 1)
        with self.assertRaises(IndexError):
          test_case[1]

    def test_add_to_Front(self):
        result = LinkedSortedSet()
        result.add(4)
        result.add(2)

        test_case = []
        for value in result:
          test_case.append(value)

        self.assertEqual(len(result), 2)
        self.assertEqual(test_case, [4, 2])

    def test_add_to_back(self):
        result = LinkedSortedSet()
        result.add(4)
        result.add(2)
        result.add(5)

        test_case = []
        for value in result:
          test_case.append(value)

        self.assertEqual(len(result), 3)
        self.assertEqual(test_case, [5, 4, 2])

    def test_add_new_smaller_to_front(self):
        result = LinkedSortedSet()
        result.add(4)
        result.add(2)
        result.add(5)
        result.add(1)

        test_case = []
        for value in result:
          test_case.append(value)

        self.assertEqual(len(result), 4)
        self.assertEqual(test_case, [5, 4, 2, 1])

    def test_sort(self):
        result = LinkedSortedSet()
        result.add(4)
        result.add(2)
        result.add(5)
        result.add(1)
        result.add(10)
        result.add(8)

        test_case = []
        for value in result:
          test_case.append(value)

        self.assertEqual(len(result), 6)
        self.assertEqual(test_case, [10, 8, 5, 4, 2, 1])

    def test_sort_2(self):
        result = LinkedSortedSet()
        result.add(2)
        result.add(4)
        result.add(5)
        result.add(3)
        result.add(1)
        result.add(6)

        test_case = []
        for value in result:
          test_case.append(value)

        self.assertEqual(len(result), 6)
        self.assertEqual(test_case, [6, 5, 4, 3, 2, 1])




if __name__ == '__main__':
    unittest.main()