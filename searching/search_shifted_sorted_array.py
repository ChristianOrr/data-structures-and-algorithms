"""
medium

Write a function that takes in a sorted array of distinct integers as well as a target integer.
The caveat is that the integers in the array have been shifted by some amount;
in other words, they've been moved to the left or to the right by one or more positions.
For example, [1, 2, 3, 4] might have turned into [3, 4, 1, 2].

The function should determine if the target integer is
contained in the array and should return its index if it is, otherwise -1.

Solution 1
Time Complexity: O(log(n)), space complexity: O(log(n))
Strategy:
Recursion. Use variation of Binary Search (three pointer strategy).
Base Case1: If left > right return -1.
Base Case2: If middle == target return middle.
Check whether the left or right side is sorted.
Then check if the target is within the sorted side's interval.
If it is, then explore the sorted side, otherwise explore the other side.
Continue this method until the target is found or left index is greater than the right.

Solution 2
Time Complexity: O(log(n)), space complexity: O(1)
Strategy:
Iterative. Use variation of Binary Search (three pointer strategy).
While left <= right search for a match.
If middle == target return middle.
Otherwise check whether the left or right side is sorted.
Then check if the target is within the sorted side's interval.
If it is, then explore the sorted side, otherwise explore the other side.
If the while loop completes without finding a match return -1.

Video:
https://www.youtube.com/watch?v=U8XENwh8Oy8&ab_channel=NeetCode
"""
import unittest


def shiftedBinarySearch(array, target):
    return search_helper(array, target, 0, len(array) - 1)

def search_helper(array, target, left, right):
    middle = (right + left) // 2
    if array[middle] == target:
        return middle
    elif left > right:
        return -1

    if array[left] < array[middle]:
        if target == array[left]:
            return left
        elif array[left] < target < array[middle]:
            return search_helper(array, target, left, middle - 1)
        else:
            return search_helper(array, target, middle + 1, right)
    else:
        if target == array[right]:
            return right
        elif array[middle] < target < array[right]:
            return search_helper(array, target, middle + 1, right)
        else:
            return search_helper(array, target, left, middle - 1)





class TestProgram(unittest.TestCase):
    def test_1(self):
        self.assertEqual(shiftedBinarySearch([45, 61, 71, 72, 73, 0, 1, 21, 33, 37], 33), 8)

    def test_2(self):
        self.assertEqual(shiftedBinarySearch([33, 37, 45], 38), -1)

    def test_3(self):
        self.assertEqual(shiftedBinarySearch([3, 1], 1), 1)
