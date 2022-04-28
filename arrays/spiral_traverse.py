"""
medium

Write a function that takes in an n x m two-dimensional array
(that can be square-shaped when n == m) and returns a one-dimensional array of all the array's elements in spiral order.

Spiral order starts at the top left corner of the two-dimensional array, goes to the right,
and proceeds in a spiral pattern all the way until every element has been visited.

Sample Input
array = [
  [1,   2,  3, 4],
  [12, 13, 14, 5],
  [11, 16, 15, 6],
  [10,  9,  8, 7],
]
Sample Output
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
"""
import unittest



def spiralTraverse(array):
    visited = [(0, 0)]
    direction = "right"
    i = 0
    j = 0
    while len(visited) < (len(array[0]) * len(array)):
        if direction == "right":
            if j + 1 >= len(array[0]) or (i, j + 1) in visited:
                direction = "down"
                i += 1
            else:
                j += 1
            visited.append((i, j))
        elif direction == "down":
            if i + 1 >= len(array) or (i + 1, j) in visited:
                direction = "left"
                j -= 1
            else:
                i += 1
            visited.append((i, j))
        elif direction == "left":
            if j - 1 < 0 or (i, j - 1) in visited:
                direction = "up"
                i -= 1
            else:
                j -=1
            visited.append((i, j))
        elif direction == "up":
            if i - 1 < 0 or (i - 1, j) in visited:
                direction = "right"
                j += 1
            else:
                i -= 1
            visited.append((i, j))

    return [array[i][j] for i, j in visited]


class TestProgram(unittest.TestCase):
    def test_1(self):
        matrix = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        self.assertEqual(spiralTraverse(matrix), expected)