"""
easy

Write a function that takes in an array of at least three integers and, without sorting the input array,
returns a sorted array of the three largest integers in the input array.

The function should return duplicate integers if necessary; for example,
it should return [10, 10, 12] for an input array of [10, 5, 9, 10, 12].

Sample Input
array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
Sample Output
[18, 141, 541]
"""
import unittest


def findThreeLargestNumbers(array):
    three_largest = sorted(array[0:3])
    for i in range(3, len(array)):
        new_value = array[i]
        if new_value > three_largest[0]:
            three_largest.pop(0)
            if new_value > three_largest[-1]:
                three_largest.append(new_value)
            elif new_value > three_largest[-2]:
                three_largest.insert(1, new_value)
            else:
                three_largest.insert(0, new_value)
    return three_largest


class TestProgram(unittest.TestCase):
    def test_1(self):
        self.assertEqual(findThreeLargestNumbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]), [18, 141, 541])

    def test_2(self):
        self.assertEqual(findThreeLargestNumbers([21, 2, 8]), [2, 8, 21])
