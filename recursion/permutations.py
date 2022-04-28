"""
medium

Write a function that takes in an array of unique integers and
returns an array of all permutations of those integers in no particular order.

If the input array is empty, the function should return an empty array.

Sample Input
array = [1, 2, 3]
Sample Output
[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
"""
import unittest


def getPermutations(array):
    if len(array) == 0:
        return []
    elif len(array) == 1:
        return [array]
    permutations = []
    for element in array:
        mutated_array = array.copy()
        mutated_array.remove(element)
        sub_permutations = getPermutations(mutated_array)
        for sub_array in sub_permutations:
            sub_array.insert(0, element)
            permutations.append(sub_array)
    return permutations




class TestProgram(unittest.TestCase):
    def test_1(self):
        perms = getPermutations([1, 2, 3])
        self.assertTrue(len(perms) == 6)
        self.assertTrue([1, 2, 3] in perms)
        self.assertTrue([1, 3, 2] in perms)
        self.assertTrue([2, 1, 3] in perms)
        self.assertTrue([2, 3, 1] in perms)
        self.assertTrue([3, 1, 2] in perms)
        self.assertTrue([3, 2, 1] in perms)

    def test_2(self):
        perms = getPermutations([8])
        self.assertTrue(len(perms) == 1)
        self.assertTrue([8] in perms)

    def test_3(self):
        perms = getPermutations([])
        self.assertTrue(len(perms) == 0)