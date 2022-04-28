"""
medium

You're given an array of integers and an integer.
Write a function that moves all instances of that integer in the array to the end of the array and returns the array.

The function should perform this in place (i.e., it should mutate the input array) and
doesn't need to maintain the order of the other integers.
"""
import unittest


# Solution 1
def moveElementToEnd(array, toMove):
    move_indexes = []
    for i in range(len(array)):
        if array[i] == toMove:
            move_indexes.append(i)

    for del_index in sorted(move_indexes, reverse=True):
        del array[del_index]
    for i in range(len(move_indexes)):
        array.append(toMove)
    return array


# Solution 2
def moveElementToEnd(array, toMove):
    start = 0
    end = len(array) - 1

    while start < end:
        if not array[start] == toMove:
            start += 1
            continue

        if array[end] == toMove:
            end -= 1
            continue

        array[start] = array[end]
        array[end] = toMove

    return array


class TestProgram(unittest.TestCase):
    def test_1(self):
        array = [2, 1, 2, 2, 2, 3, 4, 2]
        toMove = 2
        expectedStart = [1, 3, 4]
        expectedEnd = [2, 2, 2, 2, 2]
        output = moveElementToEnd(array, toMove)
        outputStart = sorted(output[0:3])
        outputEnd = output[3:]
        self.assertEqual(outputStart, expectedStart)
        self.assertEqual(outputEnd, expectedEnd)

    def test_2(self):
        array = []
        toMove = 3
        expected = []
        output = moveElementToEnd(array, toMove)
        self.assertEqual(output, expected)


