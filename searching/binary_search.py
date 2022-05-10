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

Solution 1
Time Complexity: O(log(n)), space complexity: O(log(n))
Strategy:
Recursion, use three pointers for left, right and middle of the array.
Base case: Return -1 if left index is greater than right index.
If middle_number is equal target return middle, elif target less than middle_number set right = middle - 1.
Else set left = middle + 1.



Solution 2
Time Complexity: O(log(n)), space complexity: O(1)
Strategy:
Iteration, use three pointers for left, right and middle of the array.
Loop while left <= right.
If middle_number == target return middle, elif target < middle_number set right = middle - 1.
Else set left = middle + 1.
If loop finishes return -1.

Video:
https://www.youtube.com/watch?v=s4DPM8ct1pI&ab_channel=NeetCode
"""
import unittest


# Solution 1
def binarySearch(array, target):
    return search_helper(array, target, 0, len(array) - 1)


def search_helper(array, target, left, right):
    if left > right:
        return -1

    middle = (left + right) // 2

    if array[middle] == target:
        return middle
    elif target > array[middle]:
        return search_helper(array, target, middle + 1, right)
    else:
        return search_helper(array, target, left, middle - 1)



# Solution 2
def binarySearch(array, target):
    left_index = 0
    right_index = len(array) - 1

    while left_index <= right_index:
        middle_index = (left_index + right_index) // 2
        if array[middle_index] == target:
            return middle_index
        elif array[middle_index] < target:
            left_index = middle_index + 1
        else:
            right_index = middle_index - 1

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
