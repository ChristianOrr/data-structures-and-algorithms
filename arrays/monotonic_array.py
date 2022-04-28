"""
medium

Write a function that takes in an array of integers and returns a boolean representing whether the array is monotonic.

An array is said to be monotonic if its elements, from left to right,
are entirely non-increasing or entirely non-decreasing.

Non-increasing elements aren't necessarily exclusively decreasing; they simply don't increase.
Similarly, non-decreasing elements aren't necessarily exclusively increasing; they simply don't decrease.

Note that empty arrays and arrays of one element are monotonic.
"""
import unittest


def isMonotonic(array):
    decreasing = None
    for i in range(1, len(array)):
        change = array[i] - array[i - 1]
        if change != 0:
            if change < 0:
                if decreasing is None:
                    decreasing = True
                elif decreasing:
                    continue
                elif not decreasing:
                    return False
            else:
                if decreasing is None:
                    decreasing = False
                elif decreasing:
                    return False
                elif not decreasing:
                    continue
    return True


class TestProgram(unittest.TestCase):
    def test_1(self):
        array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
        expected = True
        actual = isMonotonic(array)
        self.assertEqual(actual, expected)

    def test_2(self):
        array = [2, 2, 2, 1, 4, 5]
        expected = False
        actual = isMonotonic(array)
        self.assertEqual(actual, expected)

    def test_3(self):
        array = [1, 2]
        expected = True
        actual = isMonotonic(array)
        self.assertEqual(actual, expected)

    def test_4(self):
        array = []
        expected = True
        actual = isMonotonic(array)
        self.assertEqual(actual, expected)

    def test_5(self):
        array = [7]
        expected = True
        actual = isMonotonic(array)
        self.assertEqual(actual, expected)
