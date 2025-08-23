"""
medium

You're given a two-dimensional array (a matrix) of potentially unequal height and width containing only 0s and 1s.
The matrix represents a two-toned image, where each 1 represents black and each 0 represents white.
An island is defined as any number of 1s that are horizontally or vertically adjacent (but not diagonally adjacent) and
that don't touch the border of the image.
In other words, a group of horizontally or vertically adjacent 1s isn't an island if
any of those 1s are in the first row, last row, first column, or last column of the input matrix.

Note that an island can twist.
In other words, it doesn't have to be a straight vertical line or a straight horizontal line;
it can be L-shaped, for example.

You can think of islands as patches of black that don't touch the border of the two-toned image.

Write a function that returns a modified version of the input matrix,
where all of the islands are removed. You remove an island by replacing it with 0s.

Naturally, you're allowed to mutate the input matrix.

Sample Input
matrix =
[
  [1, 0, 0, 0, 0, 0],
  [0, 1, 0, 1, 1, 1],
  [0, 0, 1, 0, 1, 0],
  [1, 1, 0, 0, 1, 0],
  [1, 0, 1, 1, 0, 0],
  [1, 0, 0, 0, 0, 1],
]
Sample Output
[
  [1, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 1, 1],
  [0, 0, 0, 0, 1, 0],
  [1, 1, 0, 0, 1, 0],
  [1, 0, 0, 0, 0, 0],
  [1, 0, 0, 0, 0, 1],
]
// The islands that were removed can be clearly seen here:
// [
//   [ ,  ,  ,  ,  , ],
//   [ , 1,  ,  ,  , ],
//   [ ,  , 1,  ,  , ],
//   [ ,  ,  ,  ,  , ],
//   [ ,  , 1, 1,  , ],
//   [ ,  ,  ,  ,  , ],
// ]
"""

def remove_islands_1(matrix):
    non_islands = get_non_islands(matrix)

    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == 1 and (i, j) not in non_islands:
                matrix[i][j] = 0

    return matrix

def get_non_islands(matrix):
    non_islands = set()
    end_column = len(matrix[0]) - 1
    end_row = len(matrix) - 1

    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == 1 and \
                    (j == end_column or j == 0 or i == 0 or i == end_row) and \
                    (i, j) not in non_islands:
                non_islands.add((i, j))
                non_islands = dfs(i, j, matrix, non_islands)

    return non_islands


def dfs(i, j, matrix, non_islands):
    children = get_children(i, j, matrix, non_islands)

    for child in children:
        non_islands = dfs(child[0], child[1], matrix, non_islands)
    return non_islands


def get_children(i, j, matrix, non_islands):
    children = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]

    for child in children.copy():
        if child in non_islands:
            children.remove(child)
        elif child[0] < 0 or child[0] >= len(matrix) or child[1] < 0 or child[1] >= len(matrix[0]):
            children.remove(child)
        elif matrix[child[0]][child[1]] == 0:
            children.remove(child)
        else:
            non_islands.add(child)
    return children

