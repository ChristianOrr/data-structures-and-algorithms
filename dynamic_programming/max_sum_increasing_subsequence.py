"""
hard

Write a function that takes in a non-empty array of integers and
returns the greatest sum that can be generated from a strictly-increasing subsequence in the array as well as
an array of the numbers in that subsequence.

A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but that are in
the same order as they appear in the array.
For instance, the numbers [1, 3, 4] form a subsequence of the array [1, 2, 3, 4], and
so do the numbers [2, 4].
Note that a single number in an array and the array itself are both valid subsequences of the array.

You can assume that there will only be one increasing subsequence with the greatest sum.

Sample Input
array = [10, 70, 20, 30, 50, 11, 30]
Sample Output
[110, [10, 20, 30, 50]] // The subsequence [10, 20, 30, 50] is strictly increasing and yields the greatest sum: 110.
"""
def max_sum_increasing_subsequence_1(array):
    sums = [array[0]]
    prev_indexes = [None for i in range(len(array))]

    for i in range(1, len(array)):
        new_sum = array[i]
        for j in range(i):
            if array[j] < array[i] and array[i] + sums[j] > new_sum:
                new_sum = array[i] + sums[j]
                prev_indexes[i] = j
        sums.append(new_sum)

    max_value = max(sums)
    max_index = sums.index(max_value)
    sub_sequence = []
    new_index = max_index
    while new_index is not None:
        sub_sequence.insert(0, array[new_index])
        new_index = prev_indexes[new_index]

    return [max_value, sub_sequence]

