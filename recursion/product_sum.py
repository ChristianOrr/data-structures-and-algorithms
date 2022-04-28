"""
easy

Write a function that takes in a "special" array and returns its product sum.

A "special" array is a non-empty array that contains either integers or other "special" arrays.
The product sum of a "special" array is the sum of its elements,
where "special" arrays inside it are summed themselves and then multiplied by their level of depth.

The depth of a "special" array is how far nested it is. For instance, the depth of [] is 1;
the depth of the inner array in [[]] is 2; the depth of the innermost array in [[[]]] is 3.

Therefore, the product sum of [x, y] is x + y;
the product sum of [x, [y, z]] is x + 2 * (y + z); the product sum of [x, [y, [z]]] is x + 2 * (y + 3z).
"""
import unittest


def productSum(array, depth=1):
    sum = 0
    for element in array:
        if type(element) == int:
            sum += element
        else:
            sum += productSum(element, depth + 1)
    return sum * depth



class TestProgram(unittest.TestCase):
    def test_1(self):
        test = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
        self.assertEqual(productSum(test), 12)

    def test_2(self):
        test = [9, [2, -3, 4], 1, [1, 1, [1, 1, 1]], [[[[3, 4, 1]]], 8],
                [1, 2, 3, 4, 5, [6, 7], -7], [1, [2, 3, [4, 5]], [6, 0, [7, 0, -8]], -7],
                [1, -3, 2, [1, -3, 2, [1, -3, 2], [1, -3, 2, [1, -3, 2]], [1, -3, 2]]], -3]
        self.assertEqual(productSum(test), 1351)

    def test_3(self):
        test = [1, 2, [3], 4, 5]
        self.assertEqual(productSum(test), 18)

    def test_4(self):
        test = [[[[[5]]]]]
        self.assertEqual(productSum(test), 600)
