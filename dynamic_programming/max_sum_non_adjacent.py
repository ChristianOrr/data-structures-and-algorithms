"""
medium

Write a function that takes in an array of positive integers and
returns the maximum sum of non-adjacent elements in the array.

If the input array is empty, the function should return 0.

Sample Input
array = [75, 105, 120, 75, 90, 135]
Sample Output
330 // 75 + 120 + 135
"""
import unittest


def maxSubsetSumNoAdjacent(array):
    if len(array) == 0:
        return 0

    max_values = [array[0]]
    for i in range(1, len(array)):
        prev_max = max_values[-1]
        if i > 1:
            current_max = array[i] + max_values[-2]
        else:
            current_max = array[i]
        next_max = max(current_max, prev_max)
        max_values.append(next_max)

    return max_values[-1]


class TestProgram(unittest.TestCase):
    def test_1(self):
        self.assertEqual(maxSubsetSumNoAdjacent([75, 105, 120, 75, 90, 135]), 330)

    def test_2(self):
        self.assertEqual(maxSubsetSumNoAdjacent([]), 0)
