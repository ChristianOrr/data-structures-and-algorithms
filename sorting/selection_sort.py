"""
easy

Write a function that takes in an array of integers and returns a sorted version of that array.
Use the Selection Sort algorithm to sort the array.

Sample Input
array = [8, 5, 2, 9, 5, 6, 3]
Sample Output
[2, 3, 5, 5, 6, 8, 9]
"""
import unittest


def selectionSort(array):

    for i in range(len(array) - 1):
        current_value = array[i]
        smallest_value = current_value
        smallest_index = i
        for j in range(i + 1, len(array)):
            next_value = array[j]
            if next_value < smallest_value:
                smallest_value = next_value
                smallest_index = j
        array[i] = smallest_value
        array[smallest_index] = current_value

    return array


class TestProgram(unittest.TestCase):
    def test_1(self):
        self.assertEqual(selectionSort([8, 5, 2, 9, 5, 6, 3]), [2, 3, 5, 5, 6, 8, 9])

    def test_2(self):
        self.assertEqual(selectionSort([8]), [8])

    def test_3(self):
        self.assertEqual(selectionSort([8, 6]), [6, 8])
