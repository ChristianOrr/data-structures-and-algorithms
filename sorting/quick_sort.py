"""
hard

Write a function that takes in an array of integers and returns a sorted version of that array.
Use the Quick Sort algorithm to sort the array.

Sample Input
array = [8, 5, 2, 9, 5, 6, 3]
Sample Output
[2, 3, 5, 5, 6, 8, 9]
"""
import unittest

def quickSort(array):
    quick_sort_helper(0, len(array) - 1, array)
    return array

def quick_sort_helper(start_index, end_index, array):
    if start_index >= end_index:
        return

    pivot_index = start_index
    left_index = start_index + 1
    right_index = end_index

    while left_index <= right_index:
        if array[left_index] > array[pivot_index] and array[right_index] < array[pivot_index]:
            array[left_index], array[right_index] = array[right_index], array[left_index]
            left_index += 1
            right_index -= 1
        if array[left_index] <= array[pivot_index]:
            left_index += 1
        if array[right_index] >= array[pivot_index]:
            right_index -= 1
    array[pivot_index], array[right_index] = array[right_index], array[pivot_index]

    quick_sort_helper(start_index, right_index - 1, array)
    quick_sort_helper(right_index + 1, end_index, array)
    return array


class TestProgram(unittest.TestCase):
    def test_1(self):
        self.assertEqual(quickSort([8, 5, 2, 9, 5, 6, 3]), [2, 3, 5, 5, 6, 8, 9])

    def test_2(self):
        self.assertEqual(quickSort([8]), [8])

    def test_3(self):
        self.assertEqual(quickSort([8, 6]), [6, 8])

    def test_4(self):
        self.assertEqual(quickSort([6, 8]), [6, 8])
