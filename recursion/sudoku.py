"""
hard

You're given a two-dimensional array that represents a 9x9 partially filled Sudoku board.
Write a function that returns the solved Sudoku board.

Sudoku is a famous number-placement puzzle in which you need to fill a 9x9 grid with integers in the range of 1-9.
Each 9x9 Sudoku board is split into 9 3x3 subgrids, as seen in the illustration below, and starts out partially filled.

- - 3 | - 2 - | 6 - -
9 - - | 3 - 5 | - - 1
- - 1 | 8 - 6 | 4 - -
- - - - - - - - - - -
- - 8 | 1 - 2 | 9 - -
7 - - | - - - | - - 8
- - 6 | 7 - 8 | 2 - -
- - - - - - - - - - -
- - 2 | 6 - 9 | 5 - -
8 - - | 2 - 3 | - - 9
- - 5 | - 1 - | 3 - -
The objective is to fill the grid such that each row, column, and 3x3 subgrid contains the numbers 1-9 exactly once.
In other words, no row may contain the same digit more than once, no column may contain the same digit more than once,
and none of the 9 3x3 subgrids may contain the same digit more than once.

Your input for this problem will always be a partially filled 9x9 two-dimensional array that
represents a solvable Sudoku puzzle.
Every element in the array will be an integer in the range of 0-9,
where a 0 represents an empty square that must be filled by your algorithm.

Note that you may modify the input array and that there will always be exactly one solution to each input Sudoku board.

Sample Input
board =
[
  [7, 8, 0, 4, 0, 0, 1, 2, 0],
  [6, 0, 0, 0, 7, 5, 0, 0, 9],
  [0, 0, 0, 6, 0, 1, 0, 7, 8],
  [0, 0, 7, 0, 4, 0, 2, 6, 0],
  [0, 0, 1, 0, 5, 0, 9, 3, 0],
  [9, 0, 4, 0, 6, 0, 0, 0, 5],
  [0, 7, 0, 3, 0, 0, 0, 1, 2],
  [1, 2, 0, 0, 0, 7, 4, 0, 0],
  [0, 4, 9, 2, 0, 6, 0, 0, 7],
]
Sample Output
[
  [7, 8, 5, 4, 3, 9, 1, 2, 6],
  [6, 1, 2, 8, 7, 5, 3, 4, 9],
  [4, 9, 3, 6, 2, 1, 5, 7, 8],
  [8, 5, 7, 9, 4, 3, 2, 6, 1],
  [2, 6, 1, 7, 5, 8, 9, 3, 4],
  [9, 3, 4, 1, 6, 2, 7, 8, 5],
  [5, 7, 8, 3, 9, 4, 6, 1, 2],
  [1, 2, 6, 5, 8, 7, 4, 9, 3],
  [3, 4, 9, 2, 1, 6, 8, 5, 7],
]
"""
import unittest


def solveSudoku(board):
    return backtrack(0, 0, board)


def backtrack(row_index, column_index, board):
    if row_index == 9:
        return board

    if column_index == 8:
        new_column_index = 0
        new_row_index = row_index + 1
    else:
        new_column_index = column_index + 1
        new_row_index = row_index


    if board[row_index][column_index] != 0:
        return backtrack(new_row_index, new_column_index, board)

    row_values = board[row_index]
    column_values = [row[column_index] for row in board]

    def get_square_indices(index):
        if index < 3:
            return [0, 1, 2]
        elif index < 6:
            return [3, 4, 5]
        else:
            return [6, 7, 8]

    square_rows = get_square_indices(row_index)
    square_columns = get_square_indices(column_index)

    square_values = []
    for i, row in enumerate(board):
        if i in square_rows:
            for j, value in enumerate(row):
                if j in square_columns:
                    square_values.append(value)

    for num in range(1, 10):
        if not (num in row_values or num in column_values or num in square_values):
            board[row_index][column_index] = num
            updated_board = backtrack(new_row_index, new_column_index, board)
            if not any(0 in new_rows for new_rows in updated_board):
                return updated_board

    board[row_index][column_index] = 0
    return board


class TestProgram(unittest.TestCase):
    def test_1(self):
        input = [
            [7, 8, 0, 4, 0, 0, 1, 2, 0],
            [6, 0, 0, 0, 7, 5, 0, 0, 9],
            [0, 0, 0, 6, 0, 1, 0, 7, 8],
            [0, 0, 7, 0, 4, 0, 2, 6, 0],
            [0, 0, 1, 0, 5, 0, 9, 3, 0],
            [9, 0, 4, 0, 6, 0, 0, 0, 5],
            [0, 7, 0, 3, 0, 0, 0, 1, 2],
            [1, 2, 0, 0, 0, 7, 4, 0, 0],
            [0, 4, 9, 2, 0, 6, 0, 0, 7]
        ]
        expected = [
            [7, 8, 5, 4, 3, 9, 1, 2, 6],
            [6, 1, 2, 8, 7, 5, 3, 4, 9],
            [4, 9, 3, 6, 2, 1, 5, 7, 8],
            [8, 5, 7, 9, 4, 3, 2, 6, 1],
            [2, 6, 1, 7, 5, 8, 9, 3, 4],
            [9, 3, 4, 1, 6, 2, 7, 8, 5],
            [5, 7, 8, 3, 9, 4, 6, 1, 2],
            [1, 2, 6, 5, 8, 7, 4, 9, 3],
            [3, 4, 9, 2, 1, 6, 8, 5, 7]
        ]
        actual = solveSudoku(input)
        self.assertEqual(actual, expected)

    def test_2(self):
        input = [
            [0, 2, 0, 0, 9, 0, 1, 0, 0],
            [0, 0, 7, 8, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 3, 6, 0],
            [0, 0, 1, 9, 0, 4, 0, 0, 0],
            [0, 0, 0, 6, 0, 5, 0, 0, 7],
            [8, 0, 0, 0, 0, 0, 0, 0, 9],
            [0, 0, 0, 0, 2, 0, 0, 0, 0],
            [7, 0, 0, 0, 0, 0, 0, 8, 5],
            [4, 9, 0, 0, 3, 0, 0, 0, 0]
          ]
        expected = [
            [5, 2, 4, 3, 9, 6, 1, 7, 8],
            [3, 6, 7, 8, 4, 1, 9, 5, 2],
            [1, 8, 9, 7, 5, 2, 3, 6, 4],
            [2, 5, 1, 9, 7, 4, 8, 3, 6],
            [9, 4, 3, 6, 8, 5, 2, 1, 7],
            [8, 7, 6, 2, 1, 3, 5, 4, 9],
            [6, 1, 5, 4, 2, 8, 7, 9, 3],
            [7, 3, 2, 1, 6, 9, 4, 8, 5],
            [4, 9, 8, 5, 3, 7, 6, 2, 1]
        ]
        actual = solveSudoku(input)
        self.assertEqual(actual, expected)