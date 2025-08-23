"""
medium

Write a function that takes in a non-empty array of integers and
returns the maximum sum that can be obtained by summing up all of the
integers in a non-empty subarray of the input array.
A subarray must only contain adjacent numbers (numbers next to each other in the input array).

Sample Input
array = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
Sample Output
19 // [1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1]
"""

def kadanes_algorithm_1(array):
    max_adjacents = [array[0]]

    for i in range(1, len(array)):
        new_max = max(max_adjacents[-1] + array[i], array[i])
        max_adjacents.append(new_max)
    return max(max_adjacents)
