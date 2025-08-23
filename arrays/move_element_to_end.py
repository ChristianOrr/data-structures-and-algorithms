"""
medium

You're given an array of integers and an integer.
Write a function that moves all instances of that integer in the array to the end of the array and returns the array.

The function should perform this in place (i.e., it should mutate the input array) and
doesn't need to maintain the order of the other integers.
"""


# Solution 1 O(n) - collect and append
def move_element_to_end_solution_1(array, toMove):
    move_indexes = []
    for i in range(len(array)):
        if array[i] == toMove:
            move_indexes.append(i)

    for del_index in sorted(move_indexes, reverse=True):
        del array[del_index]
    for i in range(len(move_indexes)):
        array.append(toMove)
    return array


# Solution 2 O(n) - two pointers
def move_element_to_end_solution_2(array, toMove):
    start = 0
    end = len(array) - 1

    while start < end:
        if array[start] != toMove:
            start += 1
            continue

        if array[end] == toMove:
            end -= 1
            continue

        array[start] = array[end]
        array[end] = toMove

    return array


