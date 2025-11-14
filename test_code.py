import unittest
from sort_list import bubble_sort

class TestAI(unittest.TestCase):
    def test_bubble_sort(self):
        array = [6, 4, 3, 2, 1]
        bubble_sort(array)
        self.assertEqual(array, [1, 2, 3, 4, 6])

if __name__ == "__main__":
    unittest.main(verbosity=2)