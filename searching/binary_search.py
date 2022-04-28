"""
easy

Write a function that takes in a sorted array of integers as well as a target integer.
The function should use the Binary Search algorithm to determine if the target integer is contained in the array and
should return its index if it is, otherwise -1.

Sample Input
array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target = 33
Sample Output
3
"""
import unittest


def binarySearch(array, target):
    left_index = 0
    right_index = len(array) - 1
    middle_index = (left_index + right_index) // 2

    while left_index <= right_index:
        if array[middle_index] == target:
            return middle_index
        elif array[middle_index] < target:
            left_index = middle_index + 1
        else:
            right_index = middle_index - 1

        middle_index = (left_index + right_index) // 2
    return -1





class TestProgram(unittest.TestCase):
    def test_1(self):
        self.assertEqual(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33), 3)

    def test_2(self):
        self.assertEqual(binarySearch([1, 5, 23, 245], 245), 3)

    def test_3(self):
        self.assertEqual(binarySearch([0, 1, 21, 33, 71], 0), 0)

    def test_4(self):
        self.assertEqual(binarySearch([0, 21, 33, 61, 72, 355], 354), -1)
