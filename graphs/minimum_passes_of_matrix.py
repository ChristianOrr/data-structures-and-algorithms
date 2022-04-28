"""
medium

Write a function that takes in an integer matrix of potentially unequal height and width and
returns the minimum number of passes required to convert all negative integers in the matrix to positive integers.

A negative integer in the matrix can only be converted to a positive integer if
one or more of its adjacent elements is positive.
An adjacent element is an element that is to the left, to the right,
above, or below the current element in the matrix.
Converting a negative to a positive simply involves multiplying it by -1.

Note that the 0 value is neither positive nor negative,
meaning that a 0 can't convert an adjacent negative to a positive.

A single pass through the matrix involves converting all the negative integers that
can be converted at a particular point in time.
For example, consider the following input matrix:

[
  [0, -2, -1],
  [-5, 2, 0],
  [-6, -2, 0],
]
After a first pass, only 3 values can be converted to positives:

[
  [0, 2, -1],
  [5, 2, 0],
  [-6, 2, 0],
]
After a second pass, the remaining negative values can all be converted to positives:

[
  [0, 2, 1],
  [5, 2, 0],
  [6, 2, 0],
]
Note that the input matrix will always contain at least one element.
If the negative integers in the input matrix can't all be converted to positives,
regardless of how many passes are run, your function should return -1.

Sample Input
matrix = [
  [0, -1, -3, 2, 0],
  [1, -2, -5, -1, -3],
  [3, 0, 0, -4, -1],
]
Sample Output
3
"""
import unittest


def minimumPassesOfMatrix(matrix):
    passes = dfs(matrix)
    return passes


def dfs(matrix, passes=0):
    visited = set()
    num_positive_neighbours = 0
    negatives_left = 0
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value < 0:
                visited.add((i, j))
                negatives_left += 1
                found_positive = find_positive_children(i, j, matrix, visited)
                if found_positive:
                    negatives_left -= 1
                    num_positive_neighbours += 1
                    matrix[i][j] *= -1

    if num_positive_neighbours > 0:
        passes += 1
    if negatives_left == 0:
        return passes
    elif num_positive_neighbours > 0:
        return dfs(matrix, passes)
    else:
        return -1


def find_positive_children(i, j, matrix, visited):

    children = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
    for child in children.copy():
        if child[0] < 0 or child[0] >= len(matrix) or child[1] < 0 or child[1] >= len(matrix[0]):
            children.remove(child)
        elif matrix[child[0]][child[1]] <= 0:
            children.remove(child)
        elif child in visited:
            children.remove(child)

    return len(children) > 0




class TestProgram(unittest.TestCase):
    def test_1(self):
        input = [
            [0, -1, -3, 2, 0],
            [1, -2, -5, -1, -3],
            [3, 0, 0, -4, -1],
        ]
        expected = 3
        actual = minimumPassesOfMatrix(input)
        self.assertEqual(actual, expected)

    def test_2(self):
        input = [
            [1]
        ]
        expected = 0
        actual = minimumPassesOfMatrix(input)
        self.assertEqual(actual, expected)
