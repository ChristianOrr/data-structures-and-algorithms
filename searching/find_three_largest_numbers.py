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

Solution 1
Time Complexity: O(n), space complexity: O(1)
Strategy:
Initialize the three_largest = [None, None, None]
Traverse the array and compare the current number to the three largest numbers.
If the current number is greater than one of the three largest, then pop the smallest number off and
insert the number into its correct position.
After the loop return the three_smallest array.
"""
import unittest

# Solution 1
def findThreeLargestNumbers(array):
    three_largest = [None, None, None]

    for num in array:
        if three_largest[2] is None or three_largest[2] < num:
            three_largest.pop(0)
            three_largest.append(num)
        elif three_largest[1] is None or three_largest[1] < num:
            three_largest.pop(0)
            three_largest.insert(1, num)
        elif three_largest[0] is None or three_largest[0] < num:
            three_largest.pop(0)
            three_largest.insert(0, num)

    return three_largest



class TestProgram(unittest.TestCase):
    def test_1(self):
        self.assertEqual(findThreeLargestNumbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]), [18, 141, 541])

    def test_2(self):
        self.assertEqual(findThreeLargestNumbers([21, 2, 8]), [2, 8, 21])
