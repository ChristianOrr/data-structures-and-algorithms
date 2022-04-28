"""
medium

Given an array of buildings and a direction that all of the buildings face,
return an array of the indices of the buildings that can see the sunset.

A building can see the sunset if it's strictly taller than all of the buildings that
come after it in the direction that it faces.

The input array named buildings contains positive, non-zero integers representing the heights of the buildings.
A building at index i thus has a height denoted by buildings[i].
All of the buildings face the same direction, and
this direction is either east or west, denoted by the input string named direction,
which will always be equal to either "EAST" or "WEST".
In relation to the input array, you can interpret these directions as right for east and left for west.

Important note: the indices in the ouput array should be sorted in ascending order.

Sample Input #1
buildings = [3, 5, 4, 4, 3, 1, 3, 2]
direction = "EAST"
Sample Output #1
[1, 3, 6, 7]

// Below is a visual representation of the sample input.
//    _
//   | |_ _
//  _| | | |_   _
// | | | | | | | |_
// | | | | | |_| | |
// |_|_|_|_|_|_|_|_|
Sample Input #2
buildings = [3, 5, 4, 4, 3, 1, 3, 2]
direction = "WEST"
Sample Output #2
[0, 1]

// The buildings are the same as in the first sample
// input, but their direction is reversed.
"""
import unittest


def sunsetViews(buildings, direction):
    sunset_view_indices = []
    max_height = 0

    if direction == "WEST":
        for index, height in enumerate(buildings):
            if height > max_height:
                sunset_view_indices.append(index)
                max_height = height
    else:
        for index, height in reversed(list(enumerate(buildings))):
            if height > max_height:
                sunset_view_indices.insert(0, index)
                max_height = height
    return sunset_view_indices




class TestProgram(unittest.TestCase):
    def test_1(self):
        buildings = [3, 5, 4, 4, 3, 1, 3, 2]
        direction = "EAST"
        expected = [1, 3, 6, 7]
        actual = sunsetViews(buildings, direction)
        self.assertEqual(actual, expected)

    def test_2(self):
        buildings = [2, 4]
        direction = "WEST"
        expected = [0, 1]
        actual = sunsetViews(buildings, direction)
        self.assertEqual(actual, expected)

    def test_3(self):
        buildings = []
        direction = "WEST"
        expected = []
        actual = sunsetViews(buildings, direction)
        self.assertEqual(actual, expected)

    def test_4(self):
        buildings = [7, 1, 7, 8, 9, 8, 7, 6, 5, 4, 2, 5]
        direction = "EAST"
        expected = [4, 5, 6, 7, 11]
        actual = sunsetViews(buildings, direction)
        self.assertEqual(actual, expected)