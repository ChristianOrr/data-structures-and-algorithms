"""
easy

Write a function that takes in an array of integers and returns a sorted version of that array.
Use the Bubble Sort algorithm to sort the array.

Sample Input
array = [8, 5, 2, 9, 5, 6, 3]
Sample Output
[2, 3, 5, 5, 6, 8, 9]

# Solution 1
Time complexity: O(n^2), space complexity: O(n)
Strategy:
Loop through the array twice. Compare adjacent elements in second loop.
First loop decreases the size of the second loop by 1 every sweep, using a counter.
If value1 < value2 swap them, otherwise continue second loop.
The largest element will get moved to the back during each sweep.
Check if a swap is performed during second loop sweep.
If no swap is performed for a sweep, then the array is sorted, and you can return it.
"""
import unittest


def bubbleSort(array):
    is_sorted = False
    counter = 0

    while not is_sorted and counter < len(array):
        is_sorted = True
        for i in range(len(array) - 1 - counter):

            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                is_sorted = False
        counter += 1
    return array


class TestProgram(unittest.TestCase):
    def test_1(self):
        input = [8, 5, 2, 9, 5, 6, 3]
        self.assertEqual(bubbleSort(input), [2, 3, 5, 5, 6, 8, 9])

    def test_2(self):
        self.assertEqual(bubbleSort([]), [])

    def test_3(self):
        input = [9, 1]
        self.assertEqual(bubbleSort(input), [1, 9])