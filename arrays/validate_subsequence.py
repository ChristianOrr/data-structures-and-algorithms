"""
easy

Given two non-empty arrays of integers, write a function that determines whether the
second array is a subsequence of the first one.

A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but
that are in the same order as they appear in the array.
For instance, the numbers [1, 3, 4] form a subsequence of the array [1, 2, 3, 4], and so do the numbers [2, 4].
Note that a single number in an array and the array itself are both valid subsequences of the array.

Sample Input
array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
Sample Output
true

Solution 1
Time Complexity: O(n), space complexity: O(1)
Strategy:
Loop through the array, and keep a counter for the sequence.
When a match is found increase the counter,
then check it the counter is the length of the sequence, return True if it is.
At the end of the loop return True if counter == len(sequence), False otherwise.

Solution 2
Time Complexity: O(n), space complexity: O(1)
Strategy:
Use while loop that loops while counter for the sequence and counter for the array are not finished.
When a match is found increase sequence counter,
increase counter for array at end of loop.
After loop is complete return True if counter == len(sequence), False otherwise.
"""
# Solution 1
def validate_subsequence_solution_1(array, sequence):
    array_index = 0
    seq_index = 0

    while seq_index < len(sequence) and array_index < len(array):
        if array[array_index] == sequence[seq_index]:
            seq_index += 1
        array_index += 1
    return seq_index == len(sequence)
