"""
easy

Write a function that takes in an array of integers and returns a sorted version of that array.
Use the Insertion Sort algorithm to sort the array.

Solution 1
Time Complexity: O(n^2), space complexity: O(1)
Strategy:
Iterate over the array starting from index 1.
Create pointer and initially set pointer = index.
Shift the smallest values to the left on each pass.
While num < previous_num swap values and decrement pointer.
Add condition to while loop to stop pointer < 0.
Return the array at the end of the loop.
"""
import unittest


# Solution 1
def insertionSort(array):

    for index in range(1, len(array)):
        pointer = index

        while pointer > 0 and array[pointer] < array[pointer - 1]:
            array[pointer], array[pointer - 1] = array[pointer - 1], array[pointer]
            pointer -= 1

    return array



class TestProgram(unittest.TestCase):
    def test_1(self):
        self.assertEqual(insertionSort([8, 5, 2, 9, 5, 6, 3]), [2, 3, 5, 5, 6, 8, 9])

    def test_2(self):
        self.assertEqual(insertionSort([8]), [8])

    def test_3(self):
        self.assertEqual(insertionSort([8, 6]), [6, 8])

    def test_4(self):
        self.assertEqual(insertionSort([6, 8]), [6, 8])