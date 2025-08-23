"""
medium

You're given a two-dimensional array (a matrix) of potentially unequal height and width containing only 0s and 1s.
Each 0 represents land, and each 1 represents part of a river.
A river consists of any number of 1s that are either horizontally or vertically adjacent (but not diagonally adjacent).
The number of adjacent 1s forming a river determine its size.

Note that a river can twist.
In other words, it doesn't have to be a straight vertical line or a straight horizontal line;
it can be L-shaped, for example.

Write a function that returns an array of the sizes of all rivers represented in the input matrix.
The sizes don't need to be in any particular order.

Sample Input
matrix = [
  [1, 0, 0, 1, 0],
  [1, 0, 1, 0, 0],
  [0, 0, 1, 0, 1],
  [1, 0, 1, 0, 1],
  [1, 0, 1, 1, 0],
]
Sample Output
[1, 2, 2, 2, 5] // The numbers could be ordered differently.

// The rivers can be clearly seen here:
// [
//   [1,  ,  , 1,  ],
//   [1,  , 1,  ,  ],
//   [ ,  , 1,  , 1],
//   [1,  , 1,  , 1],
//   [1,  , 1, 1,  ],
// ]
"""

def river_sizes_1(matrix):
    visited = set()
    sizes = []
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if (i, j) in visited:
                continue
            if value == 1:
                river_length = dfs(i, j, matrix, visited, 0)
                sizes.append(river_length)
    return sizes


def dfs(i, j, matrix, visited, river_length):
    river_length += 1
    visited.add((i, j))
    children = get_children(i, j, matrix, visited)
    for child in children:
        river_length = dfs(child[0], child[1], matrix, visited, river_length)

    return river_length


def get_children(i, j, matrix, visited):
    children = [[i - 1, j], [i, j + 1], [i + 1, j], [i, j - 1]]
    for child in children.copy():
        if child[0] < 0 or child[0] >= len(matrix) or \
                child[1] < 0 or child[1] >= len(matrix[0]):
            children.remove(child)
        elif matrix[child[0]][child[1]] == 0:
            children.remove(child)
        elif (child[0], child[1]) in visited:
            children.remove(child)
        else:
            visited.add((child[0], child[1]))
    return children

