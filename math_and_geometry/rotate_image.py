"""
medium

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix =
    [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
Output:
    [
    [7,4,1],
    [8,5,2],
    [9,6,3]
    ]

Example 2:
Input: matrix =
    [
    [5,1,9,11],
    [2,4,8,10],
    [13,3,6,7],
    [15,14,12,16]
    ]
Output:
    [
    [15,13,2,5],
    [14,3,4,1],
    [12,6,8,9],
    [16,7,10,11]
    ]

Solution 1
Time Complexity: O(n^2), space complexity: O(1)
Strategy:
Iteration. Create 4 pointers for left, right, top and bottom.
The outer while loop will rotate the outer square to the inner square.
The inner for loop will rotate 4 positions per loop and shift by 1 each time.
Store the elements to be replaced in a temp variable before replacing.
Rotate in reverse so that only 1 temp variable needs to be created per sweep.

Video:
https://www.youtube.com/watch?v=fMSJSS7eO1w&ab_channel=NeetCode
"""
import unittest


def rotate(matrix: list[list[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    left = 0
    right = len(matrix[0]) - 1

    while left < right:
        top = left
        bottom = right
        for i in range(right - left):
            # temp variable
            top_left = matrix[top][left + i]

            matrix[top][left + i] = matrix[bottom - i][left]
            matrix[bottom - i][left] = matrix[bottom][right - i]
            matrix[bottom][right - i] = matrix[top + i][right]
            matrix[top + i][right] = top_left

        left += 1
        right -= 1




class TestProgram(unittest.TestCase):

    def test_1(self):
        input = [
                [1,2,3],
                [4,5,6],
                [7,8,9]
                ]
        output = [
                [7,4,1],
                [8,5,2],
                [9,6,3]
                ]
        rotate(input)
        self.assertEqual(output, input)

    def test_2(self):
        input = [
            [5, 1, 9, 11],
            [2, 4, 8, 10],
            [13, 3, 6, 7],
            [15, 14, 12, 16]
                ]
        output = [
            [15, 13, 2, 5],
            [14, 3, 4, 1],
            [12, 6, 8, 9],
            [16, 7, 10, 11]
                ]
        rotate(input)
        self.assertEqual(output, input)
