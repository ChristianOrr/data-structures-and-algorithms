"""
easy

Write a function that takes in a non-empty array of integers that are sorted in ascending order and
returns a new array of the same length with the squares of the original integers also sorted in ascending order.

Sample Input
array = [-3, 1, 2, 3, 5]
Sample Output
[1, 4, 9, 9, 25]

Solution 1
Time Complexity: O(nlog(n)), space complexity: O(n)
Strategy:
Square the elements in the array, sort the array and return it.

Solution 2
Time Complexity: O(n), space complexity: O(n)
Strategy:
Create left and right pointers.
Initialize the output square array with zero's, then iterate over it starting from the right.
At each position find the largest absolute value of left and right numbers,
then add its square to the output array, starting from the back.
Return the output array after the loop.

"""
import unittest


def sortedSquaredArray(array):

    output = [0 for _ in range(len(array))]
    left = 0
    right = len(array) - 1

    for index in reversed(range(len(output))):

        if abs(array[left]) > abs(array[right]):
            output[index] = array[left] ** 2
            left += 1
        else:
            output[index] = array[right] ** 2
            right -= 1

    return output




class TestProgram(unittest.TestCase):
    def test_1(self):
        input = [-3, 1, 2, 3, 5]
        expected = [1, 4, 9, 9, 25]
        actual = sortedSquaredArray(input)
        self.assertEqual(actual, expected)