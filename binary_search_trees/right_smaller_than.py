"""
hard

Write a function that takes in an array of integers and returns an array of the same length,
where each element in the output array corresponds to the number of integers in the input array that
are to the right of the relevant index and that are strictly smaller than the integer at that index.

In other words, the value at output[i] represents the number of integers that
are to the right of i and that are strictly smaller than input[i].

Sample Input
array = [8, 5, 11, -1, 3, 4, 2]
Sample Output
[5, 4, 4, 0, 1, 1, 0]
// There are 5 integers smaller than 8 to the right of it.
// There are 4 integers smaller than 5 to the right of it.
// There are 4 integers smaller than 11 to the right of it.
// Etc..
"""
# Solution 1. Double for loop, O(n^2)
def right_smaller_than_1(array):
    if len(array) == 0:
        return []
    array.append(max(array) + 1)
    smaller_than_array = []
    for i in range(len(array) - 1):
        current_value = array[i]
        num_smaller = 0
        array_remainder = array[i + 1:]
        for element in array_remainder:
            if element < current_value:
                num_smaller += 1
        smaller_than_array.append(num_smaller)
    return smaller_than_array


# Solution 2 (placeholder)
def right_smaller_than_2(array):
    pass
