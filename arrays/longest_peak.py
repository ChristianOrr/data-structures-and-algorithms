"""
medium

Write a function that takes in an array of integers and returns the length of the longest peak in the array.

A peak is defined as adjacent integers in the array that are strictly increasing until they reach a tip
(the highest value in the peak), at which point they become strictly decreasing.
At least three integers are required to form a peak.

For example, the integers 1, 4, 10, 2 form a peak, but the integers 4, 0, 10 don't and
neither do the integers 1, 2, 2, 0.
Similarly, the integers 1, 2, 3 don't form a peak because there aren't any strictly decreasing integers after the 3.

Sample Input
array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
Sample Output
6 // 0, 10, 6, 5, -1, -3
"""
import unittest


def longestPeak(array):
    longest = 0
    i = 1

    while i < (len(array) - 1):
        left = i - 1
        right = i + 1

        if array[left] < array[i] and array[right] < array[i]:
            left -= 1
            right += 1
            while left >= 0 and array[left] < array[left + 1]:
                left -= 1
            while right < len(array) and array[right] < array[right - 1]:
                right += 1

            current = right - left - 1
            if current > longest:
                longest = current
        i = right
    return longest



class TestProgram(unittest.TestCase):
    def test_1(self):
        array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
        expected = 6
        self.assertEqual(longestPeak(array), expected)

    def test_2(self):
        array = [5, 4, 3, 2, 1, 2, 1]
        expected = 3
        self.assertEqual(longestPeak(array), expected)

    def test_3(self):
        array = [1, 2, 3, 3, 2, 1]
        expected = 0
        self.assertEqual(longestPeak(array), expected)

    def test_4(self):
        array = [1, 2, 3, 2, 1, 1]
        expected = 5
        self.assertEqual(longestPeak(array), expected)

    def test_5(self):
        array = [1, 1, 1, 2, 3, 10, 12, -3, -3, 2, 3, 45, 800, 99, 98, 0, -1, -1, 2, 3, 4, 5, 0, -1, -1]
        expected = 9
        self.assertEqual(longestPeak(array), expected)