"""
medium

Write a function that takes in an array of unique integers and returns its powerset.

The powerset P(X) of a set X is the set of all subsets of X.
For example, the powerset of [1,2] is [[], [1], [2], [1,2]].

Note that the sets in the powerset do not need to be in any particular order.

Sample Input
array = [1, 2, 3]
Sample Output
[[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
"""
import unittest


def powerset(array, result=None):
    if result is None:
        result = [[]]
    if len(array) == 0:
        return result
    elif len(array) == 1:
        if array not in result:
            result.append(array)
        return result

    for element in array:
        sub_array = array.copy()
        sub_array.remove(element)
        if sub_array not in result:
            result.append(sub_array)
        result = powerset(sub_array, result)

    if array not in result:
        result.append(array)
    return result


class TestProgram(unittest.TestCase):
    def test_1(self):
        output = list(map(lambda x: set(x), powerset([1, 2, 3])))
        self.assertTrue(len(output) == 8)
        self.assertTrue(set([]) in output)
        self.assertTrue(set([1]) in output)
        self.assertTrue(set([2]) in output)
        self.assertTrue(set([1, 2]) in output)
        self.assertTrue(set([3]) in output)
        self.assertTrue(set([1, 3]) in output)
        self.assertTrue(set([2, 3]) in output)
        self.assertTrue(set([1, 2, 3]) in output)

    def test_2(self):
        output = list(map(lambda x: set(x), powerset([1, 2])))
        self.assertTrue(len(output) == 4)
        self.assertTrue(set([]) in output)
        self.assertTrue(set([1]) in output)
        self.assertTrue(set([2]) in output)
        self.assertTrue(set([1, 2]) in output)

    def test_3(self):
        output = list(map(lambda x: set(x), powerset([5])))
        self.assertTrue(len(output) == 2)
        self.assertTrue(set([]) in output)
        self.assertTrue(set([5]) in output)