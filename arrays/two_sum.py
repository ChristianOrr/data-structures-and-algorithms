"""
easy

Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.
If any two numbers in the input array sum up to the target sum,
the function should return them in an array, in any order.
If no two numbers sum up to the target sum, the function should return an empty array.

Note that the target sum has to be obtained by summing two different integers in the array;
you can't add a single integer to itself in order to obtain the target sum.

You can assume that there will be at most one pair of numbers summing up to the target sum.

Sample Input
array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10
Sample Output
[-1, 11] // the numbers could be in reverse order

Solution 1
Time complexity: O(n^2), Space complexity: O(1)
Strategy:
Double for loop. Compare the number in the first loop to all the remaining numbers in the array.
If array[i] + array[j] == target, then return True.
Return False if it loops through all elements.

Solution 2
Time complexity: O(n), Space complexity: O(n)
Strategy:
Loop through the array a single time. Check if (target - current value) is in the hash map.
If it is then return the values, else add the current value to the hash map and continue.
Return False if it loops through all elements.

Solution 3
Time complexity: O(nlog(n)), Space complexity: O(1)
Strategy:
Sort the input array in-place. Create while loop and place left_pointer = 0 index and right_pointer = len(array) - 1,
last index. If left_pointer + right_pointer = target return the answer, else check if it's less or greater than target.
If less increment left_pointer, if greater decrement right_pointer and continue while loop.
Return False if it loops through all elements.

Video:
https://www.youtube.com/watch?v=KLlXCFG5TnA&ab_channel=NeetCode
"""
import unittest

# Solution 1 O(n^2)

# Solution 2 O(n)
def twoNumberSum(array, targetSum):
    hash_map = set()
    for i, num in enumerate(array):
        difference = targetSum - num
        if difference in hash_map:
            return [num, difference]
        hash_map.add(num)
    return []

# Solution 3 O(nlog(n))
def twoNumberSum(array, targetSum):
    left = 0
    right = len(array) - 1
    array.sort()

    while left < right:
        left_value = array[left]
        right_value = array[right]
        total = left_value + right_value

        if total == targetSum:
            return [left_value, right_value]
        elif total < targetSum:
            left += 1
        else:
            right -= 1
    return []




class TestProgram(unittest.TestCase):
    def test_1(self):
        output = twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10)
        self.assertTrue(len(output) == 2)
        self.assertTrue(11 in output)
        self.assertTrue(-1 in output)

    def test_2(self):
        output = twoNumberSum([4], 4)
        self.assertTrue(len(output) == 0)

    def test_3(self):
        output = twoNumberSum([4, 6, 1], 5)
        self.assertTrue(len(output) == 2)
        self.assertTrue(4 in output)
        self.assertTrue(1 in output)
