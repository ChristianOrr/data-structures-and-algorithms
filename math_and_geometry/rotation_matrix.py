"""
medium

You are given an n x n 2D matrix representing an image,
rotate the image by 90 degrees (clockwise) using a rotation matrix.

|x'| = |cos(theta), sin(theta) | * |x|
|y'|   |-sin(theta), cos(theta)|   |y|

[x', y'] is the new coordinates, [x, y] the old coordinates and theta the angle.

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
Iterate over each point in the matrix.
Convert the coordinates so that the centre of the image is the origin, then apply the rotation operation.
Convert the rotated coords back to the normal coordinate frame then insert the value into the
rotation matrix.
Return the rotated matrix at the end of the loop.

"""
import unittest
import math

def rotate(matrix, theta):

    rotated_matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    theta = math.radians(theta)
    sin = math.sin(theta)
    cos = math.cos(theta)
    width = len(matrix[0])
    height = len(matrix)
    mid_y = height // 2
    mid_x = width // 2
    if height % 2 == 0:
        offset = 1
    else:
        offset = 0

    for y in range(height):
        for x in range(width):

            new_x = mid_x - round((x - mid_x) * cos + (y - mid_y) * sin) - offset
            new_y = mid_y - round(-(x - mid_x) * sin + (y - mid_y) * cos)

            if new_x < width and new_y < height:
                rotated_matrix[new_y][new_x] = matrix[y][x]


    return rotated_matrix






class TestProgram(unittest.TestCase):

    def test_1(self):
        input = [
                [1,2,3],
                [4,5,6],
                [7,8,9]
                ]
        theta = 90
        output = [
                [7,4,1],
                [8,5,2],
                [9,6,3]
                ]
        self.assertEqual(output, rotate(input, theta))

    def test_2(self):
        input = [
            [5, 1, 9, 11],
            [2, 4, 8, 10],
            [13, 3, 6, 7],
            [15, 14, 12, 16]
                ]
        theta = 90
        output = [
            [15, 13, 2, 5],
            [14, 3, 4, 1],
            [12, 6, 8, 9],
            [16, 7, 10, 11]
                ]
        self.assertEqual(output, rotate(input, theta))
