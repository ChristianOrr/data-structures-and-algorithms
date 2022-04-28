"""
medium

You're given a two-dimensional array (a matrix) of distinct integers and a target integer.
Each row in the matrix is sorted, and each column is also sorted;
the matrix doesn't necessarily have the same height and width.

Write a function that returns an array of the row and column indices of the
target integer if it's contained in the matrix, otherwise [-1, -1].

Sample Input
matrix = [
  [1, 4, 7, 12, 15, 1000],
  [2, 5, 19, 31, 32, 1001],
  [3, 8, 24, 33, 35, 1002],
  [40, 41, 42, 44, 45, 1003],
  [99, 100, 103, 106, 128, 1004],
]
target = 44
Sample Output
[3, 3]
"""
import unittest


def searchInSortedMatrix(matrix, target):
    row_index = 0
    while row_index < len(matrix):
        if matrix[row_index][0] > target:
            row_index -= 1
            break
        row_index += 1

    if row_index >= len(matrix):
        row_index = len(matrix) - 1

    for col_index in range(len(matrix[row_index])):
        value = matrix[row_index][col_index]
        if value == target:
            return [row_index, col_index]
        elif value > target:
            while value > target and row_index > 0:
                row_index -= 1
                value = matrix[row_index][col_index]
                if value == target:
                    return [row_index, col_index]

    return [-1, -1]





class TestProgram(unittest.TestCase):
    def test_1(self):
        matrix = [
            [1, 4, 7, 12, 15, 1000],
            [2, 5, 19, 31, 32, 1001],
            [3, 8, 24, 33, 35, 1002],
            [40, 41, 42, 44, 45, 1003],
            [99, 100, 103, 106, 128, 1004],
        ]
        actual = searchInSortedMatrix(matrix, 44)
        self.assertEqual(actual, [3, 3])

    def test_2(self):
        matrix = [
            [1, 4, 7, 12, 15, 1000],
            [2, 5, 19, 31, 32, 1001],
            [3, 8, 24, 33, 35, 1002],
            [40, 41, 42, 44, 45, 1003],
            [99, 100, 103, 106, 128, 1004],
        ]
        actual = searchInSortedMatrix(matrix, 100)
        self.assertEqual(actual, [4, 1])

    def test_3(self):
        matrix = [
            [1, 4, 7, 12, 15, 1000],
            [2, 5, 19, 31, 32, 1001],
            [3, 8, 24, 33, 35, 1002],
            [40, 41, 42, 44, 45, 1003],
            [99, 100, 103, 106, 128, 1004],
        ]
        actual = searchInSortedMatrix(matrix, 1000)
        self.assertEqual(actual, [0, 5])

    def test_4(self):
        matrix = [
            [1, 4, 7, 12, 15, 1000],
            [2, 5, 19, 31, 32, 1001],
            [3, 8, 24, 33, 35, 1002],
            [40, 41, 42, 44, 45, 1003],
            [99, 100, 103, 106, 128, 1004],
        ]
        actual = searchInSortedMatrix(matrix, 20)
        self.assertEqual(actual, [-1, -1])

    def test_5(self):
        matrix = [
            [1, 4, 7, 12, 15, 1000],
            [2, 5, 19, 31, 32, 1001],
            [3, 8, 24, 33, 35, 1002],
            [40, 41, 42, 44, 45, 1003],
            [99, 100, 103, 106, 128, 1004],
        ]
        actual = searchInSortedMatrix(matrix, 999)
        self.assertEqual(actual, [-1, -1])

    def test_6(self):
        matrix = [
            [1, 4, 7, 12, 15, 1000],
            [2, 5, 19, 31, 32, 1001],
            [3, 8, 24, 33, 35, 1002],
            [40, 41, 42, 44, 45, 1003],
            [99, 100, 103, 106, 128, 1004],
        ]
        actual = searchInSortedMatrix(matrix, 15)
        self.assertEqual(actual, [0, 4])
