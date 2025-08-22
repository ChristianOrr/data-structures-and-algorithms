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

# Solution 1 O(n^2) - brute force
def two_number_sum_1(array, targetSum):
    n = len(array)
    for i in range(n):
        for j in range(i + 1, n):
            if array[i] + array[j] == targetSum:
                return [array[i], array[j]]
    return []


# Solution 2 O(n) - hash set
def two_number_sum_2(array, targetSum):
    hash_map = set()
    for num in array:
        difference = targetSum - num
        if difference in hash_map:
            return [num, difference]
        hash_map.add(num)
    return []


# Solution 3 O(nlog(n)) - two pointers on sorted copy
def two_number_sum_3(arr, target_sum):
    sorted_arr = sorted(arr)
    left_ptr = 0
    right_ptr = len(sorted_arr) - 1
    while left_ptr < right_ptr:
        left_value = sorted_arr[left_ptr]
        right_value = sorted_arr[right_ptr]
        total_sum = left_value + right_value
        if total_sum > target_sum:
            right_ptr -= 1
        elif total_sum < target_sum:
            left_ptr += 1
        else:
            return [left_value, right_value]
    return []